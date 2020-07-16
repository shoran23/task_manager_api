from django.shortcuts import render
from rest_framework import generics, permissions

from .permissions import IsAuthorOrReadOnly

from .models import Category
from .models import Task
from .models import Detail
from django.contrib.auth.models import User

from .serializers import CategorySerializer
from .serializers import TaskSerializer
from .serializers import DetailSerializer
from .serializers import UserSerializer

from django.http import HttpResponse

# Category Views -----------------------------------------------------------
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Task Views -----------------------------------------------------------------
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Detail Views ----------------------------------------------------------------
class DetailList(generics.ListCreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

class DetailDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

# User Views ------------------------------------------------------------------
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView): 
#     queryset = User.objects.filter(username='username')
#     serializer_class = UserSerializer

def UserDetail(request, username):
    return HttpResponse('<h1>This is the given username: {}</h1>'.format(username))

