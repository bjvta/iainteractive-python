"""Common Serializers"""

from rest_framework import serializers

from .models import Applicant


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        exclude = ("grimorie",)

    def create(self, validated_data):
        return Applicant.objects.create(**validated_data)

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
