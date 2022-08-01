from django.urls import path, include
from rest_framework import routers

from .import views
from products.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)


urlpatterns = [
    # path('', views.api_home),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
