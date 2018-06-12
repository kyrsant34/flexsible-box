from django.test import TestCase
from django.utils.translation import ugettext as _
from rest_framework import exceptions

from .factories import UserFactory

from apps.account.serializer import AuthTokenSerializer


class TestAuthTokenSerializer(TestCase):

    def test_validate_email_password_ok(self):
        serializer = AuthTokenSerializer()
        data = {'email': 'john@example.com', 'password': 'correct'}
        UserFactory(**data)
        self.assertIsNotNone(serializer.validate(attrs=data))

    def test_validate_email_password_error(self):
        serializer = AuthTokenSerializer()
        data = {'email': 'john@example.com', 'password': 'correct'}
        UserFactory(**data)
        data['password'] = 'incorrect'
        with self.assertRaisesRegex(exceptions.ValidationError, _('Unable to login with provided credentials.')):
            serializer.validate(attrs=data)

    def test_validate_email_error_password(self):
        serializer = AuthTokenSerializer()
        data = {'email': 'john@example.com', 'password': 'correct'}
        UserFactory(**data)
        data['email'] = 'incorrect@example.com'
        with self.assertRaisesRegex(exceptions.ValidationError, _('Unable to login with provided credentials.')):
            serializer.validate(attrs=data)

    def test_validate_username_error(self):
        serializer = AuthTokenSerializer()
        data = {'email': 'john@example.com', 'password': 'correct'}
        UserFactory(**data)
        data = {'username': 'john@example.com', 'password': 'correct'}
        with self.assertRaisesRegex(exceptions.ValidationError, _('Need email for authorization')):
            serializer.validate(attrs=data)

    def test_validate_non_active(self):
        serializer = AuthTokenSerializer()
        data = {'email': 'john@example.com', 'password': 'correct'}
        UserFactory(**data, is_active=False)
        # Should not it be "User account is disabled."?
        with self.assertRaisesRegex(exceptions.ValidationError, _('Unable to login with provided credentials.')):
            serializer.validate(attrs=data)
