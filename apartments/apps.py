from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ApartmentsConfig(AppConfig):
    name = 'apartments'
    verbose_name = _('Apartments')
