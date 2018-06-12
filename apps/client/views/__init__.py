from .car import CarViewSet
from .insurance import InsuredObjectViewSet, InsuredObjectParameterViewSet, InsuredObjectTypeViewSet
from .person import LegalPersonViewSet, NaturalPersonViewSet


__all__ = ['CarViewSet', 'InsuredObjectViewSet', 'InsuredObjectParameterViewSet', 'InsuredObjectTypeViewSet',
           'LegalPersonViewSet', 'NaturalPersonViewSet']
