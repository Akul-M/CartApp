from .models import CartItem, Cart
from .views import _cart_id

def counter(request):
    cart_id = _cart_id(request)
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cartId=cart_id)
            cartItem = CartItem.objects.all().filter(cart=cart[:1])
            for c_item in cartItem:
                item_count += c_item.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)