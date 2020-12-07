from rest_framework import serializers
from .models import Joblisting

class JoblistingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Joblisting
        fields=('id','firstname','lastname','email','qualifications','jobs')
