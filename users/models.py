from django.db import models
from django.utils import choices
from .roles import UserRoles


class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(
        max_length=50, choices=[(role.value, role.name) for role in UserRoles]
    )
