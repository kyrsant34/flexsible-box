from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext as _
from mptt import models as mptt_models

from apps.common.models import CreatedMixin
from .managers import UserManager


class Department(mptt_models.MPTTModel):
    title = models.CharField(max_length=255)
    parent = mptt_models.TreeForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.title


class PermissionMixin(models.Model):

    is_superuser = models.BooleanField(default=False)

    def has_module_perms(self, app_label=None):
        if self.is_active and self.is_superuser:
            return True
        return False

    def has_perm(self, perm=None, obj=None):
        if self.is_active and self.is_superuser:
            return True
        return False

    class Meta:
        abstract = True


class User(CreatedMixin, PermissionMixin, AbstractBaseUser):

    email = models.EmailField(_('email address'), blank=True, unique=True)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    department = models.ForeignKey(Department, related_name='users')
    person = models.ForeignKey('client.Person', blank=True, null=True, related_name='users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['department']

    objects = UserManager()

    def get_short_name(self):
        return "{}".format(self.email)

    def get_full_name(self):
        return "{}".format(self.email)
