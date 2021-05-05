from rest_framework import serializers
from . models import CSVdata

class CSVdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVdata
        fields = '__all__'