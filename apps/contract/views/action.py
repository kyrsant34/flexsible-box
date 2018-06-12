from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from ..models import ActionParameter, ActionType, Action
from ..serializers import ActionParameterSerializer, ActionTypeSerializer, ActionSerializer


class ActionParametersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ActionParameter.objects.all()
    serializer_class = ActionParameterSerializer
    filter_fields = ('code',)


class ActionTypesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ActionType.objects.all()
    serializer_class = ActionTypeSerializer
    filter_fields = ('department', 'insurance_type',)


class ActionsViewSet(mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

    def filter_queryset(self, queryset):
        queryset = queryset.filter(**self.kwargs)
        return super().filter_queryset(queryset)

    def create(self, request, *args, **kwargs):
        request.data['insurance_contract'] = self.kwargs['insurance_contract']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        parameters = serializer.validated_data['parameters']
        action_type = serializer.validated_data['action_type']
        if parameters['success']:
            self.perform_create(serializer)
            new_contract_status = action_type.successfull_contract_status
            http_status = status.HTTP_201_CREATED
            data = serializer.data
        else:
            new_contract_status = action_type.fail_contract_status
            http_status = status.HTTP_400_BAD_REQUEST
            data = {'logic error'}

        insurance_contract = serializer.validated_data['insurance_contract']
        if new_contract_status and insurance_contract.insurance_contract_status != new_contract_status:
            insurance_contract.insurance_contract_status = new_contract_status
            insurance_contract.save()

        return Response(data, status=http_status)
