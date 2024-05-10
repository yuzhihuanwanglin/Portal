from django.contrib import admin

# Register your models here.
import xadmin
from productsApp.models import Product


class ProductsAdmin(object):
    list_display = ['title', 'photo', 'productType', 'price', 'publishDate', 'views']
    fields = ['title', 'description', 'photo', 'productType', 'price', 'publishDate', 'views']


xadmin.site.register(Product, ProductsAdmin)
