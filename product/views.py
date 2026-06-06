from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
import json
from product.models import Product, Images, CommentForm, Comment, Variants, Category


def addcomment(request):


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

    active_attributes = list(
        active_variant.attributes.values_list(
            "id",
            flat=True
        )
    )

    product = active_variant.product


    comments = Comment.objects.filter(
        variant=active_variant,
        status='True'
    )

    variants = (
        product.variants
        .filter(active=True)
        .prefetch_related(
            "attributes",
            "attributes__attribute",
            "image"
        )
    )

    attribute_groups = {}

    for variant in variants:

        for attr_value in variant.attributes.all():

            attr_name = attr_value.attribute.name

            if attr_name not in attribute_groups:
                attribute_groups[attr_name] = []

            if attr_value not in attribute_groups[attr_name]:
                attribute_groups[attr_name].append(attr_value)






    variants_json = []



    for v in variants:

        variants_json.append({

            "id": v.id,

            "slug": v.slug,

            "url": v.get_absolute_url(),

            "price": str(v.price),

            "quantity": v.quantity,

            "image": (
                v.image.image.url
                if v.image and v.image.image
                else product.image.url
            ),

            "attributes": list(
                v.attributes.values_list(
                    "id",
                    flat=True
                )
            )

        })

    context = {

        "product": product,

        "active_variant": active_variant,

        "variants": variants,

        "active_attributes": active_attributes,

        "attribute_groups": attribute_groups,

        "variants_json": variants_json,

        "comments": comments,
    }

    return render(
        request,
        "product/product_detail.html",
        context
    )


