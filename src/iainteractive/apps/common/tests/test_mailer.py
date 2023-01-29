"""Common TestMailer Module"""

# Django
from django.core import mail
from django.test import TestCase

# Common
from .factories import MembershipFactory
from ..mailer import Mailer


class TestMailer(TestCase):

    def test_send_dummy(self):
        Mailer.send_dummy()
        self.assertEqual(len(mail.outbox), 1)

    def test_send_dummy_with_template(self):
        Mailer.send_dummy_with_template()
        self.assertEqual(len(mail.outbox), 1)

    def test_send_registration(self):
        membership = MembershipFactory()
        customer = membership.customer
        Mailer.send_email_to_customer(membership=membership, customer=customer)
        self.assertEqual(len(mail.outbox), 1)
