from django.conf.urls import url

from apps.handbooks.views import (AddressTypesList, AttachmentTypesList, CarMarksList, CarModelsList, ContactTypesList,
                             CredentialTypesList, InsuranceTypesList, MessageTypesList, PaymentTypesList,
                             InsuranceContractStatusList)


urlpatterns = [
    url('address_types', AddressTypesList.as_view()),
    url('attachment_types', AttachmentTypesList.as_view()),
    url('car_marks', CarMarksList.as_view()),
    url('car_models', CarModelsList.as_view()),
    url('contact_types', ContactTypesList.as_view()),
    url('credential_types', CredentialTypesList.as_view()),
    url('insurance_types', InsuranceTypesList.as_view()),
    url('message_types', MessageTypesList.as_view()),
    url('payment_types', PaymentTypesList.as_view()),
    url('insurance_contract_status', InsuranceContractStatusList.as_view()),
]
