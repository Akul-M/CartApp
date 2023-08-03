from django.shortcuts import render, redirect, get_object_or_404
from CartApp.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def addToCart(request, productId):
    product = Product.objects.get(id=productId)
    cart_id = _cart_id(request)
    try:
        cart = Cart.objects.get(cartId=cart_id)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cartId=cart_id)
        cart.save()
    try:
        cartItem = CartItem.objects.get(product=product, cart=cart)
        if cartItem.quantity < cartItem.product.stock:
            cartItem.quantity += 1
            cartItem.save()
    except CartItem.DoesNotExist:
        cartItem = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cartItem.save()

    return redirect('AddToCartApp:cart_details')

def cart_details(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cartId=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for c_item in cart_items:
            total += (c_item.product.price * c_item.quantity)
            counter += c_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'Cart.html', dict(cart_items=cart_items, total=total, counter=counter))

def removeFromCart(request, productId):
    product = get_object_or_404(Product, id=productId)
    cart_id = _cart_id(request)
    cart = Cart.objects.get(cartId=cart_id)
    cartItem = CartItem.objects.get(product=product, cart=cart)
    if cartItem.quantity > 1:
        cartItem.quantity -= 1
        cartItem.save()
    else:
        cartItem.delete()
    return redirect('AddToCartApp:cart_details')

def deleteFromCart(request, productId):
    product = get_object_or_404(Product, id=productId)
    cart_id = _cart_id(request)
    cart = Cart.objects.get(cartId=cart_id)
    cartItem = CartItem.objects.get(product=product, cart=cart)
    cartItem.delete()
    return redirect('AddToCartApp:cart_details')



