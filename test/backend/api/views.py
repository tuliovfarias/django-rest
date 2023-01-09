from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def api_home(request, *args, **kawargs):
    if request.method == 'GET':
        instance = Product.objects.all().order_by("?").first()
        data = {}
        if instance:
            data = ProductSerializer(instance).data
            return Response(data)
    else:
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            return Response(serializer.data)