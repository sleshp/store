from rest_framework.viewsets import ModelViewSet
from products.models import Product, Basket
from products.serializers import ProductSerializer, BasketSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BaskerModelViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
