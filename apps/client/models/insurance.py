from django.db import models

from apps.common.models import AbstractOperationType, AbstractParameter, AbstractOperation
from .person import Person
from ..managers import InsuredObjectParameterManager


class InsuredObjectType(AbstractOperationType):
    pass


class InsuredObjectParameter(AbstractParameter):
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
        'client.NaturalPerson': {
            'display_name': 'Физическое лицо',
            'serializer_field_name': ''
        },
        'client.Person': {
            'display_name': 'Персона',
            'serializer_field_name': ''
        },
    }

    insured_object_types = models.ManyToManyField(InsuredObjectType)

    objects = InsuredObjectParameterManager()


class InsuredObject(AbstractOperation):
    insured_object_type = models.ForeignKey(InsuredObjectType)
    insurant = models.ForeignKey(Person)


__all__ = ['InsuredObject', 'InsuredObjectParameter', 'InsuredObjectType']
