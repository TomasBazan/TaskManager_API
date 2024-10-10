from rest_framework import viewsets, generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UserSerializer, RegisterSerializer, CustomTokenObtainSerializer
from .models import User


# Older pre-built version
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer
    pass
