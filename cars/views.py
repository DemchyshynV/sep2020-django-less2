from rest_framework.generics import ListAPIView

from .models import CarModel
from .serializers import CarSerializer


class CarsListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
