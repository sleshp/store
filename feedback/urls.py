from django.urls import path, include
from rest_framework import routers
from feedback.views import feedback_view, FeedbackModelViewSet, ReferenceMaterialList
app_name = 'feedback'

router = routers.DefaultRouter()
router.register(r'feedback-list', FeedbackModelViewSet)

urlpatterns = [
    path('', feedback_view, name='feedback'),
    path('', include(router.urls)),
    path('referencematerials/', ReferenceMaterialList.as_view(), name='referencematerial-list'),

]
