from rest_framework import serializers

from products.models import Product, ProductCategory, Basket


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=ProductCategory.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category', 'description', 'image', 'quantity')


class BasketSerializer(serializers.ModelSerializer):
    products = ProductSerializer()

    class Meta:
        model = Basket
        fields = ('id', 'product', 'quantity', 'created_at')
        read_only_fields = ('created_at',)
