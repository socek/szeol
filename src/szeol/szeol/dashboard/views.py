from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View


class DashboardHome(LoginRequiredMixin, View):

    def get(self, request):
        print(request.user)
        return HttpResponse('result')
