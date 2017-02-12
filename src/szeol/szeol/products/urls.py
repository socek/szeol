from django.conf.urls import url

from .views import CreateProduct
from .views import EditProduct
from .views import ListProduct


urlpatterns = [
    url(
        r'^create/$',
        CreateProduct.as_view(),
        name='products_create'),
    url(
        r'^$',
        ListProduct.as_view(),
        name='products_list'),
    url(
        r'^edit/(?P<product_id>[0-9]+)/$',
        EditProduct.as_view(),
        name='products_edit'),
]
