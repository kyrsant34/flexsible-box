from django.db import models
from django.contrib.postgres import fields

from apps.handbooks.models import HandBook
from .mixins import ChangesTrackingMixin


class AbstractParameterManager(models.Manager):

    def all_active(self, **kwargs):
        return self.filter(is_active=True, **kwargs)

    def all_required(self, **kwargs):
        return self.filter(is_required=True, **kwargs)


class AbstractParameter(HandBook):
    PARAMETERS_TYPES = {
        'int': {
            'display_name': 'Целое число',
            'serializer_field_name': 'IntegerField'
        },
        'float': {
           'display_name': 'Десятичное число',
           'serializer_field_name': 'FloatField'
        },
        'string': {
           'display_name': 'Строка',
           'serializer_field_name': 'CharField'
        },
        'json': {
           'display_name': 'JSON',
           'serializer_field_name': 'JSONField'
        },
        'date': {
           'display_name': 'Дата',
           'serializer_field_name': 'DateField'
        },
        'bool': {
            'display_name': 'Логический',
            'serializer_field_name': 'NullBooleanField'
        },
    }

    param_type = models.CharField(max_length=255)
    is_required = models.NullBooleanField(default=True)
    is_active = models.NullBooleanField(default=True)
    is_many = models.NullBooleanField(default=False)

    class Meta:
        abstract = True
        unique_together = ('code',)

    @classmethod
    def choices(cls):
        choices = []
        for param_type in cls.PARAMETERS_TYPES:
            choices.append((param_type, cls._meta.model.PARAMETERS_TYPES[param_type]['display_name']))
        return tuple(choices)


class AbstractOperationType(HandBook):
    department = models.ForeignKey('account.Department')
    insurance_type = models.ForeignKey('handbooks.InsuranceType')

    class Meta:
        abstract = True
        unique_together = ('department', 'insurance_type', 'code',)

    def __str__(self):
        return f'{self.title} {self.department} {self.insurance_type}'


class AbstractOperation(ChangesTrackingMixin):
    parameters = fields.JSONField()

    class Meta:
        abstract = True
