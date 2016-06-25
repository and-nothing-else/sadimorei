from django import template
from ..models import Photo

register = template.Library()


@register.inclusion_tag('gallery/_random_photos.html')
def random_photos():
    return {'photos': Photo.objects.filter(active=True).order_by('?')[:2]}
