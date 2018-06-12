from rest_framework.generics import ListAPIView


from .models import (AddressType, AttachmentType, CarMark, CarModel, ContactType, CredentialType, InsuranceType,
                     MessageType, PaymentType, InsuranceContractStatus)
from .serializers import (AddressTypeSerializer, AttachmentTypeSerializer, CarMarkSerializer, CarModelSerializer,
                          ContactTypeSerializer, CredentialTypeSerializer, InsuranceTypeSerializer,
                          MessageTypeSerializer, PaymentTypeSerializer, InsuranceContractStatusSerializer)


class HandBookList(ListAPIView):
    filter_fields = ('code', 'title')

class AddressTypesList(HandBookList):
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeSerializer


class AttachmentTypesList(HandBookList):
    queryset = AttachmentType.objects.all()
    serializer_class = AttachmentTypeSerializer


class CarMarksList(HandBookList):
    queryset = CarMark.objects.all()
    serializer_class = CarMarkSerializer


class CarModelsList(HandBookList):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    filter_fields = HandBookList.filter_fields + ('car_mark',)


class ContactTypesList(HandBookList):
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer


class CredentialTypesList(HandBookList):
    queryset = CredentialType.objects.all()
    serializer_class = CredentialTypeSerializer


class InsuranceTypesList(HandBookList):
    queryset = InsuranceType.objects.all()
    serializer_class = InsuranceTypeSerializer


class MessageTypesList(HandBookList):
    queryset = MessageType.objects.all()
    serializer_class = MessageTypeSerializer


class PaymentTypesList(HandBookList):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class InsuranceContractStatusList(HandBookList):
    queryset = InsuranceContractStatus.objects.all()
    serializer_class = InsuranceContractStatusSerializer

__all__ = ['AddressTypesList', 'AttachmentTypesList', 'CarMarksList', 'CarModelsList', 'ContactTypesList',
           'CredentialTypesList', 'InsuranceTypesList', 'MessageTypesList', 'PaymentTypesList',
           'InsuranceContractStatusList']
