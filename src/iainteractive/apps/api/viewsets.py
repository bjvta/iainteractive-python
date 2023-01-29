"""Api Viewsets"""

from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from iainteractive.apps.common.models import Applicant
from iainteractive.apps.common.serializers import ApplicantSerializer


class ApplicantViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving applicants.
    """

    def list(self, request):
        queryset = Applicant.objects.all()
        serializer = ApplicantSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ApplicantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Applicant.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ApplicantSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass
