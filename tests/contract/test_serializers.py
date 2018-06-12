from django.test import TestCase

from .factories import (CalculationTypeFactory, CalculationParameterFactory, ResultTypeFactory, ResultParameterFactory,
                        CalculationFactory)
from tests.account.factories import UserFactory
from apps.contract.serializers import CalculationSerializer, ResultSerializer


class TestCalculationSerializer(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.creator = UserFactory()

    def setUp(self):
        self.creator.refresh_from_db()
        request = type('Request', (), {})()
        setattr(request, 'user', self.creator)
        self.context = {'request': request}

    def test_normal(self):
        calc_type = CalculationTypeFactory()
        p1 = CalculationParameterFactory(calculation_types=[calc_type])
        user_input = {
            'calculation_type': calc_type.code,
            'parameters': {
                p1.code: 'FOO'
            }
        }
        s = CalculationSerializer(data=user_input, context=self.context)
        self.assertTrue(s.is_valid())

    def test_no_required_parameter(self):
        calc_type = CalculationTypeFactory()
        CalculationParameterFactory(calculation_types=[calc_type])
        user_input = {
            'calculation_type': calc_type.code,
            'parameters': {},
        }
        s = CalculationSerializer(data=user_input, context=self.context)
        self.assertFalse(s.is_valid())

    def test_unexpected_parameter(self):
        calc_type = CalculationTypeFactory()
        user_input = {
            'calculation_type': calc_type.code,
            'parameters': {
                'FOO': 'BAR'
            }
        }
        s = CalculationSerializer(data=user_input, context=self.context)
        self.assertTrue(s.is_valid())

    def test_non_active_parameter(self):
        calc_type = CalculationTypeFactory()
        p1 = CalculationParameterFactory(calculation_types=[calc_type], is_active=False)
        user_input = {
            'calculation_type': calc_type.code,
            'parameters': {
                p1.code: 'FOO'
            }
        }
        s = CalculationSerializer(data=user_input, context=self.context)
        self.assertTrue(s.is_valid())

    def test_missing_non_required_parameter(self):
        calc_type = CalculationTypeFactory()
        CalculationParameterFactory(is_required=False, calculation_types=[calc_type])
        user_input = {
            'calculation_type': calc_type.code,
            'parameters': {}
        }
        s = CalculationSerializer(data=user_input, context=self.context)
        self.assertTrue(s.is_valid())


class TestResultSerializer(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.creator = UserFactory()

    def setUp(self):
        self.creator.refresh_from_db()
        request = type('Request', (), {})()
        setattr(request, 'user', self.creator)
        self.context = {'request': request}

    def test_normal(self):
        res_type = ResultTypeFactory()
        calculation = CalculationFactory()
        p1 = ResultParameterFactory(result_types=[res_type])
        user_input = {
            'result_type': res_type.code,
            'calculation': calculation.pk,
            'parameters': {
                p1.code: 'FOO'
            }
        }
        s = ResultSerializer(data=user_input, context=self.context)
        self.assertTrue(s.is_valid())

    def test_no_required_parameter(self):
        res_type = ResultTypeFactory()
        ResultParameterFactory(result_types=[res_type])
        calculation = CalculationFactory()
        user_input = {
            'result_type': res_type.code,
            'calculation': calculation.pk,
            'parameters': {}
        }
        s = ResultSerializer(data=user_input, context=self.context)
        self.assertFalse(s.is_valid())

    def test_unexpected_parameter(self):
        res_type = ResultTypeFactory()
        calculation = CalculationFactory()
        user_input = {
            'result_type': res_type.code,
            'calculation': calculation.pk,
            'parameters': {
                'FOO': 'BAR'
            }
        }
        s = ResultSerializer(data=user_input, context=self.context)
        self.assertTrue(s.is_valid())

    def test_non_active_parameter(self):
        res_type = ResultTypeFactory()
        calculation = CalculationFactory()
        p1 = ResultParameterFactory(result_types=[res_type], is_active=False)
        user_input = {
            'result_type': res_type.code,
            'calculation': calculation.pk,
            'parameters': {
                p1.code: 'FOO'
            }
        }
        s = ResultSerializer(data=user_input, context=self.context)
        self.assertTrue(s.is_valid())

    def test_missing_non_required_parameter(self):
        res_type = ResultTypeFactory()
        calculation = CalculationFactory()
        ResultParameterFactory(result_types=[res_type], is_required=False)
        user_input = {
            'result_type': res_type.code,
            'calculation': calculation.pk,
            'parameters': {}
        }
        s = ResultSerializer(data=user_input, context=self.context)
        self.assertTrue(s.is_valid())
