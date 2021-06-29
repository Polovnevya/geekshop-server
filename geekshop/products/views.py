from django.shortcuts import render
import json
from pathlib import Path
from django.utils.datetime_safe import datetime

# Create your views here.



def index(request):
    context = {

        "title": "GeekShop",
        "date_time": datetime.now(),
        "username": "Иван Иванов",
        "is_promotion": 1,
        "promotion_text": "Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям."
    }
    return render(request, './products/index.html', context)


def products(request):
    fixture_path = str(Path(__file__).resolve().parent)
    fixture_path += '\\fixtures\\products.json'
    with open(fixture_path, encoding='utf-8') as f:
        result = json.load(f)

    context = {
        'title': 'Каталог товаров'
    }
    context.update(result)
    return render(request, 'products/products.html', context)
