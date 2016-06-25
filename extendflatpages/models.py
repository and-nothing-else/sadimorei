from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _


class ExtendFlatpage(FlatPage):
    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('static pages')
