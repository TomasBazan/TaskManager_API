from .models import Project, Tasks
from rest_framework import viewsets
from .serializer import ProjectSerializer, TasksSerializer
from rest_framework.permissions import IsAuthenticated


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class TasksViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()
