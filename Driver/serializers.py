from rest_framework import serializers
from Driver.models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = (
            'no_kendaraan',
            'nama_supir',
            'no_telepon_supir',
            'jenis_kendaraan',
            'merek_kendaraan',
            'status_kendaraan'
        )