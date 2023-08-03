from django.shortcuts import render
from CartApp.models import Category, Product
from django.db.models import Q
# Create your views here.

def searchResults(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(productName__contains=query) | Q(description__contains=query))
        return render(request, 'Search.html', {'query': query, 'products': products})
