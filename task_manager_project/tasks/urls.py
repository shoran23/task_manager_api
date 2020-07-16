from django.urls import path
from .views import CategoryList, CategoryDetail
from .views import TaskList, TaskDetail
from .views import DetailList, DetailDetail
from .views import UserList, UserDetail
from . import views

urlpatterns = [
    # category views
    path('/categories/<int:pk>', CategoryDetail.as_view()),
    path('/categories', CategoryList.as_view()),
    # task views
    path('/tasks/<int:pk>/', TaskDetail.as_view()),
    path('/tasks', TaskList.as_view()),
    # detail views
    path('/details/<int:pk>/', DetailDetail.as_view()),
    path('/details', DetailList.as_view()),

    # user views
    path('/users/<username>/', views.UserDetail),
    path('/users', UserList.as_view()),
]