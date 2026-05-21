from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
import json
from product.models import Product, Images, CommentForm, Comment, Variants, Color, Size



def addcomment(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    if not request.user.is_authenticated:

        return JsonResponse({
            "status": "error",
            "message": "Yorum yapmak için giriş yapmalısınız"
        })

    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():

            variant = None

            variant_id = request.POST.get(
                "variantid"
            )

            if variant_id:

                variant = Variants.objects.filter(
                    id=variant_id,
                    active=True
                ).first()

            Comment.objects.create(

                subject=form.cleaned_data['subject'],

                comment=form.cleaned_data['comment'],

                rate=form.cleaned_data['rate'],

                ip=request.META.get('REMOTE_ADDR'),

                product=product,

                variant=variant,

                user=request.user
            )

            return JsonResponse({
                "status": "success",
                "message": "Yorum Gönderildi"
            })

        return JsonResponse({
            "status": "error",
            "errors": form.errors
        })

    return JsonResponse({
        "status": "error",
        "message": "Geçersiz istek"
    })


def product_variant_detail(request, slug):

    active_variant = get_object_or_404(
        Variants,
        slug=slug,
        active=True
    )

    product = active_variant.product

    comments = Comment.objects.filter(
        variant=active_variant,
        status='True'
    )

    variants = product.variants.filter(
        active=True
    ).select_related(
        "color",
        "size",
        "image"
    )

    sizes = (
        Size.objects.filter(
            variants__product=product,
            variants__active=True
        ).distinct()
    )

    colors = (
        Color.objects.filter(
            variants__product=product,
            variants__active=True
        ).distinct()
    )

    variants_json = []

    for v in variants:

        variants_json.append({

            "id": v.id,

            "slug": v.slug,

            "url": v.get_absolute_url(),

            "size": (
                v.size.id if v.size else None
            ),

            "color": (
                v.color.id if v.color else None
            ),

            "size_name": (
                v.size.name if v.size else ""
            ),

            "color_name": (
                v.color.name if v.color else ""
            ),

            "color_code": (
                v.color.code if v.color else ""
            ),

            "price": str(v.price),

            "quantity": v.quantity,

            "image": (
                v.image.image.url
                if v.image and v.image.image
                else product.image.url
            )
        })

    context = {

        "product": product,

        "active_variant": active_variant,

        "variants": variants,

        "sizes": sizes,

        "colors": colors,

        "variants_json": variants_json,

        "comments": comments,
    }

    return render(
        request,
        "product/product_detail.html",
        context
    )


def product_detail(request, slug):

    product = get_object_or_404(
        Product,
        slug=slug
    )

    variants = product.variants.filter(
        active=True
    ).select_related(
        "color",
        "size",
        "image"
    )

    active_variant = variants.first()

    # =========================
    # COMMENTS
    # =========================

    if active_variant:

        comments = Comment.objects.filter(
            variant=active_variant,
            status='True'
        )

    else:

        comments = Comment.objects.filter(
            product=product,
            variant__isnull=True,
            status='True'
        )

    # =========================
    # UNIQUE SIZES
    # =========================

    sizes = (
        Size.objects.filter(
            variants__product=product,
            variants__active=True
        ).distinct()
    )

    # =========================
    # UNIQUE COLORS
    # =========================

    colors = (
        Color.objects.filter(
            variants__product=product,
            variants__active=True
        ).distinct()
    )

    # =========================
    # VARIANTS JSON
    # =========================

    variants_json = []

    for v in variants:

        variants_json.append({

            "id": v.id,

            "slug": v.slug,

            "url": v.get_absolute_url(),

            "size": (
                v.size.id if v.size else None
            ),

            "color": (
                v.color.id if v.color else None
            ),

            "size_name": (
                v.size.name if v.size else ""
            ),

            "color_name": (
                v.color.name if v.color else ""
            ),

            "color_code": (
                v.color.code if v.color else ""
            ),

            "price": str(v.price),

            "quantity": v.quantity,

            "image": (
                v.image.image.url
                if v.image and v.image.image
                else product.image.url
            )
        })

    context = {

        "product": product,

        "active_variant": active_variant,

        "variants": variants,

        "sizes": sizes,

        "colors": colors,

        "variants_json": variants_json,

        "comments": comments,
    }

    return render(
        request,
        "product/product_detail.html",
        context
    )