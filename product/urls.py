from django.urls import path

from product import views

urlpatterns = [
    path('addcomment/<int:id>/', views.addcomment, name='addcomment'),

    # 🔥 PRODUCT (fallback page)
    path('<slug:slug>/', views.product_detail, name='product_detail'),

    # 🔥 VARIANT (asıl SEO page)
    path('<slug:slug>/v/', views.product_variant_detail, name='product_variant_detail'),

]
