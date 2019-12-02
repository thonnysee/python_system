from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('user/create/', views.UserRegistrationView.as_view(),
         name='user.create'),
    path('user/me/', views.ManageUserView.as_view(), name='user.me'),
    path('shop/product/list', views.ProductListView.as_view(),
         name='shop.product.list'),
]
