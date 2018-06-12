from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers


class NestedModelSerializer(serializers.ModelSerializer):
    RELATION_DESCRIPTOR_TYPES = ('ReverseManyToOneDescriptor', 'ReverseGenericManyToOneDescriptor')

    class Meta:
        abstract = True

    def create(self, validated_data):

        def create_nested_field(field, field_value):
            try:
                validated_data[field.source] = field.create(field_value)
            except Exception as err:
                raise serializers.ValidationError({field.source: err})

        model_class = self.Meta.model
        deferred_data = {}
        for field in self._writable_fields:
            field_name = field.source
            field_value = validated_data.get(field_name)

            # Убираем значения field_value == [] и field_value == {}, т.к. это не проходит встроеную валидацию
            is_mutable_type = isinstance(field_value, (list, dict))
            if not field_value and is_mutable_type:
                del validated_data[field_name]
                continue

            if not (field_value is not None
                    and isinstance(field, serializers.BaseSerializer)
                    and is_mutable_type):
                continue

            # здесь выбираем объекты которые должны создаваться после super()
            model_field_descriptor = getattr(model_class, field_name, None)
            if model_field_descriptor is None:
                model_field_descriptor = getattr(model_class, f'{field_name}_set', None)

            if model_field_descriptor and model_field_descriptor.__class__.__name__ in self.RELATION_DESCRIPTOR_TYPES:
                deferred_data[field_name] = {
                    'field': field,
                    'field_value': validated_data.pop(field_name),
                    'field_descriptor': model_field_descriptor
                }
                continue

            create_nested_field(field, field_value)

        instance = super().create(validated_data)

        if deferred_data:
            content_type = ContentType.objects.get_for_model(model_class)
            instance_pk = instance.pk

        for field_data in deferred_data.values():
            field_descriptor_name = field_data['field_descriptor'].__class__.__name__
            model_field = field_data['field_descriptor'].field

            if field_descriptor_name == 'ReverseManyToOneDescriptor':
                related_name = model_field.name
                additional_data = {
                        related_name: instance
                }

            elif field_descriptor_name == 'ReverseGenericManyToOneDescriptor':
                additional_data = {
                        model_field.content_type_field_name: content_type,
                        model_field.object_id_field_name: instance_pk
                }

            else:
                print(f"Don't know descriptor {field_descriptor_name}")
                continue

            if isinstance(field_data['field_value'], list):
                for field_value in field_data['field_value']:
                    field_value.update(additional_data)
            create_nested_field(field_data['field'], field_data['field_value'])

        return instance
