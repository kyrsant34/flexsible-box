from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.mixins import CreateModelMixin

from ..models import Car
from ..serializers import CarSerializer


class CarViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
