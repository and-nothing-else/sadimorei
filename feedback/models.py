from django.db import models
from django.utils.translation import ugettext_lazy as _


class Feedback(models.Model):
    datetime = models.DateTimeField(verbose_name=_('Add Time'), auto_now_add=True)
    name = models.CharField(verbose_name=_('Full Name'), max_length=256)
    contact = models.CharField(verbose_name=_('Contacts'), max_length=512)
    message = models.TextField(verbose_name=_('Message'))

    def __str__(self):
        return "{}. {}: {}".format(self.datetime, _('Author'), self.name)

    class Meta:
        ordering = ["-datetime"]
        verbose_name = _('Message')
        verbose_name_plural = _('Feedback')
