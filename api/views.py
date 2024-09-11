from django.http import JsonResponse
from django.shortcuts import render
from .models import Project, Tasks
from rest_framework import viewsets
from .serializer import ProjectSerializer, TasksSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()
