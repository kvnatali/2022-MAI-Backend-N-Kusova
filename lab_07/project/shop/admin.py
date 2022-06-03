from django.contrib import admin

# Register your models here.

from shop.models import Profile, Product, Category
from django.contrib.admin import AdminSite

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_filter = ('first_name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Profile)
admin_site.register(Product)
admin_site.register(Category)

#@admin.register(Profile)
#class ProfileAdmin(admin.ModelAdmin):
#pass