from django.conf import settings
from django.conf.urls import url

from apps.client.views import (CarViewSet, InsuredObjectViewSet, InsuredObjectParameterViewSet, InsuredObjectTypeViewSet,
                          LegalPersonViewSet, NaturalPersonViewSet)


urlpatterns = [

    # NaturalPerson
    url(
        r'natural_persons/?$',
        NaturalPersonViewSet.as_view({'get': 'list', 'post': 'create'})
    ),

    # NaturalPerson
    url(
        r'legal_persons/?$',
        LegalPersonViewSet.as_view({'get': 'list', 'post': 'create'})
    ),

    # Car
    url(
        r'cars/?$',
        CarViewSet.as_view({'get': 'list', 'post': 'create'})
    ),

    # InsuredObject
    url(
        r'insured_objects/?$',
        InsuredObjectViewSet.as_view({'get': 'list', 'post': 'create'})
    ),
    url(
        r'insured_objects/{}/?$'.format(settings.PK_NUM_PATTERN),
        InsuredObjectViewSet.as_view({'get': 'retrieve'})
    ),

    # InsuredObjectParameter
    url(
        r'insured_object_parameters/?$',
        InsuredObjectParameterViewSet.as_view({'get': 'list'})
    ),
    url(
        r'insured_object_parameters/{}/?$'.format(settings.PK_CODE_PATTERN),
        InsuredObjectParameterViewSet.as_view({'get': 'retrieve'})
    ),

    # InsuredObjectType
    url(
        r'insured_object_types/?$',
        InsuredObjectTypeViewSet.as_view({'get': 'list'})
    ),
    url(
        r'insured_object_types/{}/?$'.format(settings.PK_CODE_PATTERN),
        InsuredObjectTypeViewSet.as_view({'get': 'retrieve'})
    ),
]
