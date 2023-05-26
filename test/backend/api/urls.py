from django.urls import path, include
from rest_framework import routers

from products.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet) # "products": "http://localhost:8000/api/products/"


urlpatterns = [
    # path('', views.api_home),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
