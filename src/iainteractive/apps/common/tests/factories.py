"""Common Test Factories module"""

# Other
from datetime import date

import factory

# Common
from ..models import *


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    name = "Event 1"
    date = date(2020, 7, 1)


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = "Name"
    telephone = "234567"
    is_major = True
    email = factory.Sequence(lambda n: "person{0}@example.com")


class MembershipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Membership

    event = factory.SubFactory(EventFactory)
    customer = factory.SubFactory(CustomerFactory)
    date_joined = date(2020, 7, 1)
    pin_invitation = factory.Sequence(lambda n: "{0}")
