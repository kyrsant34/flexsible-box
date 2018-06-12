from django import test
from django.db.utils import IntegrityError

from apps.contract.models import CalculationType, CalculationParameter, Calculation, ResultParameter, Result
from tests.handbooks.factories import PaymentTypeFactory, InsuranceTypeFactory
from tests.account.factories import DepartmentFactory
from tests.contract.factories import (CalculationTypeFactory, CalculationParameterFactory, CalculationFactory,
                                       ResultTypeFactory, ResultParameterFactory, ResultFactory)


class TestCalculationType(test.TestCase):

    def test_payment_types(self):
        payment_types = PaymentTypeFactory.create_batch(2)
        insurance_type = InsuranceTypeFactory()
        department = DepartmentFactory()
        calc_type_amt = 2
        CalculationTypeFactory.create_batch(calc_type_amt, payment_types=payment_types, insurance_type=insurance_type,
                                            department=department)

        # We expect for both of payment type to return exactly 2 records
        for payment_type in payment_types:
            self.assertEquals(calc_type_amt, CalculationType.objects.filter(payment_types__in=[payment_type]).count())

    def test_uniqueness(self):
        insurance_type = InsuranceTypeFactory()
        department = DepartmentFactory()
        code = 'FOO'

        with self.assertRaises(IntegrityError):
            CalculationTypeFactory.create_batch(2, insurance_type=insurance_type, department=department, code=code)


class TestCalculationParameter(test.TestCase):

    def test_uniqueness(self):
        code = 'FOO'

        with self.assertRaises(IntegrityError):
            CalculationParameterFactory.create_batch(2, code=code)

    def test_multiple_parameters(self):
        calculation_type = CalculationTypeFactory()
        calc_param_amt = 2
        CalculationParameterFactory.create_batch(calc_param_amt, calculation_types=[calculation_type])

        self.assertEquals(calc_param_amt, CalculationParameter.objects.filter(calculation_types=calculation_type).count())


class TestCalculation(test.TestCase):

    def test_multiple_calculation_types(self):
        calculation_type = CalculationTypeFactory()
        calc_amt = 2
        CalculationFactory.create_batch(calc_amt, calculation_type=calculation_type)

        self.assertEquals(calc_amt, Calculation.objects.filter(calculation_type=calculation_type).count())

    def test_input_parameters(self):
        user_input = {"FOO": "BAR"}
        CalculationFactory(pk=1, parameters=user_input)
        o = Calculation.objects.get(pk=1)
        self.assertDictEqual(user_input, o.parameters)

    def test_input_parameters_non_serializable_json(self):
        from datetime import datetime
        user_input = datetime.utcnow()
        with self.assertRaisesRegex(TypeError, 'is not JSON serializable'):
            CalculationFactory(pk=1, parameters=user_input)


class TestResultType(test.TestCase):

    def test_uniqueness(self):
        insurance_type = InsuranceTypeFactory()
        department = DepartmentFactory()
        code = 'FOO'
        with self.assertRaises(IntegrityError):
            ResultTypeFactory.create_batch(2, insurance_type=insurance_type, department=department, code=code)


class TestResultParameter(test.TestCase):

    def test_uniqueness(self):
        code = 'FOO'
        with self.assertRaises(IntegrityError):
            ResultParameterFactory.create_batch(2, code=code)

    def test_multiple_result_types(self):
        result_type = ResultTypeFactory()
        ResultParameterFactory.create_batch(2, result_types=[result_type])
        self.assertEquals(2, ResultParameter.objects.filter(result_types=result_type).count())


class TestResult(test.TestCase):

    def test_multiple_result_types(self):
        result_type = ResultTypeFactory()
        ResultFactory.create_batch(2, result_type=result_type)
        self.assertEquals(2, Result.objects.filter(result_type=result_type).count())

    def test_multiple_calculations(self):
        calculation = CalculationFactory()
        ResultFactory.create_batch(2, calculation=calculation)
        self.assertEquals(2, Result.objects.filter(calculation=calculation).count())
