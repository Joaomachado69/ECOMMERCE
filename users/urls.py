from django.urls import path,include
from .views import UserListCreate, UserRetrieveUpdateDelete

urlpatterns = [
    path('users', UserListCreate.as_view(),name="Create-User-List"),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(),name='user-Details')
]
