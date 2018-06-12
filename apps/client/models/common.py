from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from apps.handbooks.models import CredentialType, AttachmentType, ContactType, AddressType
from apps.common.models import ChangesTrackingMixin


class Attachment(ChangesTrackingMixin):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    file = models.FileField()
    attachment_type = models.ForeignKey(AttachmentType)
    description = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=255)


class Credential(ChangesTrackingMixin):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    number = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    credential_type = models.ForeignKey(CredentialType)
    attachment = GenericRelation(Attachment)
    issue_point = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiration_date = models.DateField()


class Contact(ChangesTrackingMixin):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    contact_type = models.ForeignKey(ContactType)
    data = models.CharField(max_length=255)


class Address(ChangesTrackingMixin):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    address_type = models.ForeignKey(AddressType)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    flat = models.CharField(max_length=255)
    kladr = models.CharField(max_length=255)


__all__ = ['Address', 'Attachment', 'Contact', 'Credential']
