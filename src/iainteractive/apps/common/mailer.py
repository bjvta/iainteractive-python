"""Common Mailer Module"""

# Django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


class Mailer:
    @staticmethod
    def send_dummy():
        text_content = 'This is a email'
        subject = 'My subject'
        from_email = 'accounting@agiletestingdays.us'
        to_email = ['bjvtamayo78@gmail.com']
        confirmation = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        confirmation.send()