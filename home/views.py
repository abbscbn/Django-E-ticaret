import json
from asyncio import log

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

import product
from home.forms import SearchForm
from home.models import Setting, ContactForm, ContactMessage
from product.models import Product, Category, Variants
from users.models import UserProfile


# Create your views here.
def index(request):


    setting = Setting.objects.get(pk=1)

    parent_categories = Category.objects.filter(
        parent__isnull=True,
        status='True'
    )

    category_products = []

    for parent in parent_categories:

        children = parent.get_descendants(include_self=True)

        products = Product.objects.filter(
            category__in=children,
            status='True'
        )

        if products.exists():
            category_products.append({
                "category": parent,
                "products": products
            })

    products = Product.objects.filter(
        status=True
    )

    variants = (
        Variants.objects.filter(
            active=True
        )
        .select_related(
            'product',
            'image'
        )
    )
    categorys = Category.objects.all()

    context = {
        'setting': setting
        , 'page': 'home'
        , 'products': products
        , 'variants': variants
        , 'categorys': categorys
        ,'category_products': category_products
    }

    return render(request, 'home/index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'aboutus'}  # burada hangi sayafaya ilettiğimizi belli etmek amaçlı page parametreside gönderebiliriz
    return render(request, 'home/aboutus.html', context)


def contactus(request):
    if request.method == 'POST':  # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(request, "Mesjaınız iletildi.Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)

    form = ContactForm
    context = {'setting': setting, 'form': form}
    return render(request, 'home/contact.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)

    children = category.get_children()

    # Eğer alt kategori varsa
    if children.exists():
        context = {
            'category': category,
            'children': children,
            'page': 'subcategory'
        }

        return render(
            request,
            'home/subcategories.html',
            context
        )

    # 🔥 ARTIK PRODUCT DEĞİL VARIANT
    variants = (
        Variants.objects
        .filter(
            product__category=category,
            active=True
        )
        .select_related(
            "product"

        )
    )

    products = (
        Product.objects.filter(
            category=category,
        )
    )

    context = {
        'category': category,
        'page': 'variants',
        'products': products,
    }

    return render(
        request,
        'home/category_products.html',
        context
    )


def search(request):
    if request.method == 'POST':

        form = SearchForm(request.POST)

        if form.is_valid():
            query = form.cleaned_data['query']

            variants = (
                Variants.objects
                .filter(
                    title__icontains=query,
                    active=True
                )
                .select_related(
                    "product",
                    "image",
                )
            )

            context = {
                'variants': variants,
                'query': query
            }

            return render(
                request,
                'home/search_products.html',
                context
            )

    return HttpResponseRedirect('/')


def search_auto(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        q = request.GET.get('term', '')

        variants = (
            Variants.objects
            .filter(
                title__icontains=q,
                active=True
            )[:10]
        )

        results = []

        for v in variants:
            results.append(v.title)

        return JsonResponse(results, safe=False)

    return JsonResponse([], safe=False)
