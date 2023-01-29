"""Common Models module"""


from django.db import models
from iainteractive.apps.common.validators import validate_age, validate_only_letters


"""
Grimorie is the section where an Applicant will be added
"""
class Grimorie(models.Model):
    name = models.CharField(max_length=40)
    trefoil_leaves = models.SmallIntegerField()

    def __str__(self):
        return f"{self.name} - Trébol de {self.trefoil_leaves} hoja(s)"


"""
Magic Affinity is like an attribute where it can be selected
"""
class MagicAffinity(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"


"""
Applicant is a candidate for the magic academy where import data will be stored,
It has a directly relation with Magic Affinity and Grimorie
"""
class Applicant(models.Model):
    first_name = models.CharField(max_length=20, validators=[validate_only_letters])
    last_name = models.CharField(max_length=20, validators=[validate_only_letters])
    identification = models.CharField(max_length=10)
    age = models.SmallIntegerField(validators=[validate_age])
    magic_affinity = models.ForeignKey(MagicAffinity, on_delete=models.CASCADE)
    grimorie = models.ForeignKey(Grimorie, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.magic_affinity}"