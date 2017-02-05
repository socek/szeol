from django.db.models import CharField
from django.db.models import Model
from django.utils.translation import ugettext as _


class Product(Model):
    TASTES = (
        ('d', _('Dry')),
        ('sd', _('Semi-Dry')),
        ('ss', _('Semi-Sweet')),
        ('s', _('Sweet')))

    COLORS = (
        ('wh', _('White')),
        ('re', _('Red')),
        ('ro', _('Rosé')))

    name = CharField(max_length=50, help_text=_('Name'))
    year = CharField(max_length=5, help_text=_('Year'))
    taste = CharField(max_length=2, choices=TASTES, help_text=_('Taste'))
    color = CharField(max_length=2, choices=COLORS, help_text=_('Color'))
