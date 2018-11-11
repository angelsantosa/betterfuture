from django.db import models
from django.contrib.auth.models import AbstractUser

from shortuuidfield import ShortUUIDField

from betterfuture.footprints.models import FootPrint
# Create your models here.

class User(AbstractUser):
    uuid = ShortUUIDField(primary_key=True)

    def __str__(self):
        return self.email

class UserToken(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)
    tokens = models.DecimalField('Tokens', max_digits=19, decimal_places=10)

    def __str__(self):
        return '{} tokens for User: {}'.format(self.tokens, self.user)

class UserCo2(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)
    
    FOOD_QUANTITY_NEVER = 0
    FOOD_QUANTITY_ALMOST_NEVER = 2.88
    FOOD_QUANTITY_FREQUENTLY = 5.76
    FOOD_QUANTITY_VERY_FREQUENTLY = 11.62

    FOOD_QUANTITY_VALUES = (
        (FOOD_QUANTITY_NEVER, 'Never'),
        (FOOD_QUANTITY_ALMOST_NEVER, 'Almost never'),
        (FOOD_QUANTITY_FREQUENTLY, 'Frequently'),
        (FOOD_QUANTITY_VERY_FREQUENTLY, 'Very frequently'),
    )

    HOUSING_FREE_NRW = 1
    HOUSING_FREE_RW = 3
    HOUSING_MULTI_APAR = 5
    HOUSING_DUPLEX = 7
    HOUSING_LUXURY = 10

    HOUSING_VALUES = (
        (HOUSING_FREE_NRW,'Freestanding NRW'),
        (HOUSING_FREE_RW,'Freestanding RW'),
        (HOUSING_MULTI_APAR, 'Multistore aparment'),
        (HOUSING_DUPLEX, 'Duplex row house'),
        (HOUSING_LUXURY, 'Luxury condominum'),
    )

    food_quantity = models.FloatField('Food quantity', choices=FOOD_QUANTITY_VALUES, default=FOOD_QUANTITY_NEVER)
    housing_quantity_dict = models.PositiveIntegerField('Housing quantity option', choices=HOUSING_VALUES, default=HOUSING_FREE_NRW)
    housing_open = models.PositiveIntegerField('House quantity open')

    km_travel_quantity = models.FloatField('Km travel')
    fuel_economy_quantity = models.FloatField('Fuel economy km/lts')
    
    food_co2 = models.FloatField('Food CO2', blank=True)
    housing_co2 = models.FloatField('Housing CO2', blank=True)
    transportation_co2 = models.FloatField('Transportation CO2', blank=True)
    
    co2_owed = models.FloatField('Owed CO2', blank=True)
    co2_paid = models.FloatField('Paid CO2', blank=True)

    def __str__(self):
        return 'Diagnostic for user {}'.format(self.user)

class UserFootPrint(models.Model):
    uuid = ShortUUIDField(primary_key=True)
    footprint = models.ForeignKey(FootPrint, on_delete=models.CASCADE)
    value = models.PositiveIntegerField('Generic value')
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return 'FootPrint ({}) movement for User: {}'.format(self.footprint, self.user)