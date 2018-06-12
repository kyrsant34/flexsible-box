from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.common.models import ChangesTrackingMixin, CreatedMixin

from .common import Credential, Address, Contact


class NaturalPerson(ChangesTrackingMixin):

    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    birth_date = models.DateField()
    credential = GenericRelation(Credential)
    address = GenericRelation(Address)
    contact = GenericRelation(Contact)


class NaturalPersonGroup(ChangesTrackingMixin):
    natural_persons = models.ManyToManyField(NaturalPerson)


class LegalPerson(ChangesTrackingMixin):
    title = models.CharField(max_length=255)


class Person(CreatedMixin):
    legal_person = models.OneToOneField(LegalPerson, null=True, blank=True)
    natural_person = models.OneToOneField(NaturalPerson, null=True, blank=True)

    ONLY_ONE_OF_FIELDS = ('natural_person', 'legal_person')

    def get_concrete_person(self):
        for field in self.ONLY_ONE_OF_FIELDS:
            val = getattr(self, field, None)
            if val:
                return val

    def save(self, *args, **kwargs):
        objects = [field for field in self.ONLY_ONE_OF_FIELDS if getattr(self, field, None)]
        # только один обязательный объект; сделано через filter т.к. позже будет больше 2 объектов
        assert len(objects) == 1
        super().save(*args, **kwargs)

    def __str__(self):
        person = self.get_concrete_person()
        if not person:
            person = super().__str__()
        return person


__all__ = ['Person', 'NaturalPerson', 'LegalPerson']
