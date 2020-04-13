from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Clothing
from .serializers import ClothingSerializer


@api_view(['POST', ])
def item_view(request):
    data = {}
    item_id = request.POST.get('item_id')
    try:
        clothing = Clothing.objects.get(id=item_id)
        clothing_ser = ClothingSerializer(clothing)
        return Response(data=clothing_ser.data, status=status.HTTP_200_OK)
    except Clothing.DoesNotExist:
        data['response'] = 'Error'
        data['Error message'] = 'No Clothing with this id'
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)