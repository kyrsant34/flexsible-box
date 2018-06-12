from factory import DjangoModelFactory, Sequence

from apps.handbooks.models import HandBook, CredentialType, InsuranceType, PaymentType, CarMark


class HandBookFactory(DjangoModelFactory):
    class Meta:
        model = HandBook

    code = Sequence("CODE_{}".format)
    title = Sequence("TITLE_{}".format)


class CredentialTypeFactory(HandBookFactory):
    class Meta:
        model = CredentialType


class InsuranceTypeFactory(HandBookFactory):
    class Meta:
        model = InsuranceType


class PaymentTypeFactory(HandBookFactory):
    class Meta:
        model = PaymentType


class CarMarkFactory(HandBookFactory):
    class Meta:
        model = CarMark
