from django.test import TransactionTestCase

from apps.handbooks.serializers import CredentialTypeSerializer
from apps.handbooks.models import CredentialType
from .factories import CredentialTypeFactory


class TestCredentialTypeSerializer(TransactionTestCase):

    def test_serialize_one(self):
        o = CredentialTypeFactory(code="FOO", title="BAR")
        serializer = CredentialTypeSerializer(o)
        self.assertIsNotNone(serializer.data)

    def test_serialize_many(self):
        CredentialTypeFactory.create()
        CredentialTypeFactory.create()
        serializer = CredentialTypeSerializer(CredentialType.objects.all(), many=True)
        self.assertTrue(serializer.data)
