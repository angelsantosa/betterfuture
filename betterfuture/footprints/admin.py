from django.contrib import admin

from .models import FootPrint, Organization, Item

# Register your models here.
class FootPrintAdmin(admin.ModelAdmin):
    list_display = ('name', 'co2_multiplicative', 'transaction_type', 'fp_type')
admin.site.register(FootPrint, FootPrintAdmin)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'eth_address')
admin.site.register(Organization, OrganizationAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'token_price')
admin.site.register(Item, ItemAdmin)