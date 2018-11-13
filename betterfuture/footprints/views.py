from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from betterfuture.users.utils import LoginRequired, AbstractUserLoginTest
from betterfuture.users.models import UserFootPrint

from .models import Item, Organization, FootPrint

# Create your views here.
class ItemListView(LoginRequired, ListView):
    template_name = 'footprints/item_list.html'
    model = Item
    context_object_name = 'item'

item_list_view = ItemListView.as_view()

class ItemDetailView(LoginRequired, DetailView):

    template_name = 'footprints/item_detail.html'
    model = Item
    context_object_name = 'item'
    
item_detail_view = ItemDetailView.as_view()


class OrganizationListView(LoginRequired, ListView):
    template_name = 'footprints/org_list.html'
    model = Organization
    context_object_name = 'org'

organization_list_view = OrganizationListView.as_view()

class OrganizationDetailView(LoginRequired, DetailView):

    template_name = 'footprints/org_detail.html'
    model = Organization
    context_object_name = 'org'

organization_detail_view = OrganizationDetailView.as_view()

class PetCreateView(LoginRequired, CreateView):

    template_name = 'footprints/pet_create.html'
    model = UserFootPrint
    fields = ['value']
    success_url = reverse_lazy('users:dashboard')
    def form_valid(self, form):
        user = self.request.user
        pet_footprint = FootPrint.objects.pet()
        
        self.object = form.save(commit=False)
        self.object.user = user
        self.object.footprint = pet_footprint
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

pet_create_view = PetCreateView.as_view()

class PedometerCreateView(LoginRequired, CreateView):

    template_name = 'footprints/pedometer_create.html'
    model = UserFootPrint
    fields = ['value']
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        user = self.request.user
        pedometer_footprint = FootPrint.objects.pedometer()

        self.object = form.save(commit=False)
        self.object.user = user
        self.object.footprint = pedometer_footprint
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

pedometer_create_view = PedometerCreateView.as_view()

class DonateCreateView(LoginRequired, CreateView):

    template_name = 'footprints/donate_create.html'
    model = UserFootPrint
    fields = ['value']
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        kwargs = self.kwargs
        org_pk = kwargs["org_pk"]
        org = FootPrint.objects.get(organization=org_pk)
        user = self.request.user

        self.object = form.save(commit=False)
        self.object.user = user
        self.object.footprint = org
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

donate_create_view = DonateCreateView.as_view()