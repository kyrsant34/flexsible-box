from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import InsuredObject, InsuredObjectParameter, InsuredObjectType
from ..serializers import InsuredObjectSerializer, InsuredObjectParameterSerializer, InsuredObjectTypeSerializer


class InsuredObjectViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    queryset = InsuredObject.objects.all()
    serializer_class = InsuredObjectSerializer


class InsuredObjectParameterViewSet(ReadOnlyModelViewSet):
    queryset = InsuredObjectParameter.objects.all()
    serializer_class = InsuredObjectParameterSerializer
    filter_fields = ('code',)


class InsuredObjectTypeViewSet(ReadOnlyModelViewSet):
    queryset = InsuredObjectType.objects.all()
    serializer_class = InsuredObjectTypeSerializer
    filter_fields = ('department', 'insurance_type',)


__all__ = ['InsuredObjectViewSet', 'InsuredObjectParameterViewSet', 'InsuredObjectTypeViewSet']
