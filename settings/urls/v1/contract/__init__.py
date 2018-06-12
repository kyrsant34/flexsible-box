from django.conf import settings
from django.conf.urls import url

from apps.contract.views import (CalculationParametersViewSet, CalculationTypesViewSet, CalculationsViewSet,
                             ResultParametersViewSet, ResultViewSet, ResultTypeViewSet,
                             InsuranceContractsViewSet,
                             ActionParametersViewSet, ActionTypesViewSet, ActionsViewSet)


urlpatterns = [

    # CalculationType
    url(
        r'calculation_types/?$',
        CalculationTypesViewSet.as_view({'get': 'list'})
    ),
    url(
        r'calculation_types/{}/?$'.format(settings.PK_CODE_PATTERN),
        CalculationTypesViewSet.as_view({'get': 'retrieve'})
    ),

    # CalculationParameter
    url(
        r'calculation_parameters/?$',
        CalculationParametersViewSet.as_view({'get': 'list'})
    ),
    url(
        r'calculation_parameters/{}/?$'.format(settings.PK_CODE_PATTERN),
        CalculationParametersViewSet.as_view({'get': 'retrieve'})
    ),

    # Calculation
    url(
        r'calculations/?$',
        CalculationsViewSet.as_view({'get': 'list', 'post': 'create'})
    ),
    url(
        r'calculations/{}/?$'.format(settings.PK_NUM_PATTERN),
        CalculationsViewSet.as_view({'get': 'retrieve'})
    ),

    # ResultType
    url(
        r'result_types/?$',
        ResultTypeViewSet.as_view({'get': 'list'})
    ),
    url(
        r'result_types/{}/?$'.format(settings.PK_CODE_PATTERN),
        ResultTypeViewSet.as_view({'get': 'retrieve'})
    ),

    # ResultParameters
    url(
        r'result_parameters/?$',
        ResultParametersViewSet.as_view({'get': 'list'})
    ),
    url(
        r'result_parameters/{}/?$'.format(settings.PK_CODE_PATTERN),
        ResultParametersViewSet.as_view({'get': 'retrieve'})
    ),

    # Results
    url(
        r'results/?$',
        ResultViewSet.as_view({'get': 'list', 'post': 'create'})
    ),
    url(
        r'results/{}/?$'.format(settings.PK_NUM_PATTERN),
        ResultViewSet.as_view({'get': 'retrieve'})
    ),

    # ActionType
    url(
        r'action_types/?$',
        ActionTypesViewSet.as_view({'get': 'list'})
    ),
    url(
        r'action_types/{}/?$'.format(settings.PK_CODE_PATTERN),
        ActionTypesViewSet.as_view({'get': 'retrieve'})
    ),

    # ActionParameters
    url(
        r'action_parameters/?$',
        ActionParametersViewSet.as_view({'get': 'list'})
    ),
    url(
        rf'action_parameters/{settings.PK_CODE_PATTERN}/?$',
        ActionParametersViewSet.as_view({'get': 'retrieve'})
    ),

    # InsuranceContracts
    url(
        r'insurance_contracts/?$',
        InsuranceContractsViewSet.as_view({'get': 'list', 'post': 'create'})
    ),
    url(
        rf'insurance_contracts/{settings.PK_NUM_PATTERN}/?$',
        InsuranceContractsViewSet.as_view({'get': 'retrieve'})
    ),

    # Actions
    url(
        r'insurance_contracts/(?P<insurance_contract>[\d]+)/actions/?$',
        ActionsViewSet.as_view({'get': 'list', 'post': 'create'})
    ),
    url(
        rf'insurance_contracts/(?P<insurance_contract>[\d]+)/actions/{settings.PK_CODE_PATTERN}/?$',
        ActionsViewSet.as_view({'get': 'retrieve'})
    ),
]
