from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from products.views import IndexView
from store import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
    path('feedback/', include('feedback.urls')),
    path('api/', include('api.urls', namespace='api')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
