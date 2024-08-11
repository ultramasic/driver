from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RawData
from .serializers import RawDataSerializer
from trucks.models import Truck
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class RawDataView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            truck = Truck.objects.get(vin=request.data.get('vin'))
        except Truck.DoesNotExist:
            return Response({"error": "Truck not found"}, status=status.HTTP_404_NOT_FOUND)

        raw_data = {
            "truck": truck.id,
            "data": request.data
        }
        serializer = RawDataSerializer(data=raw_data)
        if serializer.is_valid():
            serializer.save()
            process_data(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def process_data(data):
    truck = Truck.objects.get(id=data['truck'])
    raw_data = data['data']
    
    truck.last_trip = raw_data.get('last_trip')
    truck.obdii_fault_codes = raw_data.get('obdii_fault_codes')
    truck.fuel_level = raw_data.get('fuel_level')
    truck.status = raw_data.get('status')
    truck.speed = raw_data.get('speed')
    truck.rpm = raw_data.get('rpm')
    truck.engine_temperature = raw_data.get('engine_temperature')
    truck.engine_load = raw_data.get('engine_load')
    truck.live_fuel_usage = raw_data.get('live_fuel_usage')
    truck.latitude = raw_data.get('lat')
    truck.longitude = raw_data.get('lon')
    truck.gps_data = raw_data.get('gps')
    truck.save()

    if truck.driver:
        driver = truck.driver
        driver.last_trip = truck.last_trip
        driver.last_position = truck.gps_data
        driver.save()

    if truck.asset:
        asset = truck.asset
        asset.gps_data = truck.gps_data
        asset.save()

@csrf_exempt
def data_ingestion_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            vin = data.get('vin')
            try:
                truck = Truck.objects.get(vin=vin)
            except Truck.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Truck not found'})

            raw_data = {
                "truck": truck.id,
                "data": data
            }
            serializer = RawDataSerializer(data=raw_data)
            if serializer.is_valid():
                serializer.save()
                process_data(serializer.data)
                return JsonResponse({'status': 'success', 'data': serializer.data})
            return JsonResponse({'status': 'error', 'message': serializer.errors})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
