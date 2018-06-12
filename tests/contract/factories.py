from factory import post_generation, SubFactory, DjangoModelFactory

from apps.common.models import AbstractParameter, AbstractOperationType
from apps.contract.models import (CalculationType, CalculationParameter, Calculation, ResultType, ResultParameter,
                                   Result)
from tests.account.factories import DepartmentFactory
from tests.handbooks.factories import HandBookFactory, InsuranceTypeFactory


class AbstractParameterFactory(HandBookFactory):

    param_type = 'string'
    is_required = True
    is_active = True

    class Meta:
        model = AbstractParameter


class AbstractOperationTypeFactory(HandBookFactory):

    department = SubFactory(DepartmentFactory)
    insurance_type = SubFactory(InsuranceTypeFactory)

    class Meta:
        model = AbstractOperationType


class CalculationTypeFactory(AbstractOperationTypeFactory):

    # pk = Sequence(lambda x: x)
    # payment_types = []

    @post_generation
    def payment_types(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for payment_type in extracted:
                self.payment_types.add(payment_type)

    class Meta:
        model = CalculationType


class CalculationParameterFactory(AbstractParameterFactory):

    is_active = True
    is_required = True

    @post_generation
    def calculation_types(self, create, extracted, **kwargs):
        if not create:
            return

        if not extracted:
            extracted = [SubFactory(CalculationTypeFactory)]
        for calculation_type in extracted:
            self.calculation_types.add(calculation_type)

    class Meta:
        model = CalculationParameter


class CalculationFactory(DjangoModelFactory):

    calculation_type = SubFactory(CalculationTypeFactory)
    parameters = ''

    class Meta:
        model = Calculation


class ResultTypeFactory(AbstractOperationTypeFactory):

    class Meta:
        model = ResultType


class ResultParameterFactory(AbstractParameterFactory):

    is_active = True
    is_required = True

    class Meta:
        model = ResultParameter

    @post_generation
    def result_types(self, create, extracted, **kwargs):
        if not create:
            return

        if not extracted:
            extracted = [SubFactory(ResultTypeFactory)]
        for result_type in extracted:
            self.result_types.add(result_type)


class ResultFactory(DjangoModelFactory):

    result_type = SubFactory(ResultTypeFactory)
    calculation = SubFactory(CalculationFactory)
    parameters = ''

    class Meta:
        model = Result
