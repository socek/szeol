from django.conf.urls import url

from .views import DashboardHome
from .views import StatisticsApi


urlpatterns = [
    url(
        r'^$',
        DashboardHome.as_view(),
        name='dashboard_home'),
    url(
        r'^stats$',
        StatisticsApi.as_view(),
        name='stats_api')
]
