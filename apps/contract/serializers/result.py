from rest_framework import serializers

from apps.common.validators import ParametersValidator
from ..models import ResultParameter, ResultType, Result


class ResultParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultParameter
        fields = ('result_types', 'param_type', 'is_active', 'is_required', 'code', 'title',)


class ResultTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultType
        fields = ('department', 'insurance_type', 'code', 'title',)


class ResultSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Result
        fields = ('id', 'result_type', 'calculation', 'parameters', 'created', 'creator')
        validators = [
            ParametersValidator(operation_model_type_field='result_type', parameter_model=ResultParameter)
        ]