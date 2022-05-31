from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

from django.views.decorators.http import require_http_methods

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