from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Property
from .serializers import PropertiesListSerializers

@api_view(['GET'])
# @authentication_classes([])
@permission_classes([AllowAny])
def properties_list(request):
    properties = Property.objects.all()
    serializer = PropertiesListSerializers(properties, many=True)

    return JsonResponse({
        'data': serializer.data
    })
    
    # return Response({
    #     'data': serializer.data
    # })