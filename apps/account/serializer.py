from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        ERR_CODE = 'authorization'

        if not email:
            msg = _('Need email for authorization')
            raise serializers.ValidationError(msg, code=ERR_CODE)

        if email and password:
            user = authenticate(email=email, password=password)
        else:
            user = None

        if user is None:
            msg = _('Unable to login with provided credentials.')
            raise serializers.ValidationError(msg, code=ERR_CODE)

        if user and not user.is_active:
            msg = _('User account is disabled.')
            raise serializers.ValidationError(msg, code=ERR_CODE)

        attrs['user'] = user
        return attrs
