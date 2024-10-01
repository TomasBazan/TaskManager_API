from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils import choices
from .roles import UserRoles

class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)

class User(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True)
    role = models.CharField(
        max_length=50, choices=[(role.value, role.name) for role in UserRoles]
    )
    email = models.EmailField(unique=True, max_length=255)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_by_natural_key(self):
        return self.username