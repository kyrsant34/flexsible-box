from rest_framework import serializers

from .models import (AddressType, AttachmentType, CarMark, CarModel, ContactType, CredentialType, InsuranceType,
                     MessageType, PaymentType, InsuranceContractStatus, HandBook)


class HandBookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('code', 'title')


class AddressTypeSerializer(HandBookSerializer):
    class Meta(HandBookSerializer.Meta):
        model = AddressType


class AttachmentTypeSerializer(HandBookSerializer):
    class Meta(HandBookSerializer.Meta):
        model = AttachmentType


class CarMarkSerializer(HandBookSerializer):
    class Meta(HandBookSerializer.Meta):
        model = CarMark
        fields = HandBookSerializer.Meta.fields + ('id',)


class CarModelSerializer(HandBookSerializer):
    class Meta(HandBookSerializer.Meta):
        model = CarModel
        fields = HandBookSerializer.Meta.fields + ('id',)


class ContactTypeSerializer(HandBookSerializer):
    class Meta(HandBookSerializer.Meta):
        model = ContactType


class CredentialTypeSerializer(HandBookSerializer):
    class Meta(HandBookSerializer.Meta):
        model = CredentialType


class InsuranceTypeSerializer(HandBookSerializer):
    class Meta(HandBookSerializer.Meta):
        model = InsuranceType


class MessageTypeSerializer(HandBookSerializer):
    class Meta(HandBookSerializer.Meta):
        model = MessageType


class PaymentTypeSerializer(HandBookSerializer):
    class Meta(HandBookSerializer.Meta):
        model = PaymentType


class InsuranceContractStatusSerializer(HandBookSerializer):
    class Meta(HandBookSerializer.Meta):
        model = InsuranceContractStatus
        fields = HandBookSerializer.Meta.fields + ('availiable_action_types',)


__all__ = ['AddressTypeSerializer', 'AttachmentTypeSerializer', 'CarMarkSerializer', 'CarModelSerializer',
           'ContactTypeSerializer', 'CredentialTypeSerializer', 'InsuranceTypeSerializer', 'MessageTypeSerializer',
           'PaymentTypeSerializer']
