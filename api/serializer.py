from rest_framework import serializers
from .models import Project, Tasks


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ["url", "id", "name"]
