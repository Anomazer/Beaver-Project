from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product

def home(request):
    category = Category.objects.all()
    return HttpResponse(render(request, 'index.html', {'categories': category}))

def CategoryProduct_list(request, category_id):
    category = Category.objects.get(id = category_id)
    products = Product.objects.filter(catedory = category)
    return render(request, 'index.html', {'category': category})