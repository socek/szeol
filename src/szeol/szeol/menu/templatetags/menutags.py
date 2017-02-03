from django import template

from szeol.menu.menu import MENU
from szeol.menu.models import MenuParser

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def left_menu(context):
    MenuParser
    return {'menu': MenuParser(MENU).parse(context.request)}
