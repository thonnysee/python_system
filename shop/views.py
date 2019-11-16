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
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['categories'] = Category.objects.all()
        print(context)
        return context

