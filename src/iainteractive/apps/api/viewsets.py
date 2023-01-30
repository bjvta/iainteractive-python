"""Api Viewsets"""

from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from iainteractive.apps.common.models import Applicant, Grimorie
from iainteractive.apps.common.serializers import ApplicantSerializer, GrimorieSerializer


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

    def destroy(self, request, pk=None):
        pass


    @action(detail=True, methods=['POST'], name='Attach meta items ids')
    def update_status(self, request, pk=None):
        """Does something on single item."""
        queryset = Applicant.objects.get(pk=pk)
        serializer = self.get_serializer(queryset, many=False)
        # request.data
        return Response(serializer.data)



class GrimoriesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Grimorie.objects.all()
        serializer = GrimorieSerializer(queryset, many=True)
        return Response(serializer.data)