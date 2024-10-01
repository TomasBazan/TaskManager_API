from django.shortcuts import render
from requests import Response
from rest_framework import viewsets,status,generics
from rest_framework.views import APIView 
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UserSerializer, RegisterSerializer
from .models import User

#Older pre-built version
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             user.set_password(serializer.validated_data['password'])
#             user.save()
#             return Response({"message":" User registered successfully"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer 
class LoginView(TokenObtainPairView):
    pass

# class LogoutView(APIView):
