from rest_framework import viewsets, mixins

from apps.handbooks.models import InsuranceContractStatus
from ..models import InsuranceContract
from ..serializers import InsuranceContractSerializer


class InsuranceContractsViewSet(viewsets.ReadOnlyModelViewSet, mixins.CreateModelMixin):
    queryset = InsuranceContract.objects.all()
    serializer_class = InsuranceContractSerializer

    def perform_create(self, serializer):
        serializer.validated_data['insurance_contract_status'] = InsuranceContractStatus.objects.get(
                code=InsuranceContractStatus.Code.DRAFT)
        return super().perform_create(serializer)


