from rest_framework import serializers
from django.db import models
from .models import Project, Tasks
from users.models import User


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = [ "id", "name", "owner"]

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


class TasksSerializer(serializers.HyperlinkedModelSerializer):
    user_responsable = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True)
    class Meta:
        model = Tasks
        fields = ["url", "id", "name", "description", "done", 'user_responsable']
