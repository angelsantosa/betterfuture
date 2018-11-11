from django.db import models
from django.contrib.auth.models import AbstractUser

from shortuuidfield import ShortUUIDField

from betterfuture.footprints.models import FootPrint
# Create your models here.

class User(AbstractUser):
    uuid = ShortUUIDField(primary_key=True)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        try:                
            UserCo2.objects.get(user=self)
        except UserCo2.DoesNotExist:
            self.create_userco2()
        try:                
            UserToken.objects.get(user=self)
        except UserToken.DoesNotExist:
            self.create_usertoken()

    def create_userco2(self):
        userco2 = UserCo2(user=self)
        userco2.save()

    def create_usertoken(self):
        usertoken = UserToken(user=self)
        usertoken.save()

    def __str__(self):
        return self.email

class UserToken(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)
    tokens = models.FloatField('Tokens', default=10)

    def income(self, tokens):
        self.tokens += tokens
        self.save()
        return self.tokens

    def egress(self, tokens):
        if tokens > self.tokens:
            return False
        else:
            self.tokens = self.tokens - tokens
            self.save()
            return self.tokens

    def __str__(self):
        return '{} tokens for User: {}'.format(self.tokens, self.user)

class UserCo2(models.Model):
    
    FOOD_CONST = 19

    HOUSING_CONST_1 = 5.93
    HOUSING_CONST_2 = 31
    HOUSING_CONST_3 = 1.486
    HOUSING_CONST_4 = 2204
    HOUSING_CONST_5 = 907.185

    TRAVEL_CONST_1 = 19.36
    TRAVEL_CONST_2 = 2204.6
    TRAVEL_CONST_3 = 1000

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
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)

    food_quantity = models.FloatField('Food quantity', choices=FOOD_QUANTITY_VALUES, default=FOOD_QUANTITY_NEVER, blank=True)
    housing_quantity_dict = models.PositiveIntegerField('Housing quantity option', choices=HOUSING_VALUES, default=HOUSING_FREE_NRW, blank=True)
    housing_open = models.PositiveIntegerField('House quantity open', blank=True, null=True)

    km_travel_quantity = models.FloatField('Km travel', blank=True, null=True)
    fuel_economy_quantity = models.FloatField('Fuel economy km/lts', blank=True, null=True)
    
    food_co2 = models.FloatField('Food CO2', blank=True, null=True)
    housing_co2 = models.FloatField('Housing CO2', blank=True, null=True)
    transportation_co2 = models.FloatField('Transportation CO2', blank=True, null=True)
    
    co2_owed = models.FloatField('Owed CO2', default=0)
    co2_paid = models.FloatField('Paid CO2', default=0)

    def save(self, *args, **kwargs):
        super(UserCo2, self).save(*args, **kwargs)
        fields = [
            self.food_quantity,
            self.housing_open,
            self.km_travel_quantity,
            self.fuel_economy_quantity,
        ]
        if all(fields) and not self.co2_owed:
            self.generate_owed_co2()
    
    def generate_owed_co2(self):
        self.food_co2 = self.food_quantity * self.FOOD_CONST

        first = self.HOUSING_CONST_1/self.housing_open
        multi = first * self.HOUSING_CONST_2 * self.HOUSING_CONST_3
        div_big = multi / self.HOUSING_CONST_4
        div_sec_big = div_big / self.HOUSING_CONST_5

        self.housing_co2 = div_sec_big

        t_div = self.km_travel_quantity / self.fuel_economy_quantity
        t_mul = t_div * self.TRAVEL_CONST_1
        t_sec_div = t_div / self.TRAVEL_CONST_2
        t_mult_div = t_sec_div * self.TRAVEL_CONST_3

        self.transportation_co2 = t_mult_div

        self.co2_owed = sum([self.food_co2,  self.housing_co2, self.transportation_co2])
        self.save()

    @property
    def get_co2(self):
        return self.co2_owed - self.co2_paid
    
    def __str__(self):
        return 'Diagnostic for user {}'.format(self.user)

class UserFootPrint(models.Model):
    uuid = ShortUUIDField(primary_key=True)
    footprint = models.ForeignKey(FootPrint, on_delete=models.CASCADE)
    value = models.PositiveIntegerField('Generic value')
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(UserFootPrint, self).save(*args, **kwargs)
        co2 = self.footprint.co2_multiplicative * self.value
        
        self.user.userco2.co2_paid += co2
        self.user.usertoken.tokens += co2

        self.user.userco2.save()
        self.user.usertoken.save()

    def __str__(self):
        return 'FootPrint ({}) movement for User: {}'.format(self.footprint, self.user)