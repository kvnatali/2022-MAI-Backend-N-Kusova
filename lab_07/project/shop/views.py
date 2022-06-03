from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from shop.models import Category, Product, Profile
from django.views.decorators.csrf import csrf_exempt

from shop.serializers  import CategorySerializer, ProductSerializer, ProfileSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response

from shop.forms import CategoryForm

import datetime

@require_http_methods(["GET", "POST"])

def index(request):
   return render(request, "index.html", context={"data" : datetime.datetime.now()})

class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        
        if serializer.is_valid():
            category = Category()
            category.title = serializer.validated_data["title"]
            category.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = Category.objects.all() # помним про lazy-логику
        
        category = None
        try:
            category = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class ProfileViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProfileSerializer(data=request.data)
        
        if serializer.is_valid():
            profile = Profile()
            profile.first_name = serializer.validated_data["first_name"]
            profile.last_name = serializer.validated_data["last_name"]
            profile.age = serializer.validated_data["age"]
            profile.products = serializer.validated_data["products"]
            profile.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = Profile.objects.all() # помним про lazy-логику
        
        profile = None
        try:
            profile = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            product = Product()
            product.title = serializer.validated_data["title"]
            product.description = serializer.validated_data["description"]
            product.price = serializer.validated_data["price"]
            product.category = serializer.validated_data["category"]
            product.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = Product.objects.all() # помним про lazy-логику
        
        product = None
        try:
            product = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = ProductSerializer(product)
        return Response(serializer.data)


def add_category2(request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return JsonResponse({
                'msg': 'Категория сохранена',
                'id': category.id
            })
        return JsonResponse({'errors': form.errors}, status=400)


def shop_profile(request):
	return JsonResponse({'Заглушка' : 'Заглушка профиля.'})

def products_list(request):
	return JsonResponse({'Заглушка' : 'Заглушка для списка продуктов!'})

def categories(request):
	return JsonResponse({'Заглушка' : 'Заглушка для страницы категорий!'})
	
def category(request, id_category):
	response = {'Заглушка' : 'Заглушка для категории №%s' % id_category} 
	return JsonResponse(response)

def all_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return JsonResponse({
            'Category': list(categories.values())
        })

@csrf_exempt 
def add_category(request):
    if request.method == 'GET':
        return JsonResponse({"status": False, "msg": "Нужен POST запрос"})

    if request.method == 'POST':
        name = request.GET.get("category_name", None)
        if not name:
            return JsonResponse({"status": False, "msg": "Укажите имя категории"})

        duplicates = Category.objects.filter(title=name)
        if len(duplicates) > 0:
            return JsonResponse({"status": False, "msg": "Уже есть такой"})
            
        new_category = Category()
        new_category.title = name
        new_category.save()
        
        return JsonResponse({"status": True, "msg": "Категория добавлена"})

def all_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return JsonResponse({
            'Product': list(products.values())
        })

def find_product(request):
    if request.method == 'GET':

        product_name = request.GET.get("product_name", None)
        if not product_name:
            return JsonResponse({"status": False, "msg": "Укажите название продукта"})
        product = Product.objects.filter(title=product_name).values()
        return JsonResponse({
            'Product': list(product.values())
        })