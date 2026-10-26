from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request):
    return render(request, "shop/home.html", {
        "products": Product.objects.all(),
        "categories": Category.objects.all(),
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, "shop/home.html", {
        "products": category.products.all(),
        "categories": Category.objects.all(),
        "current": category,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "shop/product_detail.html", {"product": product})