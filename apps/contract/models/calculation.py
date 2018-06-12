from django.db import models

from apps.common.models import AbstractOperationType, AbstractParameter, AbstractOperation
from apps.handbooks.models import PaymentType

from ..managers import CalculationParametersManager


class CalculationType(AbstractOperationType):
    payment_types = models.ManyToManyField(PaymentType, related_name='calculation_types')


class CalculationParameter(AbstractParameter):
    PARAMETERS_TYPES = {
        **AbstractParameter.PARAMETERS_TYPES,
        'handbooks.CarMark': {
            'display_name': 'Марка авто',
            'serializer_field_name': ''
        },
        'handbooks.CarModel': {
            'display_name': 'Модель авто',
            'serializer_field_name': ''
        },
        'client.InsuredObject': {
            'display_name': 'Объект страхования',
            'serializer_field_name': ''
        },
        'client.Person': {
            'display_name': 'Персона',
            'serializer_field_name': ''
        },
    }

    calculation_types = models.ManyToManyField(CalculationType, related_name='calculation_parameters')

    objects = CalculationParametersManager()


class Calculation(AbstractOperation):
    calculation_type = models.ForeignKey(CalculationType, related_name='calculations')


__all__ = ['CalculationType', 'CalculationParameter', 'Calculation']
