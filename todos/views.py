from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class ListCreateTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailUpdateDestroyTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
