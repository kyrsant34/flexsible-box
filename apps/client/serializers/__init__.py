from .car import CarSerializer
from .common import ContactSerializer, AddressSerializer, QueryAddressSerializer, CredentialSerializer
from .insurance import InsuredObjectSerializer, InsuredObjectParameterSerializer, InsuredObjectTypeSerializer
from .person import LegalPersonSerializer, NaturalPersonSerializer, PersonSerializer


__all__ = ['CarSerializer', 'InsuredObjectSerializer', 'InsuredObjectParameterSerializer', 'PersonSerializer',
           'InsuredObjectTypeSerializer', 'LegalPersonSerializer', 'NaturalPersonSerializer']
