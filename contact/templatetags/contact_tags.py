from contact.models import Office
from django import template
register = template.Library()


@register.inclusion_tag('contact/office_link.html')
def office_link(office_code):
    office = Office.objects.get(slug=office_code)
    return {'office': office}


@register.inclusion_tag('contact/office_label.html')
def office_label(office_code):
    office = Office.objects.get(slug=office_code)
    return {'office': office}


@register.inclusion_tag('contact/office_info.html')
def office_info(office_code):
    office = Office.objects.get(slug=office_code)
    return {'office': office}
