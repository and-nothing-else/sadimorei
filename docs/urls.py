from django.conf.urls import url
from .views import doc_list


urlpatterns = [
    url(r'^$', doc_list, name='index'),
]
