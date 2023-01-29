"""Common TestServices module"""

# Django
from django.core import mail
from django.test import TestCase

# Common
from ..forms import RegistrationForm
from ..services import *
from .factories import *


class TestCurrentEvent(TestCase):
    def test_return_the_current(self):
        event = EventFactory(default=True)
        event_id = CurrentEventService.get_id()
        self.assertEqual(event_id, event.pk)

    def test_return_the_first_event_when_there_are_many_default(self):
        event_1 = EventFactory(default=True)
        EventFactory(default=True)
        event_id = CurrentEventService.get_id()
        self.assertEqual(event_id, event_1.pk)

    def test_return_first_one_if_there_is_no_any_default(self):
        event_1 = EventFactory()
        EventFactory()
        event_id = CurrentEventService.get_id()
        self.assertEqual(event_id, event_1.pk)

    def test_return_empty_if_there_is_no_event(self):
        event_id = CurrentEventService.get_id()
        self.assertEqual(event_id, '')


class TestRegistrationService(TestCase):

    def setUp(self):
        self.event = EventFactory(default=True)

    def test_best_case(self):
        initial_data = {
            'name': 'Brandon',
            'telephone': '2134567',
            'email': 'email1@gmail.com',
            'is_major': 'true',
            'birth': '02-03-2014',
            'city': '01',
            'event_id': self.event.pk
        }
        form = RegistrationForm(data=initial_data)
        service = RegistrationService(form=form)
        service.call()
        self.assertEqual(len(mail.outbox), 1)
        self.assertNotEqual(Customer.objects.count(), 0)
        self.assertNotEqual(Membership.objects.count(), 0)

    def test_customer_exist_in_the_event(self):
        customer = CustomerFactory()
        MembershipFactory(event=self.event, customer=customer)
        initial_data = {
            'name': customer.name,
            'telephone': customer.telephone,
            'email': customer.email,
            'is_major': 'true',
            'birth': '02-03-2020',
            'city': '01',
            'event_id': self.event.pk
        }
        form = RegistrationForm(data=initial_data)
        service = RegistrationService(form=form)
        with self.assertRaises(CustomerAlreadyInEventException):
            service.call()

    def test_customer_exist_but_is_new_event(self):
        customer = CustomerFactory()
        initial_data = {
            'name': customer.name,
            'telephone': customer.telephone,
            'email': customer.email,
            'is_major': 'true',
            'birth': '',
            'city': '01',
            'event_id': self.event.pk
        }
        form = RegistrationForm(data=initial_data)
        service = RegistrationService(form=form)
        service.call()
        self.assertEqual(len(mail.outbox), 1)
        self.assertNotEqual(Customer.objects.count(), 0)
        self.assertNotEqual(Membership.objects.count(), 0)


class TestGenerateUniqueMembershipPin(TestCase):
    def test_best_case(self):
        pin = get_random_string(5)
        MembershipFactory(pin_invitation=pin)
        new_pin = GenerateUniqueMembershipPin.call()
        self.assertNotEqual(pin, new_pin)

class TestCheckEventPin(TestCase):
    def test_best_case(self):
        pin = get_random_string(5)
        MembershipFactory(pin_invitation=pin)
        service = CheckEventPin(pin=pin)
        result = service.call()
        self.assertTrue(result)

    def test_pin_doesnot_exist(self):
        pin = get_random_string(5)
        service = CheckEventPin(pin=pin)
        result = service.call()
        self.assertFalse(result)