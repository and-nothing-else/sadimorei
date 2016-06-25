from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PressConfig(AppConfig):
    name = 'press'
    verbose_name = _('Press Releases')
