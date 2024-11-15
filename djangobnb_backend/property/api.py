import logging
from django.http import JsonResponse
# from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import PropertyForm
from .models import Property, Reservation
from .serializers import PropertiesListSerializer, PropertiesDetailSerializers, ReservationsListSerializer

logger = logging.getLogger(__name__)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_list(request):
    try:
        properties = Property.objects.all()
        serializer = PropertiesListSerializer(properties, many=True)
        return JsonResponse({'data': serializer.data})
    except Property.DoesNotExist:
        logger.error(f"Property not found.")
        return JsonResponse({'error': 'Property not found'}, status=404)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def property_reservations(request, pk):
    property = Property.objects.get(pk=pk)
    reservations = property.reservations.all()

    serializer = ReservationsListSerializer(reservations, many=True)
    return JsonResponse(serializer.data, safe=False)

    # try:
    #     property = Property.objects.get(pk=pk)
    #     reservations = property.reservations.all()
        
    #     serializer = ReservationsListSerializer(reservations, many=True)
    #     return JsonResponse(serializer.data, safe=False)
    # except Property.DoesNotExist:
    #     logger.error(f"Property with ID {pk} not found.")
    #     return JsonResponse({'error': 'Property not found'}, status=404)
    # except Exception as e:
    #     logger.error(f"An unexpected error occurred: {e}")
    #     return JsonResponse({'error': str(e)}, status=500)



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_detail(request, pk):
    property = Property.objects.get(pk=pk)
    
    serializer = PropertiesDetailSerializers(property, many=False)

    return JsonResponse(serializer.data)


@api_view(['POST', 'FILES'])
def create_property(request):
    form = PropertyForm(request.POST, request.FILES)

    if form.is_valid():
        property = form.save(commit=False)
        property.landlord = request.user
        property.save()
        
        return JsonResponse({'success': True})
    else:
        print('error', form.errors, form.non_field_errors)
        return JsonResponse({'errors': form.errors.as_json()}, status=400)


@api_view(['POST'])
def book_property(request, pk):
    try:
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        number_of_nights = request.POST.get('number_of_nights', '')
        total_price = request.POST.get('total_price', '')
        guests = request.POST.get('guests', '')
        
        property = Property.objects.get(pk=pk)
        
        Reservation.objects.create(
            property = property,
            start_date = start_date,
            end_date = end_date,
            number_of_nights = number_of_nights,
            total_price = total_price,
            guests = guests,
            created_by = request.user
        )
        
        return JsonResponse({'success': True});
    except Exception as e:
        print('Error', e)
        
    return JsonResponse({'success': False})