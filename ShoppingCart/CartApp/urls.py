from . import views
from django.urls import path, include
app_name = 'CartApp'

urlpatterns = [
    path('', views.allcategories, name='allCategories'),
    path('<slug:c_slug>/', views.allcategories, name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/', views.productDetails, name='productDetails'),

]
