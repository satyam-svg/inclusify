from rest_framework.response import Response
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .serializers import AccountSerializers
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.views import APIView
User=settings.AUTH_USER_MODEL
# Create your views here.


class RegisterView(APIView):
    def post(self,request):
        serializer=AccountSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self,request):
        pass  
   
