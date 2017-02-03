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
)
