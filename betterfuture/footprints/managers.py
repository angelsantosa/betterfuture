from django.db import models


class FootPrintsManager(models.Manager):
    PET_FOOTPRINT_NAME = 'PET'
    PEDOMETER_FOOTPRINT_NAME = 'Pedometer'


    def pedometer(self):
        try:
            return self.get(name=self.PEDOMETER_FOOTPRINT_NAME)
        except self.model.DoesNotExist:
            raise ValueError('No hay ninguna configuración para {}'.format(self.PEDOMETER_FOOTPRINT_NAME))

    def pet(self):
        try:
            return self.get(name=self.PET_FOOTPRINT_NAME)
        except self.model.DoesNotExist:
            raise ValueError('No hay ninguna configuración para {}'.format(self.PET_FOOTPRINT_NAME))
