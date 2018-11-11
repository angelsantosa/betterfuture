from django.urls import path

from .views import (
    user_dashboard_view,
    user_diagnostic_view
)

app_name = "users"
urlpatterns = [
    path("", view=user_dashboard_view, name="dashboard"),
    path("diagnostic/", view=user_diagnostic_view, name="diagnostic"),
]
