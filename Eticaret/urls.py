"""
URL configuration for Eticaret project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import home
from home import views

from users import views as UserViews

urlpatterns = [
                  path('', include("home.urls")),
                  path('home/', include("home.urls")),
                  path('product/', include("product.urls")),
                  path('users/', include('users.urls')),
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('hakkimizda/', views.aboutus, name='aboutus'),
                  path('iletisim/', views.contactus, name='contact'),
                  path(
                      'category/<slug:slug>/',
                      views.category_detail,
                      name='category_detail'
                  ),
                  path('search/', views.search, name='search'),
                  path('search_auto/', views.search_auto, name='search_auto'),
                  path('login/', UserViews.login_form, name='login'),
                  path('logout/', UserViews.logout_func, name='logout'),
                  path('signup/', UserViews.signup_form, name='signup'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
