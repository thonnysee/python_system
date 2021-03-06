"""python_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from shop.admin import admin_site
from shop import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Shop API Endpoints')

urlpatterns = [
    path('admin/shop/doc/', include('django.contrib.admindocs.urls')),
    path('', views.HomeListView.as_view(), name='home'),
    path('products/', views.ProductsListView.as_view(), name='products_list'),
    path('products/<slug:slug>/',
         views.ProductDetailView.as_view(), name='product_detail'),
    path('admin/shop/', admin_site.urls),
    path('api/', include('api.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/endpoints/', schema_view),
]
