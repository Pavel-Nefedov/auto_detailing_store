import random
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Category, Product
# from basket.models import Basket

def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]

def products(request, pk=None, page=1):
    title = 'каталог'
    categories = Category.objects.all()
    hot_product = get_hot_product()
    products = Product.objects.all().order_by('price')

    if pk is not None:
        if pk ==0:
            products = Product.objects.all().order_by('price')
            category = {'pk': 0, 'name': 'Все'}
        else:
            category = get_object_or_404(Category, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        paginator = Paginator(products, 2)

        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'title': title,
            'categories': categories,
            'products': products_paginator,
            'category': category,
            'hot_product': hot_product
        }

        return render(request, '../templates/products.html', context)

    paginator = Paginator(products, 2)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'categories': categories,
        'hot_product': hot_product,
        'products': products
    }

    return render(request, '../templates/products.html', context)

def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': Category.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
    }

    render(request, '../templates/product_detail.html', content)