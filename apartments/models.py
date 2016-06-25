from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from sorl.thumbnail import ImageField, get_thumbnail
from sorl.thumbnail.helpers import ThumbnailError
from ckeditor_uploader.fields import RichTextUploadingField


class Building(models.Model):
    name = models.CharField(_('Building Name'), max_length=64)
    code = models.CharField(_('Two-letters Code'), max_length=2)
    sorting = models.IntegerField(_('Sorting'), default=100)
    description_title = models.CharField(_('Description Title'), max_length=128)
    description = models.TextField(_('Building Description'))
    photo = ImageField(_('Building Photo'), upload_to='buildings')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Building')
        verbose_name_plural = _('Buildings')
        ordering = ["sorting"]


class BuildingPhoto(models.Model):
    photo = ImageField(_('photo'), upload_to='building_photo')
    description = models.TextField(_('description'), blank=True, null=True)
    ordering = models.IntegerField(_('ordering'), default=100)
    building = models.ForeignKey(Building)

    class Meta:
        ordering = ['ordering']

    def thumbnail(self):
        try:
            img_resize_url = get_thumbnail(self.photo, '64x64').url
            return '<a href="%s"><img src="%s" alt="%s"></a>' % (self.photo.url, img_resize_url, self.description)
        except ThumbnailError:
            return "<span>no file</span>"
    thumbnail.allow_tags = True


class LayoutType(models.Model):
    name = models.CharField(_('Layout Type Name'), max_length=64)
    sorting = models.IntegerField(_('Sorting'), default=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["sorting"]
        verbose_name = _('Layout Type')
        verbose_name_plural = _('Layout Types')


class Layout(models.Model):
    """
    Планировка самой квартиры
    """
    name = models.CharField(_('Layout Name'), max_length=256)
    image = models.FileField(_('Layout Image'), upload_to='layout')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _('Layout')
        verbose_name_plural = _('Layouts')


class Placement(models.Model):
    """
    Размещение апартамента в корпусе
    """
    name = models.CharField(_('Placement Name'), max_length=256)
    image = models.FileField(_('Placement Image'), upload_to='placement')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _('Placement')
        verbose_name_plural = _('Placements')


class ApartmentDescriptionManager(models.Manager):
    def get(self, *args, **kwargs):
        try:
            elm = self.get_query_set().get(*args, **kwargs)
        except self.model.DoesNotExist:
            kwargsForAllBuildings = kwargs
            del kwargsForAllBuildings['building']
            try:
                elm = self.get_query_set().filter(*args, **kwargsForAllBuildings)[1]
            except self.model.DoesNotExist:
                kwargsForAllLayouts = kwargs
                del kwargsForAllLayouts['layout_type']
                try:
                    elm = self.get_query_set().filter(*args, **kwargsForAllLayouts)[1]
                except self.model.DoesNotExist:
                    elm = self.get_empty_query_set()
        return elm


class ApartmentDescription(models.Model):
    """
    Описания апартаментов
    """
    building = models.ForeignKey(Building, verbose_name=_('Building'), null=True, blank=True)
    layout_type = models.ForeignKey(LayoutType, verbose_name=_('Layout Type'), null=True, blank=True)
    description = RichTextUploadingField(_('Description'))

    def __str__(self):
        try:
            building_name = Building.objects.get(pk=self.building_id).name
        except Building.DoesNotExist:
            building_name = _('default')
        try:
            layout_name = LayoutType.objects.get(pk=self.layout_type_id).name
        except LayoutType.DoesNotExist:
            layout_name = _('default')
        return "%s, %s" % (layout_name, building_name)

    class Meta:
        ordering = ["layout_type"]
        verbose_name = _('Apartment Description')
        verbose_name_plural = _('Apartment Descriptions')
    objects = ApartmentDescriptionManager()


AVAILABLE, BOOKED, SOLD = 0, 1, 2
STATUS_CHOICES = (
    (AVAILABLE, _('Available')),
    (BOOKED, _('Booked')),
    (SOLD, _('Sold')),
)


class ActualApartmentManager(models.Manager):
    def get_query_set(self):
        return super(ActualApartmentManager, self).get_query_set().filter(status__in=[AVAILABLE, BOOKED])


class Apartment(models.Model):
    code = models.CharField(max_length=5, verbose_name=_('Apartment Code'))
    building = models.ForeignKey(Building, verbose_name=_('Building'))
    FLOOR_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),)
    floor = models.IntegerField(verbose_name=_('Floor'), choices=FLOOR_CHOICES)
    mansard = models.BooleanField(default=False, verbose_name=_('Mansard'))
    square = models.DecimalField(max_digits=4, decimal_places=1, verbose_name=_('Square'))
    balcony_square = models.DecimalField(max_digits=4, decimal_places=1, verbose_name=_('Balcony Square'),
                                         null=True, blank=True)
    loggia_square = models.DecimalField(max_digits=4, decimal_places=1, verbose_name=_('Loggia Square'),
                                        null=True, blank=True)
    layout_type = models.ForeignKey(LayoutType, verbose_name=_('Layout Type'))
    layout = models.ForeignKey(Layout, verbose_name=_('Layout'), null=True, blank=True)
    placement = models.ForeignKey(Placement, verbose_name=_('Placement'), null=True, blank=True)
    sea_view = models.BooleanField(default=False, verbose_name=_('Sea View'))
    terrace = models.BooleanField(default=False, verbose_name=_('Terrace Exists'))
    lawn = models.BooleanField(default=False, verbose_name=_('Lawn Exists'))
    price = models.IntegerField(verbose_name=_('Price'))
    status = models.IntegerField(verbose_name=_('Status'), choices=STATUS_CHOICES)

    objects = models.Manager()
    actual = ActualApartmentManager()

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('apartments:apartment-detail', args=[str(self.code)])

    def get_placement_image(self):
        return Placement.objects.get(pk=self.placement_id).image

    def get_layout_image(self):
        return Layout.objects.get(pk=self.layout_id).image

    def get_apartment_description(self):
        try:
            description = ApartmentDescription.objects.get(
                building=self.building_id,
                layout_type=self.layout_type_id
            ).description
        except:
            description = ''
        return description

    class Meta:
        ordering = ["price"]
        verbose_name = _('Apartment')
        verbose_name_plural = _('Apartments')
