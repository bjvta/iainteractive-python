# Generated by Django 4.1.5 on 2023-01-29 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="applicant",
            old_name="Grimorie",
            new_name="grimorie",
        ),
    ]
