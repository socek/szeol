from django.conf.urls import url

from .views import DashboardHome


urlpatterns = [
    url(
        r'^$',
        DashboardHome.as_view(),
        name='dashboard_home'),
]
