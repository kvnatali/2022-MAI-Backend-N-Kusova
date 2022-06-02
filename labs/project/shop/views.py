from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from shop.models import Category, Product
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(["GET", "POST"])

def index(request):
	return JsonResponse({'Заглушка' : 'Привет! Это интернет магазинчик'})

def shop_profile(request):
	return JsonResponse({'Заглушка' : 'Заглушка для профиля!'})

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