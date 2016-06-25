"""sadimorei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from reasons.views import ReasonListView
from contact.urls import contact_patterns


urlpatterns = [
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^$', ReasonListView.as_view(), name='home'),
    url(r'^contact/', include(contact_patterns)),
    url(r'^apartments/', include('apartments.urls', namespace="apartments")),
    url(r'^news/', include('news.urls', namespace="news")),
    url(r'^publications/', include('publications.urls', namespace="publications")),
    url(r'^press/', include('press.urls', namespace="press")),
    url(r'^docs/', include('docs.urls', namespace="docs")),
    url(r'^gallery/', include('gallery.urls', namespace="gallery")),
    url(r'^feedback/', include('feedback.urls', namespace="feedback")),
]


if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ] + urlpatterns
