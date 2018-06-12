from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.mixins import CreateModelMixin

from ..models import LegalPerson, NaturalPerson
from ..serializers import LegalPersonSerializer, NaturalPersonSerializer


class NaturalPersonViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    queryset = NaturalPerson.objects.all()
    serializer_class = NaturalPersonSerializer


class LegalPersonViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer


__all__ = ['LegalPersonViewSet', 'NaturalPersonViewSet']
