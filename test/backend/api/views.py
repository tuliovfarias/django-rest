import json
# from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kawargs):
    instance = Product.objects.all()
    data = {}
    if instance:
        data = ProductSerializer(instance).data

    # body = request.body
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type


    # return JsonResponse(data)
    return Response(data)