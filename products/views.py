from django.shortcuts import render
from django.utils import timezone
from .models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
    context = {

        "title": "GeekShop",
        "date_time": timezone.now,
        "username": "Иван Иванов",
        "is_promotion": 1,
        "promotion_text": "Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям."
    }
    return render(request, './products/index.html', context)


def products(request, category_id=None, page=1):
    context = {
        "title": "Каталог товаров GeekShop",
        "date_time": timezone.now,
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, './products/products.html', context)
