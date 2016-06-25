from django import template
from ..menus import MAIN_MENU, SUB_MENU

register = template.Library()


@register.inclusion_tag('navs/main_menu.html', takes_context=True)
def main_menu(context):

    return {
        'items': MAIN_MENU
    }


@register.inclusion_tag('navs/sub_menu.html', takes_context=True)
def sub_menu(context):

    return {
        'items': SUB_MENU
    }
