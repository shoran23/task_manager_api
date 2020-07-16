from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category
from .models import Task
from .models import Detail

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'color', 'created_at', 'updated_at')
        model = Category

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'completed', 'created_at', 'updated_at',)
        model = Task

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'task', 'body','completed')
        model = Detail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = User