from django.urls import path

from product import views

urlpatterns = [
    path(
        'addcomment/<int:id>/',
        views.addcomment,
        name='addcomment'
    ),

    path(
        '<slug:slug>/',
        views.product_detail,
        name='product_detail'
    ),

]
