from django.db import models


class HandBook(models.Model):
    title = models.CharField(max_length=250)
    code = models.CharField(max_length=250, primary_key=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class InsuranceType(HandBook):
    pass


class PaymentType(HandBook):
    pass


class CarMark(models.Model):
    title = models.CharField(max_length=250)
    code = models.CharField(max_length=250, null=True, blank=True)


class CarModel(models.Model):
    title = models.CharField(max_length=250)
    code = models.CharField(max_length=250, null=True, blank=True)
    car_mark = models.ForeignKey(CarMark)


class MessageType(HandBook):
    pass


class AttachmentType(HandBook):
    pass


class AddressType(HandBook):
    pass


class ContactType(HandBook):
    pass


class CredentialType(HandBook):
    pass


class InsuranceContractStatus(HandBook):
    class Code:
        DRAFT = 'DRAFT'
        SAVED = 'SAVED'
        RSA_VERIFIED = 'RSA_VERIFIED'
        PAYED = 'PAYED'

    availiable_action_types = models.ManyToManyField('contract.ActionType', blank=True,
                                                     related_name='availiable_insurance_statuses')


__all__ = ['AddressType', 'AttachmentType', 'CarMark', 'CarModel', 'ContactType', 'CredentialType', 'InsuranceType',
           'MessageType', 'PaymentType', 'InsuranceContractStatus']
