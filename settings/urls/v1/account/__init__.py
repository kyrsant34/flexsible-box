from django.conf.urls import url

from apps.account.views import ObtainAuthToken


urlpatterns = [
    url(r'^obtain-token/$', ObtainAuthToken.as_view())
]
