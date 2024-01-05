from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import OrderForm
from .models import Order,OrderProduct,Payment
import datetime
from accounts.models import UserProfile
from django.contrib import messages
from cart.models import Cart,CartItem
from cart.views import _cart_id
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from . import Checksum
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from core.settings import CUSTOMER_SUPPORT_FULL_NAME,CUSTOMER_SUPPORT_NUMBER



MERCHANT_KEY = '3t#5!NX7dvT&GNLL'


################### Checkout ########################     
################### Checkout ########################     
################### Checkout ########################     

@login_required(login_url="accounts:login")
def checkout(request):
    if request.user.is_authenticated:
        tax = 0
        grand_total = 0
        orderform = OrderForm()
        total = 0  # Initialize total before the loop
        quantity = 0  # Initialize quantity before the loop
        useraddress=UserProfile.objects.get(user=request.user)

        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        
            for cart_item in cart_items:
                total += (cart_item.product.price * cart_item.quantity)
                quantity += cart_item.quantity

            tax = (4 * total) / 100
            grand_total = total + tax

        except Cart.DoesNotExist:
            pass

        context = {
            'cart_items': cart_items,
            'cart_total_amount': grand_total,
            'order_form': orderform,
            'tax':tax,
            'useraddress':useraddress,
        }

        return render(request, 'store/checkout.html', context)
    else:
        # Handle the case when the user is not authenticated
        # Redirect to the login page or display an appropriate message
        # For example:
        messages.warning(request, "Please log in to proceed with checkout.")
        return redirect('account_login')  
    

################### Place order ########################  

@login_required(login_url="accounts:login")
def place_order(request):
    current_user=request.user
    if request.method=="POST":
        form=OrderForm(request.POST)
        amount=request.POST.get('checkout_order_total')
        tax=request.POST.get('checkout_tax')
        if form.is_valid():
            #storing all the billing details here
            data = Order()
            data.user=current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.email=form.cleaned_data['email']

            data.order_total = amount
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            #generate order number

            yr=int(datetime.date.today().strftime('%Y'))
            dt=int(datetime.date.today().strftime('%d'))
            mt=int(datetime.date.today().strftime('%m'))
            d=datetime.date(yr,mt,dt)
            current_date=d.strftime("%Y%m%d")
            order_number=current_date+str(data.id)
            data.order_number=order_number
            data.save()
            order=Order.objects.get(user=current_user,is_ordered=False,order_number=order_number)
            order.is_ordered=True
            order.save()
            tax = 0
            grand_total = 0
            total = 0  # Initialize total before the loop
            quantity = 0  # Initialize quantity before the loop

            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                cart_items = CartItem.objects.filter(cart=cart, is_active=True)
            
                for cart_item in cart_items:
                    total += (cart_item.product.price * cart_item.quantity)
                    quantity += cart_item.quantity
                    OrderProduct.objects.create(product=cart_item.product,user=request.user,quantity=cart_item.quantity,product_price=cart_item.product.price,ordered=True,order=order)
                    cart_item.delete()

                tax = (4 * total) / 100
                grand_total = total + tax
            except Cart.DoesNotExist:
                pass
            
            current_site=get_current_site(request)
            order_products=OrderProduct.objects.filter(order__order_number=order_number)
            mail_subject='Order Confirmation and Payment Steps for Your Recent Purchase from Mittal Mart'
            message=render_to_string('mail_templates/ordered_email.html',
                                    {'user':current_user,
                                        'order_id':order_number,
                                        'purchase_date':current_date,
                                        'amount':amount,
                                        'current_site':current_site,
                                        'customer_support_number':CUSTOMER_SUPPORT_NUMBER,
                                     'customer_support_full_name':CUSTOMER_SUPPORT_FULL_NAME,
                                     'order_products':order_products})
            to_email=current_user.email
            send_email=EmailMessage(mail_subject,message,to=[to_email])
            send_email.content_subtype = 'html'
            send_email.send()
            # adding the products in orderproduct
            
            #Request paytm to transfer the payment to account
            param_dict={
                "MID": "PCMqdH35575073023736",
                "ORDER_ID": str(order.order_number),
                "TXN_AMOUNT": str(order.order_total),
                "CUST_ID": order.email,
                "CHANNEL_ID": "WEB",
                "INDUSTRY_TYPE_ID": "Retail",
                "WEBSITE": "WEBSTAGING",
                "CALLBACK_URL":"http://127.0.0.1:8000/order/handlerequest/",
            }
            param_dict['CHECKSUMHASH']=Checksum.generate_checksum(param_dict,MERCHANT_KEY)
            return render(request,"orders/paytm.html",{'param_dict':param_dict})
        else:
            print(form.errors)
            return redirect("order:checkout")
                
    else:
        return redirect("order:checkout")

#################  payments ###################

@login_required(login_url="accounts:login")
def payments(request,order_id):
    order=Order.objects.get(order_number=order_id)
    param_dict={
                "MID": "PCMqdH35575073023736",
                "ORDER_ID": str(order.order_number),
                "TXN_AMOUNT": str(order.order_total),
                "CUST_ID": order.email,
                "CHANNEL_ID": "WEB",
                "INDUSTRY_TYPE_ID": "Retail",
                "WEBSITE": "WEBSTAGING",
                "CALLBACK_URL":"http://127.0.0.1:8000/order/handlerequest/",
            }
    param_dict['CHECKSUMHASH']=Checksum.generate_checksum(param_dict,MERCHANT_KEY)
    print(param_dict)
    return render(request,"orders/paytm.html",{'param_dict':param_dict})

@csrf_exempt
@login_required(login_url="accounts:login")
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        print(i)
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
            print(checksum)

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            order_id=response_dict['ORDER_ID']
            order=Order.objects.get(order_number=order_id)
            payment=Payment.objects.create(payment_method="online",status="success",user=request.user)
            order.payment=payment
            current_site=get_current_site(request)
            mail_subject='Order Confirmation and Payment Steps for Your Recent Purchase from Mittal Mart'
            message=render_to_string('mail_templates/payment_completion.html',
                                    {'user':request.user,
                                        'order_id':order.order_number,
                                        'purchase_date':order.updated_at,
                                        'amount':order.order_total,
                                        'current_site':current_site,
                                        'customer_support_number':CUSTOMER_SUPPORT_NUMBER,
                                     'customer_support_full_name':CUSTOMER_SUPPORT_FULL_NAME})
            to_email=request.user.email
            send_email=EmailMessage(mail_subject,message,to=[to_email])
            send_email.content_subtype = 'html'
            send_email.send()
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'orders/paymentstatus.html', {'response': response_dict})

