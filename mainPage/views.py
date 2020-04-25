from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from item.models import Clothing
from .serializers import MainPageClothingSerializer


@api_view(['GET'])
def main_page(request):
    data = {}
    discounted = Clothing.objects.all().order_by('-discount')[:10]
    discounted_ser = MainPageClothingSerializer(discounted, many=True)
    data['discounted'] = discounted_ser.data
    newest = Clothing.objects.all().order_by('-date_added')[:10]
    newest_ser = MainPageClothingSerializer(newest, many=True)
    data['newest'] = newest_ser.data
    data['shirt'] = 1
    data['pants'] = 2
    data['shoe'] = 3
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def cat_page(request):
    data = {}
    cat_id = request.GET.get('category')
    items = Clothing.objects.filter(kind=cat_id)
    items_ser = MainPageClothingSerializer(items, many=True)
    data['items'] = items_ser.data
    return Response(data, status=status.HTTP_200_OK)
