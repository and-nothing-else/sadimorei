from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class PressRelease(models.Model):
    name = models.CharField(_('Title'), max_length=256)
    date = models.DateField(_('Date'))
    text = RichTextUploadingField(_('Text'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('press:detail', args=[str(self.id)])

    class Meta:
        ordering = ["-date"]
        verbose_name = _('Press Release')
        verbose_name_plural = _('Press Releases')
