from django.core.exceptions import ValidationError


"""
The validation for only letters is to not allow any other digit
"""
def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError(
            ('%(value)s must contain only letters'),
            params={'value': value},
        )


"""
The validation of age, is for applicant for more than 9 years old
The age should be between 10 to 99
"""
def validate_age(value):
    if len(str(value)) != 2:
        raise ValidationError(
            ('%(value)s must have only two digits'),
            params={'value': value},
        )