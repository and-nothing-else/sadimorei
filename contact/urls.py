from django.conf.urls import url
from .views import MapView


app_name = 'contact'
contact_patterns = ([
    url(r'^$', MapView.as_view(), name='map-list'),
], 'contact')
