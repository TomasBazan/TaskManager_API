from rest_framework import serializers
from django.db import models
from .models import Project, Tasks
from users.models import User


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ["url", "id", "name"]


class TasksSerializer(serializers.HyperlinkedModelSerializer):
    user_responsable = serializers.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        model = Tasks
        fields = ["url", "id", "name", "description", "done"]
