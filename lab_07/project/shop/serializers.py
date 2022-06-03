# -*- coding: utf-8 -*-

from shop.models import Category, Product, Profile
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "category"]

class ProfileSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)
    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name", "age", "products"]