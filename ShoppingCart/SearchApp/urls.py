from . import views
from django.urls import path, include
app_name = 'SearchApp'

urlpatterns = [
    path('', views.searchResults, name='searchResults'),
]
