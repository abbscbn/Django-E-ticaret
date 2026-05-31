from django.urls import path

from product import views

urlpatterns = [
    path('addcomment', views.addcomment, name='addcomment'),

    # 🔥 PRODUCT (fallback page)


    # 🔥 VARIANT (asıl SEO page)
    path('<slug:slug>/v/', views.product_variant_detail, name='product_variant_detail'),

]
