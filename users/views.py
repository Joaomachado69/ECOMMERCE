from django.shortcuts import render
from rest_framework import generics
from .models import User
from.serializer import UserSerializer




#create a user and to display
class  UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



#to retrieve, update or delete a user by id
class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

