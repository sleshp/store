from django.urls import path, include

from rest_framework import routers

from api.views import ProductModelViewSet, BaskerModelViewSet
app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', ProductModelViewSet)
router.register(r'baskets', BaskerModelViewSet)
urlpatterns = [
    path('', include(router.urls)),

]
