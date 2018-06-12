from dadata.client import SUCCESS
from dadata.plugins import DjangoDaDataClient
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from ..models import Contact, Address, Credential


class ContactSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Contact
        fields = ('id', 'contact_type', 'data', 'creator')


class AddressSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Address
        fields = ('id', 'address_type', 'country', 'city', 'street', 'house', 'flat', 'kladr', 'creator')


class QueryAddressSerializer(AddressSerializer):

    default_error_messages = {
        'no_query': _('No query specified for address.'),
        'dadata': _('Failed connect to dadata service. Error code: {e_code}.'),
        'dadata_resp': _('Failed to parse response from dadata service. Error code: {e_code}.'),
    }

    dadata_mapping = {
        'country': 'country',
        'city': 'city',
        'street': 'street',
        'house': 'house',
        'flat': 'flat',
        'kladr': 'kladr_id',
    }

    def to_internal_value(self, data):
        query = data.pop('query', '')
        if query:
            dadata_client = DjangoDaDataClient()
            dadata_client.suggest_address = query
            try:
                result_code = dadata_client.suggestions.address.request()
                if result_code != SUCCESS:
                    self.fail('dadata', e_code=result_code)
                response_data = dadata_client.result.suggestions[0].get('data')
            except (KeyError, AttributeError) as e:
                # Поднимаем исключение наверх, если не удалось обработать результат
                # Код ошибки == класс исключения
                self.fail('dadata_resp', e_code=type(e).__name__)
            for target_key, response_key in self.dadata_mapping.items():
                data[target_key] = response_data[response_key]
        else:
            self.fail('no_query')
        return super(QueryAddressSerializer, self).to_internal_value(data)


class CredentialSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Credential
        fields = ('id', 'number', 'series', 'credential_type', 'issue_point', 'issue_date', 'expiration_date',
                  'creator')


__all__ = ['ContactSerializer', 'AddressSerializer', 'QueryAddressSerializer', 'CredentialSerializer']
