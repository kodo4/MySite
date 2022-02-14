from django.shortcuts import render

LINKS_MENU = [
    {'href': 'main', 'name': 'home'},
    {'href': 'products', 'name': 'shop'}
]


def main(request):
    content = {
        'title': 'Главная',
        'links_menu': LINKS_MENU,
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'Продукты',
        'links_menu': LINKS_MENU,
    }
    return render(request, 'mainapp/shop.html', content)
