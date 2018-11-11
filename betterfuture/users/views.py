from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy

from .utils import LoginRequired, AbstractUserLoginTest
from .models import UserFootPrint, UserCo2

# Create your views here.
class UserDashboardView(AbstractUserLoginTest, ListView):
    
    template_name = 'users/dashboard.html'
    context_object_name = 'fprints'
    no_permission_url = reverse_lazy('users:diagnostic')
    raise_exception = False

    def get_queryset(self):
        user = self.request.user
        user_footprints = UserFootPrint.objects.filter(user=user)
        return user_footprints

    def test_func(self):
        user = self.request.user
        user_co2 = user.userco2.co2_owed
        return True if user_co2 else False

user_dashboard_view = UserDashboardView.as_view()

class UserDiagnosticView(AbstractUserLoginTest, UpdateView):

    template_name = 'users/update_diagnositc.html'
    raise_exception = False
    no_permission_url = reverse_lazy('users:dashboard')
    success_url = reverse_lazy('users:dashboard')
    model = UserCo2
    fields = ['food_quantity', 'housing_quantity_dict', 'housing_open', 'km_travel_quantity', 'fuel_economy_quantity']
    
    def get_object(self):
        user = self.request.user
        user_co2 = user.userco2
        return user_co2

    def test_func(self):
        user = self.request.user
        user_co2 = user.userco2.co2_owed
        return False if user_co2 else True

user_diagnostic_view = UserDiagnosticView.as_view()