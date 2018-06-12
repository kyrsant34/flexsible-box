from django.contrib.contenttypes import fields as contenttype_fields
from django.db import models

from apps.common.models import ChangesTrackingMixin
from apps.handbooks.models import CarMark, CarModel

from .common import Credential


class Car(ChangesTrackingMixin):
    car_mark = models.ForeignKey(CarMark)
    car_model = models.ForeignKey(CarModel)
    credential = contenttype_fields.GenericRelation(Credential)
    engine_power = models.PositiveIntegerField()
    engine_power_kilowatt = models.FloatField()
    manufacturing_date = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    number_plate = models.CharField(max_length=9)
    vin_number = models.CharField(max_length=17)
