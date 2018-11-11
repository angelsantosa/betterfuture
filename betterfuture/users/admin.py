from django.contrib import admin

from .models import User, UserToken, UserCo2, UserFootPrint

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
admin.site.register(User, UserAdmin)

class UserTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'tokens')
admin.site.register(UserToken, UserTokenAdmin)

class UserCo2Admin(admin.ModelAdmin):
    list_display = ('user', 'food_co2', 'housing_co2', 'transportation_co2', 'co2_owed', 'co2_paid')
admin.site.register(UserCo2, UserCo2Admin)

class UserFootPrintAdmin(admin.ModelAdmin):
    list_display = ('user', 'value', 'footprint')
admin.site.register(UserFootPrint, UserFootPrintAdmin)

