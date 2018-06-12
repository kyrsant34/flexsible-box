from rest_framework import serializers

from apps.common.serializers import NestedModelSerializer
from apps.common.validators import ParametersValidator

from .person import PersonSerializer
from ..models import InsuredObject, InsuredObjectParameter, InsuredObjectType


class InsuredObjectSerializer(NestedModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    insurant = PersonSerializer()

    class Meta:
        model = InsuredObject
        fields = ('id', 'insured_object_type', 'insurant', 'parameters', 'creator')
        validators = [
            ParametersValidator(operation_model_type_field='insured_object_type', parameter_model=InsuredObjectParameter)
        ]


class InsuredObjectTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuredObjectType
        fields = ('department', 'insurance_type', 'code', 'title',)


class InsuredObjectParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuredObjectParameter
        fields = ('insured_object_type', 'param_type', 'is_active', 'is_required', 'code', 'title',)


__all__ = ['InsuredObjectSerializer', 'InsuredObjectParameterSerializer', 'InsuredObjectTypeSerializer']
