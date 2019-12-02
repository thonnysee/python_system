from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from shop.models import Product


class UserRegistrationSerializer(RegisterSerializer):

    username = None
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        super(UserRegistrationSerializer, self).get_cleaned_data()

        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'summary',
            'description',
            'sku',
            'price',
            'special_price',
            'product_type',
            'slug',
            'stock',
            'category',
            'url',
            'is_active'
            )

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        product = super().update(instance, validated_data)
        return product


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'email',
            'password',
            'firstname',
            'lastname',
            'second_lastname',
            'birthday',
            'telephone',
            'mobile'
            )
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5},
            'id': {'read_only': True}
            }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user')
