from django.urls import reverse
from django.utils.translation import ugettext as _

MENU = (
    dict(
        id='dashboard',
        name=_('Dashboard'),
        icon='fa-home',
        elements=(
            dict(
                id='dashboard_home',
                name=_('Statistics'),
                url=lambda: reverse('dashboard_home'),
            ),
        )
    ),
    dict(
        id='products',
        name=_('Products'),
        icon='fa-glass',
        elements=(
            dict(
                id='products_create',
                name=_('Add'),
                url=lambda: reverse('products_create'),
            ),
            dict(
                id='products_list',
                name=_('List'),
                url=lambda: reverse('products_list'),
            ),
        )
    ),
    dict(
        id='contacts',
        name=_('Contacts'),
        icon='fa-users',
        elements=(
            dict(
                id='contacts_create',
                name=_('Add'),
                url=lambda: reverse('contacts_create'),
            ),
            dict(
                id='contacts_list',
                name=_('List'),
                url=lambda: reverse('contacts_list'),
            ),
        )
    ),
    dict(
        id='orders',
        name=_('Orders'),
        icon='fa-shopping-cart',
        elements=(
            dict(
                id='orders_list',
                name=_('List'),
                url=lambda: reverse('orders_list'),
            ),
        )
    ),
)
