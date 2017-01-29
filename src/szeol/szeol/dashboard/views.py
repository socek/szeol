from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render


class DashboardHome(LoginRequiredMixin, View):

    template_name = 'szeol/dashboard.jinja2'

    def get(self, request):
        return render(request, self.template_name)
