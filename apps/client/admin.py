from django.contrib import admin

from apps.common.admin import AbstractParameterAdmin, AbstractOperationAdmin

from .models import InsuredObjectParameter, InsuredObjectType


@admin.register(InsuredObjectType)
class InsuredObjectTypeAdmin(AbstractOperationAdmin):
    pass


@admin.register(InsuredObjectParameter)
class InsuredObjectParameterAdmin(AbstractParameterAdmin):
    filter_horizontal = ('insured_object_types',)
