from django.shortcuts import render
from .models import Product, Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
def home(request):
    return render(request, 'home.html', context=None)


class ProductsListView(ListView):
    """
    Display the Models Products with Categories
    :model:`shop.Product`, :model:`shop.Category`.

    **Context**

    ``products``
        An instance of :model:`shop.Product`.

    ``categories``
        An instance of :model:`shop.Category`.

    **Template:**

    :template:`shop.html`
    """
    template_name = 'shop/list.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('name')
        return context


class ProductDetailView(DetailView):
    model = model = Product
    template_name = "shop/item.html"
    context_object_name = 'product'
