from django.urls import path,include
from .views import UserListCreate, UserRetrieveUpdateDelete
from graphene_django.views import GraphQLView
from .schemas import schema
from. import views


urlpatterns = [
    path('users', UserListCreate.as_view(),name="Create-User-List"),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(),name='user-Details'),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    path('search/', views.product_search, name='product_search'),
]
