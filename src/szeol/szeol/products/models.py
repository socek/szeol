from datetime import datetime
from datetime import timedelta

from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import Model
from django.utils.translation import ugettext as _

from szeol.main.utils import default_now


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

    when_created = DateTimeField(default=default_now, db_index=True)

    class Driver(object):

        @staticmethod
        def _viewable():
            """
            Products which are visible by for user.
            """
            return Product.objects

        @staticmethod
        def _last_week_created():
            """
            Products which were created in last 7 days.
            """
            week_ego = datetime.utcnow() - timedelta(days=7)
            return Product.objects.filter(when_created__gte=week_ego)

        @classmethod
        def viewable(cls):
            return cls._viewable().all()

        @classmethod
        def viewable_count(cls):
            return cls._viewable().count()

        @classmethod
        def last_week_created_count(cls):
            return cls._last_week_created().count()

    @property
    def taste_name(self):
        return dict(self.TASTES)[self.taste]

    @property
    def color_name(self):
        return dict(self.COLORS)[self.color]
