from rest_framework.authtoken import views

from apps.account.serializer import AuthTokenSerializer


class ObtainAuthToken(views.ObtainAuthToken):
    serializer_class = AuthTokenSerializer
