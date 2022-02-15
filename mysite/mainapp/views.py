from django.shortcuts import render
from .models import Product, ProductCategory

LINKS_MENU = [
    {'href': 'main', 'name': 'home'},
    {'href': 'products:index', 'name': 'shop'}
]


def main(request):
    products = Product.objects.all()[:9]
    content = {
        'title': 'Главная',
        'links_menu': LINKS_MENU,
        'products': products,
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    content = {
        'title': 'Продукты',
        'links_menu': LINKS_MENU,
        'categories': categories,
        'products': products,
    }
    return render(request, 'mainapp/shop.html', content)
