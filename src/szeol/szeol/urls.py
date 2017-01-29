from django.conf.urls import include
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(
        r'^accounts/login/$',
        auth_views.login,
        {'template_name': 'localauth/login.jinja2'},
        name='login'),

    url(
        r'^',
        include('szeol.dashboard.urls'))
]
