from django.urls import path

from .views import shop_index
from .views import groups_list
from .views import products_list
from .views import orders_list

app_name = "shopapp"

urlpatterns = [
    path("", shop_index, name="index"),
    path("groups/", groups_list, name="groups_list"),
    path("products/", products_list, name="products_list"),
    path("orders/", orders_list, name="orders_list"),
]
