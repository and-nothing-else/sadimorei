from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class ActualNewsManager(models.Manager):
    def get_query_set(self):
        return super(ActualNewsManager, self).get_query_set().filter(active=True)


class News(models.Model):
    name = models.CharField(_('Title'), max_length=256)
    date = models.DateField(verbose_name=_('Date'))
    announce = RichTextUploadingField(_('Announce'), blank=True, null=True)
    text = RichTextUploadingField(_('Text'))
    active = models.BooleanField(_('Active'), default=True)

    objects = models.Manager()
    actual = ActualNewsManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news:detail', args=[str(self.id)])

    class Meta:
        ordering = ["-date"]
        verbose_name = _('News Article')
        verbose_name_plural = _('News Articles')
