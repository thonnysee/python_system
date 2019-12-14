from django.contrib.auth import get_user_model
from rest_framework import generics, authentication, permissions
from api.serializers import UserSerializer, ProductSerializer
from shop.models import Product
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from django.http import Http404


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
        print(self)
        return super().get_queryset()

    def get(self, request, format=None):
        if (request.query_params and request.query_params['id']):
            product = Product.objects.get(pk=request.query_params['id'])
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        print(lookup_url_kwarg)
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        return get_object_or_404(queryset, **filter_kwargs)
