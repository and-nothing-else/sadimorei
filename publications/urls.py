from django.conf.urls import url
from .views import PublicationListView


urlpatterns = [
    url(r'^$', PublicationListView.as_view(), name='list'),
]
