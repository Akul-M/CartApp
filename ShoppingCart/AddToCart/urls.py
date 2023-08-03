from . import views
from django.urls import path, include
app_name = 'AddToCartApp'

urlpatterns = [
    path('add/<int:productId>/', views.addToCart, name='addToCart'),
    path('remove/<int:productId>/', views.removeFromCart, name='removeFromCart'),
    path('delete/<int:productId>/', views.deleteFromCart, name='deleteFromCart'),
    path('', views.cart_details, name='cart_details'),
]
