from rest_framework import serializers

from apps.common.serializers import NestedModelSerializer

from ..models import NaturalPerson, LegalPerson, Person
from .common import ContactSerializer, QueryAddressSerializer, CredentialSerializer


class NaturalPersonSerializer(NestedModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    contact = ContactSerializer(many=True)
    address = QueryAddressSerializer(many=True)
    credential = CredentialSerializer(many=True)
    person = serializers.PrimaryKeyRelatedField(required=False, queryset=Person.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for param in ['contact', 'address', 'credential']:
            param_required = kwargs.pop("is_{}_required".format(param), True)
            if not param_required:
                self.fields[param].required = False

    class Meta:
        model = NaturalPerson
        fields = ('id', 'first_name', 'last_name', 'patronymic', 'gender', 'birth_date', 'contact', 'address',
                  'credential', 'person', 'creator')


class LegalPersonSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = LegalPerson
        fields = ('id', 'title', 'creator')


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('id', 'natural_person', 'legal_person')


__all__ = ['LegalPersonSerializer', 'NaturalPersonSerializer', 'PersonSerializer']
