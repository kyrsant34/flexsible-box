from rest_framework import serializers

from ..models import InsuranceContract


class InsuranceContractSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = InsuranceContract
        fields = '__all__'
        read_only_fields = ('insurance_contract_status',)
