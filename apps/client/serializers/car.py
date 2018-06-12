from rest_framework import serializers

from apps.client.serializers.common import CredentialSerializer
from apps.common.serializers import NestedModelSerializer
from apps.client.models import Car


class CarSerializer(NestedModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    credential = CredentialSerializer(many=True)

    class Meta:
        model = Car
        fields = ('id', 'car_mark', 'car_model', 'credential', 'engine_power', 'engine_power_kilowatt',
                  'manufacturing_date', 'mileage', 'number_plate', 'vin_number', 'creator')
