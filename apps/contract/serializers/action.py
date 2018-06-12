from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from apps.common.validators import ParametersValidator
from ..models import ActionParameter, ActionType, Action


class ActionParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionParameter
        fields = ('action_types', 'param_type', 'is_active', 'is_required', 'code', 'title',)


class ActionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionType
        fields = ('department', 'insurance_type', 'code', 'title', 'successfull_contract_status',
                  'fail_contract_status')


class ActionSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Action
        fields = ('id', 'action_type', 'parameters', 'created', 'creator', 'insurance_contract')

        validators = [
            UniqueTogetherValidator(queryset=Action.objects.all(), fields=('action_type', 'insurance_contract')),
            ParametersValidator(operation_model_type_field='action_type', parameter_model=ActionParameter)
        ]

    def validate(self, attrs):
        availiable_action_types = attrs['insurance_contract'].insurance_contract_status.availiable_action_types.all()
        action_type = attrs['action_type']
        if action_type not in availiable_action_types:
            availiable_action_pk_list = list(availiable_action_types.values_list('pk', flat=True))
            msg = f'deny action type {action_type.pk}, availiable action types - {availiable_action_pk_list}'
            raise serializers.ValidationError(msg)
        return attrs
