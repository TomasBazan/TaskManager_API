from django.db import models
from django.db.models.base import CASCADE

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)

    def __srt__(self):
        return self.name


class Tasks(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __srt__(self):
        return self.name + "al projecto: " + self.project.name
