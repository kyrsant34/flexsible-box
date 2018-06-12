from django.apps.registry import apps
# from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ParametersValidator(object):

    # default_error_messages = {
    #     'operation_type_required': _('\'{parameter_type_field}\' field is required.'),
    #     'parameters_required': _('\'parameters\' field is required.'),
    #     'parameter_required': _('Parameters required but not present: {parameters}.'),
    #     'unexpected_parameters': _('Got unexpected parameters: {parameters}.'),
    # }

    def __init__(self, operation_model_type_field, parameter_model, **kwargs):
        self.VALIDATE_FIELD_NAME = kwargs.get('validate_field_name', 'parameters')
        self.OPERATION_MODEL_TYPE_FIELD = operation_model_type_field
        self.PARAMETER_MODEL_TYPE_FIELD = kwargs.get('parameter_model_type_field', f'{self.OPERATION_MODEL_TYPE_FIELD}s')
        self.parameter_model = parameter_model

    def fail(self, data):
        # message = self.default_error_messages[message_code].format(**kwargs)
        raise ValidationError({self.VALIDATE_FIELD_NAME: data})

    def get_field_by_param(self, param):
        field_args = param.param_type.split('.')
        if len(field_args) == 2:
            app_name = field_args[0]
            model_name = field_args[1]
            model = apps.get_model(app_name, model_name)
            field = serializers.PrimaryKeyRelatedField(queryset=model.objects.all(), many=bool(param.is_many))
        elif len(field_args) == 1:
            serializer_field_name = self.parameter_model.PARAMETERS_TYPES[param.param_type]['serializer_field_name']
            field = getattr(serializers, serializer_field_name)()
        else:
            raise serializers.ValidationError(f'''can't validate class for field"{param.code}"''')
        field.required = param.is_required
        return field

    def __call__(self, data, strict_mode=False):
        if self.VALIDATE_FIELD_NAME not in data:
            return data
        parameters_data = data[self.VALIDATE_FIELD_NAME]
        operation_type_pk = data.get(self.OPERATION_MODEL_TYPE_FIELD)
        if operation_type_pk is None:
            self.fail(f'{self.OPERATION_MODEL_TYPE_FIELD} field is required')

        parameters = self.parameter_model.objects.all_active(**{self.PARAMETER_MODEL_TYPE_FIELD: operation_type_pk})
        parameters_serializer = serializers.Serializer(data=parameters_data)
        for param in parameters:
            parameters_serializer.fields[param.code] = self.get_field_by_param(param)
        if not parameters_serializer.is_valid():
            self.fail(data=parameters_serializer.errors)
        if strict_mode:
            unexpected_data = set(parameters_serializer.initial_data) - set(parameters_serializer.data)
            # unexpected_data = {key: val for key, val in parameters_serializer.initial_data
            #                                 if key not in parameters_serializer.data}
            if unexpected_data:
                self.fail(f'unexpected keywords {unexpected_data}')

        data[self.VALIDATE_FIELD_NAME] = parameters_serializer.data
        return data
