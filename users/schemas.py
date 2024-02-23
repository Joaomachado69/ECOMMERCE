# No seu arquivo schemas.py

import graphene
from graphene_django import DjangoObjectType
from .models import Product, Supplier, CustomerReview, ShoppingCart, CartItem

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class SupplierType(DjangoObjectType):
    class Meta:
        model = Supplier

class CustomerReviewType(DjangoObjectType):
    class Meta:
        model = CustomerReview

class ShoppingCartType(DjangoObjectType):
    class Meta:
        model = ShoppingCart

class CartItemType(DjangoObjectType):
    class Meta:
        model = CartItem

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    all_suppliers = graphene.List(SupplierType)
    all_reviews = graphene.List(CustomerReviewType)
    all_shopping_carts = graphene.List(ShoppingCartType)
    all_cart_items = graphene.List(CartItemType)

    def resolve_all_products(self, info):
        return Product.objects.all()

    def resolve_all_suppliers(self, info):
        return Supplier.objects.all()

    def resolve_all_reviews(self, info):
        return CustomerReview.objects.all()

    def resolve_all_shopping_carts(self, info):
        return ShoppingCart.objects.all()

    def resolve_all_cart_items(self, info):
        return CartItem.objects.all()

schema = graphene.Schema(query=Query)
