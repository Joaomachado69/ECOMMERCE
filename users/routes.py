from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ShoppingCart, CartItem ,User

@api_view(['POST'])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)
    user_id = request.data.get('user_id')  # Supondo que você passe o id do usuário na requisição

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    cart, created = ShoppingCart.objects.get_or_create(user=user)

    cart_item, created = CartItem.objects.get_or_create(
        shopping_cart=cart,
        product=product
    )
    if not created:
        cart_item.quantity += int(quantity)
        cart_item.save()

    return Response({'message': 'Product added to cart successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def remove_from_cart(request):
    product_id = request.data.get('product_id')
    user_id = request.data.get('user_id')

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        cart_item = CartItem.objects.get(shopping_cart__user=user, product=product)
        cart_item.delete()
        return Response({'message': 'Product removed from cart successfully'}, status=status.HTTP_200_OK)
    except CartItem.DoesNotExist:
        return Response({'error': 'Product is not in the cart'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_cart_item(request):
    product_id = request.data.get('product_id')
    user_id = request.data.get('user_id')
    quantity = request.data.get('quantity')

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        cart_item = CartItem.objects.get(shopping_cart__user=user, product=product)
        cart_item.quantity = quantity
        cart_item.save()
        return Response({'message': 'Cart item updated successfully'}, status=status.HTTP_200_OK)
    except CartItem.DoesNotExist:
        return Response({'error': 'Product is not in the cart'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def checkout(request):
    user_id = request.data.get('user_id')

    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        cart = ShoppingCart.objects.get(user=user)
    
        for cart_item in cart.cartitem_set.all():
            create_order(cart_item.product, cart_item.quantity, user)
        cart.cartitem_set.all().delete()  # Limpa o carrinho após a compra
        return Response({'message': 'Checkout successful'}, status=status.HTTP_200_OK)
    except ShoppingCart.DoesNotExist:
        return Response({'error': 'Shopping cart not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_to_cart(request):
    user_id = request.data.get('user_id')
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    cart, created = ShoppingCart.objects.get_or_create(user=user)

    cart_item, created = CartItem.objects.get_or_create(shopping_cart=cart, product=product)
    if not created:
        cart_item.quantity += int(quantity)
        cart_item.save()

    return Response({'message': 'Product added to cart successfully'}, status=status.HTTP_200_OK)
