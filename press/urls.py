from django.conf.urls import url
from .views import PressListView, PressDetailView


urlpatterns = [
    url(r'^$', PressListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PressDetailView.as_view(), name='detail'),
]
