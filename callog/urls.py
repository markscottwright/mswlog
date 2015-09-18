from django.conf.urls import url, include
import django.contrib.auth

urlpatterns = [
    url('^', include('django.contrib.auth.urls'))
]
