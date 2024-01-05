from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate
from .forms import UserRegistrationForm,UserProfileForm,UserForm
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Account,UserProfile
from order.models import OrderProduct,Order
# from vendor.models import Vendor
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.exceptions import ObjectDoesNotExist


User=settings.AUTH_USER_MODEL
# Create your views here.

def register_view(request):
   if request.method == "POST":
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
         first_name = form.cleaned_data.get("first_name")
         last_name = form.cleaned_data.get("last_name")
         email = form.cleaned_data.get("email")
         phone_number = form.cleaned_data.get("phone_number")
         password = form.cleaned_data.get("password1")
         username = email.split('@')[0]
   
         user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
         user.phone_number = phone_number
         user.save()

         # User Activation
         current_site=get_current_site(request)
         mail_subject='Please activate your account'
         message=render_to_string('user/account_verification_email.html',
                                  {'user':user,
                                    'domain':current_site,
                                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                                    'token':default_token_generator.make_token(user),})
         to_email=email
         send_email=EmailMessage(mail_subject,message,to=[to_email])
         send_email.send()
         #messages.success(request,'Thank you for registering with us. We have sent you verification email to your address. Please verify it.')
         return redirect('/accounts/login/?command=verification&email='+email)

      else:
         print(form.errors)
       
    
   # If the request method is not POST or the form is not valid
   form = UserRegistrationForm()
   context = {
      'form': form,
   }
   return render(request, "user/sign-up.html", context)

def login_view(request):
   if request.user.is_authenticated:
      messages.success(request,f"Already logged In.")
      return redirect("store:home")
   if request.method=="POST":
      email=request.POST.get("email")
      password=request.POST.get("password")
      role=request.POST.get('role')
      if role == "" or role == "user":
         user=authenticate(request,email=email,password=password)
         if user is not None:
            login(request,user)
            messages.success(request,f"Your logged in.")
            return redirect("store:home")
         else:
            messages.error(request,f"Invalid login credentials")
            return redirect("accounts:login")
      elif role == "vendor":
         user=authenticate(request,email=email,password=password)
         if user is not None:
            try:
               vendor_user=Account.objects.get(email=email)
               vendor=Vendor.objects.filter(user=vendor_user).first()
               if vendor:
                  login(request,user)
                  return redirect("vendor:vendors_dashboard")
            except:
               messages.error(request,f"Invalid login credentials")
               return redirect("accounts:login")
         else:
            messages.error(request,f"Invalid login credentials")
            return redirect("accounts:login")
   
   return render(request,"user/login.html")

@login_required(login_url='accounts:login')
def user_logout(request):
   logout(request)
   messages.success(request,"You are logged out.")
   return redirect('accounts:login')

def activate(request,uidb64,token):
   try:
      uid=urlsafe_base64_decode(uidb64).decode()
      user=Account._default_manager.get(pk=uid)
   except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
      user=None
   if user is not None and default_token_generator.check_token(user,token):
      user.is_active=True
      user.save()
      messages.success(request,'Congratulations! Your account in activated.')
      return redirect('accounts:login')
   else:
      messages.error(request,'Invalid activation link')
      return redirect('accounts:sign-up')


def forget_password(request):
   if request.method=='POST':
      email=request.POST['email']
      print(email)
      try:
         user=Account.objects.get(email__exact=email)

         #reset password mail
         current_site=get_current_site(request)
         mail_subject='Reset Your Password'
         message=render_to_string('mail_templates/reset_password_email.html',
                                  {'user':user,
                                    'domain':current_site,
                                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                                    'token':default_token_generator.make_token(user),})
         to_email=email
         send_email=EmailMessage(mail_subject,message,to=[to_email])
         send_email.send()
         messages.success(request,"Password reset email has been sent to your email address.")
         return redirect('accounts:login')

      except ObjectDoesNotExist:
         messages.error(request,"Account does not exist!")
         return redirect("accounts:forget_password")

   return render(request,"user/forget_password.html")


def reset_password_validate(request,uidb64,token):
   try:
      uid=urlsafe_base64_decode(uidb64).decode()
      user=Account._default_manager.get(pk=uid)
   except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
      user=None
   if user is not None and default_token_generator.check_token(user,token):
      request.session['uid']=uid
      messages.success(request,'Please reset your password')
      return redirect('accounts:resetPassword')
   else:
      messages.error(request,'This link has been expired!')
      return redirect('accounts:login')

def resetPassword(request):
   if request.method=="POST":
      password=request.POST['password']
      confirm_password=request.POST['confirm_password']

      if password == confirm_password:
         uid=request.session.get('uid')
         user=Account.objects.get(pk=uid)
         user.set_password(password)
         user.save()
         messages.success(request,"Password reset successful.")
         return redirect('accounts:login')
      else:
         messages.error(request,"Password does not match")
         return redirect('accounts:resetPassword')
   return render(request,'user/resetPassword.html')

#########################user Dashboard#####################
#########################user Dashboard#####################
#########################user Dashboard#####################

@login_required(login_url='accounts:login')
def user_dashboard(request):
      orders=Order.objects.order_by('created_at').filter(user_id=request.user.id,is_ordered=True)
      orders_count=orders.count()
      try:
         user_profile = UserProfile.objects.get(user=request.user)
      except UserProfile.DoesNotExist:
         # Handle the case when no UserProfile is found for the given query
         # For example, you may want to create a new UserProfile in this case
         user_profile = UserProfile.objects.create(user=request.user)
      context={
            'orders_count':orders_count,
             'user_profile':user_profile,
      }
      return render(request,'userdashboard/dashboard.html',context)

@login_required(login_url='accounts:login')
def oder_page_view(request):
      orders=Order.objects.filter(user=request.user,is_ordered=True).order_by('-created_at')
      context={
            'orders':orders
      }
      return render(request,'userdashboard/order_page.html',context)

@login_required(login_url='accounts:login')
def track_order_view(request):
      orders=Order.objects.filter(user=request.user,is_ordered=True).order_by('-created_at')
      context={
            'orders':orders
      }
      return render(request,'userdashboard/track_order.html',context)

@login_required(login_url='accounts:login')
def edit_profile_page_view(request):
      if request.user.is_authenticated:
         try:
            user_profile = UserProfile.objects.get(user=request.user)
         except UserProfile.DoesNotExist:
            # Handle the case when no UserProfile is found for the given query
            # For example, you may want to create a new UserProfile in this case
            user_profile = UserProfile.objects.create(user=request.user)
         if request.method=='POST':
            user_form=UserForm(request.POST,instance=request.user)
            profile_form=UserProfileForm(request.POST,request.FILES,instance=user_profile)
            if user_form.is_valid() and profile_form.is_valid():
               user_form.save()
               profile_form.save()
               messages.success(request,"Your profile has been updated.")  
               context={
                  'user_form':user_form,
                  'profile_form':profile_form,
               } 
               return render(request,'userdashboard/edit_profile.html',context)
         else:
            user_form=UserForm(instance=request.user)   
            profile_form=UserProfileForm(instance=user_profile)    
            context={
               'user_form':user_form,
               'profile_form':profile_form,
               'user_profile':user_profile,
            } 
      
    
      return render(request,'userdashboard/edit_profile.html',context)

@login_required(login_url='accounts:login')
def change_password(request):
   if request.method=="POST":
      current_password=request.POST['current_password']
      new_password=request.POST['new_password']
      confirm_password=request.POST['confirm_password']

      user=Account.objects.get(username__exact=request.user.username)
      if new_password==confirm_password:
         success=user.check_password(current_password)
         if success:
            user.set_password(new_password)
            user.save()
            messages.success(request,"Password updated successfully")
            return redirect('accounts:change_password')
         else:
            messages.error(request,'Please enter a valid correct password.')
            return redirect('accounts:change_password')
      else:
         messages.error(request,"Password does not match")
         return redirect('accounts:change_password')

   return render(request,'userdashboard/change_password.html')
