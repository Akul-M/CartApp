from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.


def allcategories(request, c_slug=None):
    c_page = None
    productsList = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        productsList = Product.objects.all().filter(category=c_page, available=True)
    else:
        productsList = Product.objects.all().filter(available=True)
    paginator = Paginator(productsList, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, "Category.html", {'category': c_page, 'products': products})

def productDetails(request, c_slug, p_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=p_slug)
    except Exception as e:
        raise e

    return render(request, "Product.html", {'product': product})
