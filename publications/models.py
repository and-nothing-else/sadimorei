from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField


class NewsPortal(models.Model):
    name = models.CharField(_('Site Name'), max_length=128)
    logo = ImageField(_('Logo'), upload_to='newsportals')
    link = models.CharField(_('Link'), max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _('News Portal')
        verbose_name_plural = _('News Portals')


class Publication(models.Model):
    name = models.CharField(_('Article Name'), max_length=256)
    date = models.DateField(_('Date'))
    link = models.CharField(_('Article Link'), max_length=256)
    source = models.ForeignKey(NewsPortal, verbose_name=_('Source'))

    def __str__(self):
        return "%s, %s: %s" % (self.date, self.source, self.name,)

    def get_source(self):
        return NewsPortal.objects.get(pk=self.source_id)

    class Meta:
        ordering = ["-date"]
        verbose_name = _('Publication')
        verbose_name_plural = _('Publications')
