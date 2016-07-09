from django import template
from django.utils import timezone


register = template.Library()


@register.inclusion_tag('main/copyright.html')
def copyright_block():
    return {'current_year': timezone.now().year}
