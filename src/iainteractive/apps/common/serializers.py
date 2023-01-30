"""Common Serializers"""

from rest_framework import serializers
import random
from .models import Applicant, Grimorie
from drf_yasg import openapi


class EmailMessageField(serializers.JSONField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_OBJECT,
            "title": "Email",
            "properties": {
                "subject": openapi.Schema(
                    title="Email subject",
                    type=openapi.TYPE_STRING,
                ),
                "body": openapi.Schema(
                    title="Email body",
                    type=openapi.TYPE_STRING,
                ),
            },
            "required": ["subject", "body"],
         }


class GrimorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grimorie
        fields = '__all__'



class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        exclude = ("grimorie",)

    def create(self, validated_data):
        return Applicant.objects.create(**validated_data)

        # validated_data['grimorie'] = random.choice([x for x in Grimorie.objects.all()])

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.identification = validated_data.get(
            "identification", instance.identification
        )
        instance.age = validated_data.get("age", instance.age)
        instance.magic_affinity = validated_data.get(
            "magic_affinity", instance.magic_affinity
        )
        instance.save()
        return instance
