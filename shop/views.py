from django.shortcuts import render
from .models import Product, Category
from django.views.generic.list import ListView

# Create your views here.
def home(request):
    return render(request,'home.html',context=None)

class ProductsListView(ListView):
    template_name = 'shop.html'
    model = Product
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

