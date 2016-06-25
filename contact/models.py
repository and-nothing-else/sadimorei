from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
import re


class Office(models.Model):
    name = models.CharField(_('Office Name'), max_length=256)
    sorting = models.IntegerField(_('Sorting'), default=100)
    slug = models.SlugField(_('Slug'), max_length=32)
    address = models.CharField(_('Office Address'), max_length=256)
    phone = models.CharField(_('Phone'), max_length=32)
    lat = models.CharField(_('Latitude'), default='55.772406', max_length=16)
    lng = models.CharField(_('Longitude'), default='37.638447', max_length=16)
    scale = models.IntegerField(_('Map scale'), default=16)

    def __str__(self):
        return re.compile(r'<.*?>').sub(' ', self.name)

    def get_absolute_url(self):
        return reverse('contact:map-list') + "#" + self.slug

    class Meta:
        ordering = ["sorting"]
        verbose_name = _('Office')
        verbose_name_plural = _('Offices')
