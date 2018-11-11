from django.db import models

from shortuuidfield import ShortUUIDField

from betterfuture.users.models import User, UserFootPrint
# Create your models here.

class Token(models.Model):
    eth_address = models.CharField('Core ETH address', max_length=42)
    eth_per_token = models.DecimalField('ETH per Token', max_digits=19, decimal_places=10)

    def __str__(self):
        return self.eth_address

class TokenTransactions(models.Model):
    uuid = ShortUUIDField(primary_key=True)
    address_from = models.CharField('ETH address FROM', max_length=42, blank=True)
    address_to = models.CharField('ETH address TO', max_length=42, blank=True)
    contract = models.CharField('Contract address', max_length=42, blank=True)
    gas = models.DecimalField('Gas', max_digits=19, decimal_places=10)
    eth = models.DecimalField('Sent ETH', max_digits=19, decimal_places=10)
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)

    def __str__(self):
        return 'Blockchain transaction for {}'.format(self.transaction)

class Transaction(models.Model):
    uuid = ShortUUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_footprint = models.ForeignKey(UserFootPrint, on_delete=models.CASCADE)
    tokens_value = models.DecimalField('Tokens', max_digits=19, decimal_places=10) 

    def __str__(self):
        return 'Internal transaction for User: {}, Footprint: {}'.format(self.user, self.user_footprint.footprint)
