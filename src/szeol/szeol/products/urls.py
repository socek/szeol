from django.conf.urls import url

from .views import CreateProduct


urlpatterns = [
    url(
        r'^create/$',
        CreateProduct.as_view(),
        name='products_create'),
]
