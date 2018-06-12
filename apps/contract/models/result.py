from django.db import models

from apps.common.models import AbstractOperationType, AbstractParameter, AbstractOperation

from ..managers import ResultParametersManager

from .calculation import Calculation


class ResultType(AbstractOperationType):
    pass


class ResultParameter(AbstractParameter):
    # PARAMETERS_TYPE_CHOICES = AbstractParameter.PARAMETERS_TYPE_CHOICES + (
    #     ('handbooks.CarMark', 'Марка авто'),
    #     ('handbooks.CarModel', 'Модель авто'),
    # )

    result_types = models.ManyToManyField(ResultType, related_name='result_parameters')

    objects = ResultParametersManager()


class Result(AbstractOperation):
    result_type = models.ForeignKey(ResultType, related_name='results')
    calculation = models.ForeignKey(Calculation, related_name='results')


__all__ = ['ResultType', 'ResultParameter', 'Result']
