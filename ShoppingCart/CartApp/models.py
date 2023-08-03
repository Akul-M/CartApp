from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    categoryImage = models.ImageField(upload_to='categoryImgs', blank=True)

    class Meta:
        ordering = ('categoryName',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('CartApp:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.categoryName)


class Product(models.Model):
    productName = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    productImage = models.ImageField(upload_to='productImgs', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('productName',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('CartApp:productDetails', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.productName)




