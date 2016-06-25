from django.conf.urls import url
from .views import FeedbackFormView, FeedbackSuccessView

urlpatterns = [
    url(r'^$', FeedbackFormView.as_view(), name='form'),
    url(r'^thanks/$', FeedbackSuccessView.as_view(), name='thanks'),
]
