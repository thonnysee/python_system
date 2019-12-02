from django.contrib.auth import get_user_model
from rest_framework import generics, authentication, permissions
from api.serializers import UserSerializer, ProductSerializer
from shop.models import Product
from rest_framework.response import Response
from django.http import Http404


from rest_auth.registration.views import RegisterView


class UserRegistrationView(RegisterView):
    queryset = get_user_model().objects.all()

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
    
class ProductListView(generics.GenericAPIView):
    queryset = Product.objects.all
    
    def get_queryset(self):
        return super().get_queryset()
    
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def get_object(self, pk):
        return Product.objects.get(pk=pk)