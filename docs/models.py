from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField


class Certificate(models.Model):
    name = models.CharField(_('name'), max_length=512)
    image = ImageField(_('image'), upload_to='cert')
    sorting = models.IntegerField(_('sorting'), default=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sorting']
        verbose_name = _('certificate')
        verbose_name_plural = _('certificates')


class Doc(models.Model):
    name = models.CharField(_('name'), max_length=512)
    preview = ImageField(_('image'), upload_to='docs')
    file = models.FileField(_('file'), upload_to='docs')
    sorting = models.IntegerField(_('sorting'), default=100)
    tech_info = models.CharField(_('tech info'), max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sorting']
        verbose_name = _('document')
        verbose_name_plural = _('documents')
