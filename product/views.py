from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from product.models import Product, Images, CommentForm, Comment


def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)
    images = Images.objects.filter(product_id=product.id)
    comments = Comment.objects.filter(
        product_id=product.id,
        status='True'
    )

    form = CommentForm()

    context = {"product": product,
               "images": images,
               "comments": comments,
               "form": form}
    return render(request, "product/product_detail.html", context)


def addcomment(request, id):

    product = get_object_or_404(Product, id=id)

    if not request.user.is_authenticated:
        return JsonResponse({
            "status": "error",
            "message": "Yorum yapmak için giriş yapmalısınız"
        })

    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():

            Comment.objects.create(
                subject=form.cleaned_data['subject'],
                comment=form.cleaned_data['comment'],
                rate=form.cleaned_data['rate'],
                ip=request.META.get('REMOTE_ADDR'),
                product=product,
                user=request.user
            )

            return JsonResponse({
                "status": "success",
                "message": "Yorum Gönderildi"
            })

        temp=form.errors

        return JsonResponse({
            "status": "error",
            "errors": form.errors
        })

    return JsonResponse({
        "status": "error",
        "message": "Geçersiz istek"
    })
