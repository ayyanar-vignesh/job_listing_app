from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JoblistingSerializer
from .models import Joblisting


class JoblistingViewSet(viewsets.ModelViewSet):
    queryset = Joblisting.objects.all().order_by('id')
    serializer_class = JoblistingSerializer

