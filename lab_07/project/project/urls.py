"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from shop.admin import admin_site
from shop import views

from shop.views import ProfileViewSet, ProductViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("shop/api/profile", ProfileViewSet, basename="profiles")
router.register("api/profile", ProfileViewSet, basename="profiles")

router.register("shop/api/product", ProductViewSet, basename="products")
router.register("api/product", ProductViewSet, basename="products")

router.register("shop/api/category", CategoryViewSet, basename="categories")
router.register("api/category", CategoryViewSet, basename="categories")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/admin/', admin.site.urls),

    path('shop/', include('shop.urls')),
    path('', include('shop.urls')),

    path('myadmin/', admin_site.urls),
]

urlpatterns += router.urls