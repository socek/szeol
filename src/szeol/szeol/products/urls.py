from django.conf.urls import url

from .views import CreateProduct
from .views import ListProduct


urlpatterns = [
    url(
        r'^create/$',
        CreateProduct.as_view(),
        name='products_create'),
    url(
        r'^$',
        ListProduct.as_view(),
        name='products_list')
]
