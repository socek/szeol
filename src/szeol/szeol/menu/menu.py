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
        name=_('Proucts'),
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
)
