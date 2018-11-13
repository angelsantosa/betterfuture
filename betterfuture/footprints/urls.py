from django.urls import path

from .views import (
    item_list_view,
    item_detail_view,
    organization_list_view,
    organization_detail_view,
    pedometer_create_view,
    pet_create_view,
    donate_create_view
)

app_name = "footprints"

urlpatterns = [
    path("shop/", view=item_list_view, name="item_list"),
    path("shop/<str:pk>", view=item_detail_view, name="item_detail"),

    path("donate/", view=organization_list_view, name="org_list"),
    path("donate/<str:pk>", view=organization_detail_view, name="org_detail"),
    path("donate/create/<str:org_pk>", view=donate_create_view, name="org_create"),

    path("pedometer/", view=pedometer_create_view, name="pedometer_create"),
    path("pet/", view=pet_create_view, name="pet_create"),
]
