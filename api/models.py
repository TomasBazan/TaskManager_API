from django.db import models
from users.models import User
from django.db.models.base import CASCADE


class Project(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owned_projects"
    )
    members = models.ManyToManyField(User, related_name="projects")

    def __str__(self):
        return f"{self.name}"


class Tasks(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    user_responsable = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{ self.name  } al projecto: { self.project.name }"
