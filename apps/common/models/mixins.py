from django.db import models
from django.utils.translation import ugettext as _


class CreatedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))

    class Meta:
        abstract = True


class CreatorMixin(models.Model):
    creator = models.ForeignKey('account.User', verbose_name=_('Creator'), null=True)

    class Meta:
        abstract = True


class ChangesTrackingMixin(CreatedMixin, CreatorMixin):

    class Meta:
        abstract = True