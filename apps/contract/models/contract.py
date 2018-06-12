from django.db import models

from apps.common.models import ChangesTrackingMixin


class InsuranceContract(ChangesTrackingMixin):

    result = models.ForeignKey('contract.Result', related_name='insurance_contracts')
    insurance_contract_status = models.ForeignKey('handbooks.InsuranceContractStatus', related_name='insurance_contracts')
    # insured_object = models.ForeignKey('client.InsuredObject')


__all__ = ['InsuranceContract',]
