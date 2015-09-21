from django.conf.urls import url, include
import django.contrib.auth
from .views import overview, user_info

urlpatterns = [
    url('^$', overview),
    url('^info$', user_info),
]
