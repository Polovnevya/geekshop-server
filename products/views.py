from django.shortcuts import render
from django.utils import timezone
from .models import Product, ProductCategory


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


def products(request):
    context = {
        "title": "Каталог товаров GeekShop",
        "date_time": timezone.now,
    }
    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()
    return render(request, './products/products.html', context)
