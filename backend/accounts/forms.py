from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account,UserProfile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=Account
        fields=['first_name','last_name','email','phone_number','password1', 'password2']
    
    def _init_(self, *args, **kwargs):
        super(UserRegistrationForm,self)._init_(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder']='Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter Phone Numbar'
        self.fields['email'].widget.attrs['placeholder']='Enter Email Address'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    def clean(self):
        cleaned_data=super(UserRegistrationForm,self).clean()
        password=cleaned_data.get('password1')
        confirm_password=cleaned_data.get('password2')

        if password!=confirm_password:
            raise forms.ValidationError(
                "Password does not Match"
            )
        
class UserForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=('first_name','last_name','phone_number')
    def _init_(self, *args, **kwargs):
        super(UserForm,self)._init_(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(
        required=False,
        error_messages={'Invalid': ("Image files only")},
        widget=forms.FileInput(attrs={'class': 'custom-file-input', 'id': 'customFile'})
    )

    class Meta:
        model = UserProfile
        fields = ('profile_pic', 'address_line_1', 'address_line_2', 'city', 'state', 'country')

    def _init_(self, *args, **kwargs):
        super(UserProfileForm, self)._init_(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'