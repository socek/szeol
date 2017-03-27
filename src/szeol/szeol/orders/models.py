from datetime import datetime
from datetime import timedelta

from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import DecimalField
from django.db.models import ForeignKey
from django.db.models import IntegerField
from django.db.models import Model
from django.utils.translation import ugettext as _

from szeol.main.utils import default_now


class OrderStatus(object):
    """
    State of the order.
        PENDING - order has not yet been approved by client and may change.
        APPROVED_BY_CLIENT - order has been approved by the client and can be
            sent to storehouse
        SENT_TO_STOREHOUSE - stroyhouse is prepering the order
        SHIPPING - order is waiting to be deliverd to the client
        DELIVERED - order is delivered
    """
    PENDING = 0
    APPROVED_BY_CLIENT = 1
    SENT_TO_STOREHOUSE = 2
    SHIPPING = 3
    DELIVERED = 4

    _CHOICES = (
        (PENDING, _('Pending')),
        (APPROVED_BY_CLIENT, _('Approved')),
        (SENT_TO_STOREHOUSE, _('Sent to storyhouse')),
        (SHIPPING, _('Shipping')),
        (DELIVERED, _('Delivered')),
    )

    _DICT = dict(_CHOICES)


class PaymentStatus(object):
    """
    State of the payment:
        NOT_STARTED - order is not approved by the client
        WAITING_FOR_PAYMENT - waiting for the payment by the client
        PAYMENT_COLLECED_BY_SELLER - seller has the payment
        PAYMENT_IN_ADVANCE_BY_SELLER - seller has paid to the storehouse, but
            not yet recived it from client
        PAYMENT_COLLECED_BY_STOREHOUSE - storehouse has collected the payment
    """
    NOT_STARTED = 0
    WAITING_FOR_PAYMENT = 1
    PAYMENT_COLLECED_BY_SELLER = 2
    PAYMENT_IN_ADVANCE_BY_SELLER = 3
    PAYMENT_COLLECED_BY_STOREHOUSE = 4

    _CHOICES = (
        (NOT_STARTED, _('Not started')),
        (WAITING_FOR_PAYMENT, _('Waiting for payment')),
        (PAYMENT_COLLECED_BY_SELLER, _('Payment collected by seller')),
        (PAYMENT_IN_ADVANCE_BY_SELLER, _('Payment in advance by seller')),
        (PAYMENT_COLLECED_BY_STOREHOUSE, _('Payment collected by storyhouse')),
    )

    _DICT = dict(_CHOICES)


class Order(Model):
    description = CharField(
        max_length=255,
        help_text=_('Description'))
    order_status = IntegerField(
        help_text=_('Order status'),
        choices=OrderStatus._CHOICES,
        default=OrderStatus.PENDING)
    payment_status = IntegerField(
        help_text=_('Order status'),
        choices=PaymentStatus._CHOICES,
        default=PaymentStatus.NOT_STARTED)
    discount = DecimalField(
        max_digits=10,
        decimal_places=3,
        default=0)
    contact = ForeignKey('contacts.Contact', null=True)
    when_created = DateTimeField(default=default_now, db_index=True)

    class Driver(object):

        @staticmethod
        def _viewable():
            """
            Orders which are visible by for user.
            """
            return Order.objects

        @staticmethod
        def _last_week_created():
            """
            Orders which were created in last 7 days.
            """
            week_ego = datetime.utcnow() - timedelta(days=7)
            return Order.objects.filter(when_created__gte=week_ego)

        @classmethod
        def viewable(cls):
            return cls._viewable().all()

        @classmethod
        def viewable_tab(cls):
            query = (
                cls._viewable()
                .values_list(
                    'id',
                    'order_status',
                    'payment_status',
                    'description',
                    'contact__name',
                    'contact__surname')
            )
            for row in query:
                yield OrderViewTabElement(*row)

        @classmethod
        def viewable_count(cls):
            return cls._viewable().count()

        @classmethod
        def last_week_created_count(cls):
            return cls._last_week_created().count()

        @classmethod
        def get_viewable_by_id(cls, id_):
            return cls._viewable().get(id=id_)


class OrderItem(Model):
    order = ForeignKey(Order)
    product = ForeignKey('products.Product')
    amount = IntegerField(default=1)
    price = DecimalField(max_digits=10, decimal_places=2, help_text=_('Price'))


class OrderViewTabElement(object):

    def __init__(
        self,
        id_,
        order_status,
        payment_status,
        description,
        contact__name,
        contact__surname,
    ):
        self.id = id_
        self.order_status = order_status
        self.payment_status = payment_status
        self.description = description
        self.contact__name = contact__name
        self.contact__surname = contact__surname

    @property
    def client(self):
        return '{} {}'.format(self.contact__name, self.contact__surname)

    @property
    def order_status_name(self):
        return OrderStatus._DICT[self.order_status]

    @property
    def payment_status_name(self):
        return PaymentStatus._DICT[self.payment_status]
