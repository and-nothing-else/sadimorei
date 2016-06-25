from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField, get_thumbnail
from sorl.thumbnail.helpers import ThumbnailError
from ckeditor_uploader.fields import RichTextUploadingField


class Reason(models.Model):
    number = models.IntegerField(_('Number'), default=0)
    name = models.CharField(_('Reason name'), max_length=80, blank=True, null=True)
    nameFontSize = models.IntegerField(_('Font Size'), default=173, blank=True, null=True)
    nameLetterSpacing = models.IntegerField(_('Letter Spacing'), default=34, blank=True, null=True)
    linkText = models.CharField(_('Link text'), max_length=80, default=_('Read more'), blank=True, null=True)
    image = ImageField(_('Banner image'), upload_to='reasons')
    text = RichTextUploadingField(_('Reason description'), blank=True, null=True)

    def __str__(self):
        return "#%d: %s" % (self.number, self.name)

    def get_thumbnail_html(self):
        try:
            img_resize_url = get_thumbnail(self.image, '200x64').url
            html = '<a href="%s"><img src="%s" alt="%s"></a>'
            return html % (self.image.url, img_resize_url, self.name)
        except ThumbnailError:
            html = "<span>no file</span>"
            return html
    get_thumbnail_html.allow_tags = True

    class Meta:
        verbose_name = _('Reason')
        verbose_name_plural = _('Reasons')
        ordering = ["number"]
