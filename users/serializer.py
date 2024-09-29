from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [  "id", "name", "email", "password",]

    def create(self,validated_data):
        user = User(name=validated_data['name'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
