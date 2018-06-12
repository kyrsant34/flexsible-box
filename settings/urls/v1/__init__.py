from django.conf.urls import url, include


urlpatterns = [
        url(r'handbooks/', include('settings.urls.v1.handbooks')),
        url(r'contract/', include('settings.urls.v1.contract')),
        url(r'account/', include('settings.urls.v1.account')),
        url(r'client/', include('settings.urls.v1.client')),
]
