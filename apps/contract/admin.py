from django.contrib import admin

from apps.common.admin import AbstractOperationAdmin, AbstractParameterAdmin

from .models import CalculationType, CalculationParameter, ResultType, ResultParameter, ActionType, ActionParameter


@admin.register(CalculationType)
class CalculationTypeAdmin(AbstractOperationAdmin):
    pass


@admin.register(CalculationParameter)
class CalculationParameterAdmin(AbstractParameterAdmin):
    filter_horizontal = ('calculation_types',)


@admin.register(ResultType)
class ResultTypeAdmin(AbstractOperationAdmin):
    pass


@admin.register(ResultParameter)
class ResultParameterAdmin(AbstractParameterAdmin):
    filter_horizontal = ('result_types',)


@admin.register(ActionType)
class ActionTypeAdmin(AbstractOperationAdmin):
    pass


@admin.register(ActionParameter)
class ActionParameterAdmin(AbstractParameterAdmin):
    filter_horizontal = ('action_types',)
