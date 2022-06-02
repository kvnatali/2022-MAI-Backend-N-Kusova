from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.shop_profile, name='profile'),
    path('products_list', views.products_list, name='products_list'),
    path('categories', views.categories, name='categories'),
    path('category/<int:id_category>/', views.category, name='category'),
    path('api/categories', views.categories, name='categories'),
    path('admin/', admin.site.urls),

    path('allCategories', views.all_categories, name='all_categories'),
    path('addCategory', views.add_category, name='add_category'),

    path('allProducts', views.all_products, name='all_categories'),
    path('getProduct', views.find_product, name='add_category'),
]