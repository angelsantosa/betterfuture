from django.db import models

from shortuuidfield import ShortUUIDField
# Create your models here.

class FootPrint(models.Model):

    TRANSACTION_EGRESS_CODE = 'E'
    TRANSACTION_INCOME_CODE = 'I'

    TRANSACTION_TYPE_CODES = (
        (TRANSACTION_EGRESS_CODE, 'Egress'),
        (TRANSACTION_INCOME_CODE, 'Income'),
    )

    FOOTPRINT_ITEM_CODE = 'I'
    FOOTPRINT_DONATION_CODE = 'D'
    FOOTPRINT_USER_ACTION_CODE = 'U'

    FOOTPRINT_TYPE_CODES = (
        (FOOTPRINT_ITEM_CODE, 'Item'),
        (FOOTPRINT_DONATION_CODE, 'Donation'),
        (FOOTPRINT_USER_ACTION_CODE, 'Action'),
    )

    uuid = ShortUUIDField(primary_key=True)
    name = models.CharField('Name of FootPrint', max_length=256)
    co2_multiplicative = models.PositiveIntegerField('CO2 Multiplicative', default=10)
    transaction_type = models.CharField('Type of transaction', max_length=1, choices=TRANSACTION_TYPE_CODES, default=TRANSACTION_EGRESS_CODE)
    fp_type = models.CharField('Type of footprint', max_length=1, choices=FOOTPRINT_TYPE_CODES, default=FOOTPRINT_USER_ACTION_CODE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE, null=True, blank=True)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Organization(models.Model):
    uuid = ShortUUIDField(primary_key=True)
    name = models.CharField("Organization's name", max_length=256)
    eth_address = models.CharField('Core ETH address', max_length=42)
    picture = models.ImageField('Image')

    def __str__(self):
        return self.name

class Item(models.Model):
    uuid = ShortUUIDField(primary_key=True)
    name = models.CharField("Item's name", max_length=256)
    token_price = models.DecimalField('Price in tokens', max_digits=19, decimal_places=10)
    picture = models.ImageField('Image')
    
    def __str__(self):
        return self.name