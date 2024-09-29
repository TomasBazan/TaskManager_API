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
        User, on_delete=models.CASCADE, null=True, blank=True,
    )

    def __str__(self):
        return f"{ self.name  } al projecto: { self.project.name }"
# class ProjectSerializer(serializers.ModelSerializer):  # Changed to ModelSerializer
#     owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Now expects a user ID
#
#     class Meta:
#         model = Project
#         fields = ["id", "name", "owner"]
#
#     def create(self, validated_data):
#         validated_data['owner'] = self.context['request'].user
#         return super().create(validated_data)
#
#
# class TasksSerializer(serializers.HyperlinkedModelSerializer):
#     user_responsable = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True)
#
#     class Meta:
#         model = Tasks
#         fields = ["url", "id", "name", "description", "done", "user_responsable"]
#         extra_kwargs = {
#             'url': {'view_name': 'tasks-detail', 'lookup_field': 'pk'}  # Ensure correct view for URL
#         }
