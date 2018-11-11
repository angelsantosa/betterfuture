from django.contrib import admin

from .models import Token, TokenTransactions, Transaction

# Register your models here.
class TokenAdmin(admin.ModelAdmin):
    list_display = ('eth_address', 'eth_per_token')
admin.site.register(Token, TokenAdmin)

class TokenTransactionsAdmin(admin.ModelAdmin):
    list_display = ('address_from', 'address_to', 'contract', 'gas', 'eth', 'transaction')
admin.site.register(TokenTransactions, TokenTransactionsAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_footprint', 'tokens_value')
admin.site.register(Transaction, TransactionAdmin)