from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def home(request):
    return render(request,'home.html',context=None)

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.order_by('name')
    data = {
        'products':products,
        'categories':categories
    }
    return render(request,'shop.html',context=data)