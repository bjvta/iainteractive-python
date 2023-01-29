"""Common Commands"""

from django.core.management.base import BaseCommand

from ...models import Grimorie, MagicAffinity

GRIMORIES = [
    ("Sinceridad", 1),
    ("Esperanza", 2),
    ("Amor", 3),
    ("Buena Fortuna", 4),
    ("Desesperación", 5),
]

AFFINITIES = [
    "Oscuridad",
    "Luz",
    "Fuego",
    "Agua",
    "Viento",
    "Tierra",
]


class Command(BaseCommand):
    help = "Seeders from Grimories and Magic Affinity"

    def handle(self, *args, **options):
        self.stdout.write("Starting")
        load_grimories()
        load_magic_affinity()
        self.stdout.write("Ending")


def load_grimories():
    if Grimorie.objects.count() == 0:
        for grimorie in GRIMORIES:
            data = {"name": grimorie[0], "trefoil_leaves": grimorie[1]}
            Grimorie.objects.create(**data)


def load_magic_affinity():
    if MagicAffinity.objects.count() == 0:
        for affinity in AFFINITIES:
            MagicAffinity.objects.create(name=affinity)


# to run this, we should run with make
# make seed
