from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import choices
from .roles import UserRoles


class User(AbstractBaseUser):
    name = models.CharField(max_length=200)
    role = models.CharField(
        max_length=50, choices=[(role.value, role.name) for role in UserRoles]
    )
    email = models.EmailField(unique=True, max_length=255)
