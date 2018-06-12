from rest_framework import mixins, viewsets

from ..models import CalculationParameter, CalculationType, Calculation
from ..serializers import CalculationParameterSerializer, CalculationTypeSerializer, CalculationSerializer


class CalculationParametersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CalculationParameter.objects.all()
    serializer_class = CalculationParameterSerializer
    filter_fields = ('code',)


class CalculationTypesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CalculationType.objects.all()
    serializer_class = CalculationTypeSerializer
    filter_fields = ('department', 'insurance_type',)


class CalculationsViewSet(mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer
