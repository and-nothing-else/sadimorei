from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField, get_thumbnail
from sorl.thumbnail.helpers import ThumbnailError


class Photo(models.Model):
    name = models.CharField(_('name'), max_length=256)
    active = models.BooleanField(_('active'), default=True)
    description = models.CharField(_('description'), max_length=512, null=True, blank=True)
    photo = ImageField(_('photo'), upload_to='photo')
    sorting = models.PositiveSmallIntegerField(_('sorting'), default=100)

    def __str__(self):
        return '{} ({})'.format(self.name, self.photo.url)

    def get_thumbnail_html(self):
        try:
            img_resize_url = get_thumbnail(self.photo, '200x64').url
            html = '<a href="%s"><img src="%s" alt="%s"></a>'
            return html % (self.photo.url, img_resize_url, self.name)
        except ThumbnailError:
            html = "<span>no file</span>"
            return html
    get_thumbnail_html.allow_tags = True

    class Meta:
        ordering = ["sorting"]
        verbose_name = _('photo')
        verbose_name_plural = _('photos')
