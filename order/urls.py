from django.urls import path

from order import views

urlpatterns = [

    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
]
