from django.contrib import admin

from .models import (AddressType, AttachmentType, CarMark, CarModel, CredentialType, ContactType, InsuranceType,
                     MessageType, PaymentType, InsuranceContractStatus)


class HandBookAdmin(admin.ModelAdmin):

    # readonly_fields = ('code',)

    def get_readonly_fields(self, request, obj=None):
        # Return read-only 'code' field only whe editing, not while adding new record
        # See: https://stackoverflow.com/questions/4343535
        if obj:
            return self.readonly_fields + ('code',)
        return self.readonly_fields


@admin.register(AddressType)
class AddressTypeAdmin(HandBookAdmin):
    pass


@admin.register(AttachmentType)
class AttachmentTypeAdmin(HandBookAdmin):
    pass


@admin.register(CarMark)
class CarMarkAdmin(HandBookAdmin):
    pass


@admin.register(CarModel)
class CarModelAdmin(HandBookAdmin):
    pass


@admin.register(CredentialType)
class CredentialTypeAdmin(HandBookAdmin):
    pass


@admin.register(ContactType)
class ContactTypeAdmin(HandBookAdmin):
    pass


@admin.register(InsuranceType)
class InsuranceTypeAdmin(HandBookAdmin):
    pass


@admin.register(MessageType)
class MessageTypeAdmin(HandBookAdmin):
    pass


@admin.register(PaymentType)
class PaymentTypeAdmin(HandBookAdmin):
    pass


@admin.register(InsuranceContractStatus)
class InsuranceContractStatusAdmin(HandBookAdmin):
    filter_horizontal = ('availiable_action_types',)

