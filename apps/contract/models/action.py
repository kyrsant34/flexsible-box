from django.db import models

from apps.common.models import AbstractOperationType, AbstractParameter, AbstractOperation

from ..managers import ActionParametersManager


class ActionType(AbstractOperationType):
    successfull_contract_status = models.ForeignKey('handbooks.InsuranceContractStatus',
                                                     related_name='successfull_action_types')
    fail_contract_status = models.ForeignKey('handbooks.InsuranceContractStatus', null=True, blank=True,
                                              related_name='fail_action_types')


class ActionParameter(AbstractParameter):
    PARAMETERS_TYPE_CHOICES = AbstractParameter.PARAMETERS_TYPE_CHOICES + (
        ('handbooks.CarMark', 'Марка авто'),
        ('handbooks.CarModel', 'Модель авто'),
    )
    action_types = models.ManyToManyField(ActionType, related_name='action_parameters')

    objects = ActionParametersManager()


class Action(AbstractOperation):
    insurance_contract = models.ForeignKey('contract.InsuranceContract', related_name='actions')
    action_type = models.ForeignKey(ActionType, related_name='actions')

    class Meta:
        unique_together = ('action_type', 'insurance_contract')

__all__ = ['ActionType', 'ActionParameter', 'Action']
