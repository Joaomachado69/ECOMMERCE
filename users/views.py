from django.shortcuts import render
from rest_framework import generics
from .models import User
from.serializer import UserSerializer
from django.http import JsonResponse
from .search import search_products



#create a user and to display
class  UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



#to retrieve, update or delete a user by id
class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




def product_search(request):
    query = request.GET.get('q', '')
    results = search_products(query)
    return JsonResponse(results, safe=False)
