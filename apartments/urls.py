from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', info, name='info'),
    url(r'^(?P<building>\w{2})/$', apartments_list, name='apartments-list'),
    url(r'^(?P<building>\w{2})/(?P<code>\w{2}\d{3})/', apartment_detail, name='apartment-detail'),
    url(r'^(?P<building>\w{2}).?apartments.?(?P<code>\w{2}\d{3})', apartment_detail, name='apartment-detail')
    ]
