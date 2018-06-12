from django.test import TestCase

from apps.handbooks.models import (HandBook, AddressType, AttachmentType, CarMark, CarModel, ContactType,
                                   CredentialType, InsuranceType, MessageType, PaymentType)

from .factories import CarMarkFactory


# class TestHandbook(TestCase):
#
#     def test_abstract(self):
#         with self.assertRaisesMessage(AttributeError, "'NoneType' object has no attribute 'attname'"):
#             handbook = HandBook(code="FOO", title="BAR")
#             handbook.save()


class TestAddressType(TestCase):

    def test_create(self):
        i1 = AddressType(code="FOO", title="BAR")
        i1.save()
        i2 = AddressType.objects.get(code="FOO")
        self.assertNotEqual(id(i1), id(i2))
        self.assertEqual(i1, i2)


class TestAttachmentType(TestCase):

    def test_create(self):
        i1 = AttachmentType(code="FOO", title="BAR")
        i1.save()
        i2 = AttachmentType.objects.get(code="FOO")
        self.assertNotEqual(id(i1), id(i2))
        self.assertEqual(i1, i2)


class TestCarMark(TestCase):

    def test_create(self):
        i1 = CarMark(code="FOO", title="BAR")
        i1.save()
        i2 = CarMark.objects.get(code="FOO")
        self.assertNotEqual(id(i1), id(i2))
        self.assertEqual(i1, i2)


class TestCarModel(TestCase):

    def setUp(self):
        self.car_mark = CarMarkFactory()

    def test_create(self):
        i1 = CarModel(code="FOO", title="BAR", car_mark=self.car_mark)
        i1.save()
        i2 = CarModel.objects.get(code="FOO")
        self.assertNotEqual(id(i1), id(i2))
        self.assertEqual(i1, i2)


class TestContactType(TestCase):

    def test_create(self):
        i1 = ContactType(code="FOO", title="BAR")
        i1.save()
        i2 = ContactType.objects.get(code="FOO")
        self.assertNotEqual(id(i1), id(i2))
        self.assertEqual(i1, i2)


class TestCredentialType(TestCase):

    def test_create(self):
        i1 = CredentialType(code="FOO", title="BAR")
        i1.save()
        i2 = CredentialType.objects.get(code="FOO")
        self.assertNotEqual(id(i1), id(i2))
        self.assertEqual(i1, i2)


class TestMessageType(TestCase):

    def test_create(self):
        i1 = MessageType(code="FOO", title="BAR")
        i1.save()
        i2 = MessageType.objects.get(code="FOO")
        self.assertNotEqual(id(i1), id(i2))
        self.assertEqual(i1, i2)


class TestPaymentType(TestCase):

    def test_create(self):
        i1 = PaymentType(code="FOO", title="BAR")
        i1.save()
        i2 = PaymentType.objects.get(code="FOO")
        self.assertNotEqual(id(i1), id(i2))
        self.assertEqual(i1, i2)


class TestInsuranceType(TestCase):

    def test_create(self):
        i1 = InsuranceType(code="FOO", title="BAR")
        i1.save()
        i2 = InsuranceType.objects.get(code="FOO")
        self.assertNotEqual(id(i1), id(i2))
        self.assertEqual(i1, i2)
