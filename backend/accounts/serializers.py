from .models import Account,UserProfile
from rest_framework import serializers

class AccountSerializers(serializers.Serializer):
    first_name=serializers.CharField(max_length=50)
    last_name=serializers.CharField(max_length=50)
    username=serializers.CharField(max_length=50,unique=True)
    email=serializers.EmailField(max_length=100,unique=True)
    phone_number=serializers.CharField(max_length=50)

    #required
    date_joined=serializers.DateTimeField(auto_now_add=True)
    last_login=serializers.DateTimeField(auto_now_add=True)
    is_admin=serializers.BooleanField(default=False)
    is_staff=serializers.BooleanField(default=False)
    is_active=serializers.BooleanField(default=False)
    is_superadmin=serializers.BooleanField(default=False)
    