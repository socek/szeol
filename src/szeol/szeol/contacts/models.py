from datetime import datetime
from datetime import timedelta

from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import Model
from django.utils.translation import ugettext as _
from django.utils.translation import pgettext as _p

from szeol.main.utils import default_now


class Contact(Model):
    name = CharField(max_length=50, help_text=_p('user name', 'Name'))
    surname = CharField(max_length=50, help_text=_('Surname'))
    address = CharField(max_length=255, help_text=_('Address'), null=True)

    when_created = DateTimeField(default=default_now, db_index=True)

    class Driver(object):

        @staticmethod
        def _viewable():
            """
            Contacts which are visible by for user.
            """
            return Contact.objects

        @staticmethod
        def _last_week_created():
            """
            Contacts which were created in last 7 days.
            """
            week_ego = datetime.utcnow() - timedelta(days=7)
            return Contact.objects.filter(when_created__gte=week_ego)

        @classmethod
        def viewable(cls):
            return cls._viewable().all()

        @classmethod
        def viewable_count(cls):
            return cls._viewable().count()

        @classmethod
        def last_week_created_count(cls):
            return cls._last_week_created().count()

        @classmethod
        def get_viewable_by_id(cls, id_):
            return cls._viewable().get(id=id_)
