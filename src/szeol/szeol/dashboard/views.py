from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from szeol.main.views import contextwrapper


class DashboardHome(LoginRequiredMixin, View):

    MENU_ID = 'dashboard_home'
    TEMPLATE_NAME = 'szeol/dashboard.html'

    @contextwrapper
    def get(self, request, context, matchdict):
        pass
