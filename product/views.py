from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {"product": product}
    return render(request, "product/product_detail.html", context)
