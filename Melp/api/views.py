from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantList(generics.ListCreateAPIView):
    """View for Listinig Restaurants in API"""

    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for Detail Restaurant API Endpoints"""

    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

@csrf_exempt
def get_nearby_restaurants_count(request):
    """View for retrieving nerby restaurants given a radious"""

    try:
        latitude = request.GET.get('latitude', None)
        longitude = request.GET.get('longitude', None)
        radious = request.GET.get('radius', None)

        data = {}
        return JsonResponse(data, status=200)


    except Exception:

        data["message"] = "Hubo un error en el request"
        return JsonResponse(data, status=400)


