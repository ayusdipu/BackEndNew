from rest_framework import serializers
from Salesman.models import TugasSalesman, TargetSalesman

class TugasSalesmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TugasSalesman
        fields = (
            'nama_sales',
            'timestamp',
            'tugas_diberikan',
            'hasil_tugas',
            'keterangan',
        )

class TargetSalesmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetSalesman
        fields = (
            'nama_sales',
            'target_minimum',
            'target_incentive',
        )