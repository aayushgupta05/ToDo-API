from django.urls import path
from .views import ListCreateTodo, DetailUpdateDestroyTodo

urlpatterns = [
    path('<int:pk>/', DetailUpdateDestroyTodo.as_view()),
    path('', ListCreateTodo.as_view()),
]
