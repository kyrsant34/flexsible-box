from rest_framework import serializers

from apps.common.validators import ParametersValidator
from ..models import CalculationParameter, CalculationType, Calculation


class CalculationParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculationParameter
        fields = ('calculation_types', 'param_type', 'is_required', 'is_active', 'code', 'title')


class CalculationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculationType
        fields = ('payment_types', 'department', 'insurance_type', 'code', 'title',)


class CalculationSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Calculation
        fields = ('id', 'calculation_type', 'parameters', 'created', 'creator')
        validators = [
            ParametersValidator(operation_model_type_field='calculation_type', parameter_model=CalculationParameter)
        ]