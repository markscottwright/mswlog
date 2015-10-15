from django.conf.urls import url
from .views import overview, user_info, weigh_ins

urlpatterns = [
    url('^$', overview),
    url('^info$', user_info),
    url('^weighins$', weigh_ins),
]
