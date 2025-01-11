# produk/serializers.py

from rest_framework import serializers
from SuratJalanMasuk.models import SJMasuk, DetailSJMasuk

class SJMasukSerializer(serializers.ModelSerializer):
    class Meta:
        model = SJMasuk
        fields = [
            'no_SJ_masuk',
            'no_nota_masuk',
            'no_kendaraan',
            'nama_pembawa',
            'asal_kiriman',
            'waktu_masuk',
            'gudang_cabang',
            'nama_penerima',
            'jenis_sj_masuk',
            'modal_SJ_masuk',
        ]

class DetailSJMasukSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailSJMasuk
        fields = [
            'no_SJ_masuk',
            'no_nota_masuk',
            'nama_produk',
            'kode_produk',
            'jumlah_order',
            'kemasan_produk',
            'harga_beli_pcs',
        ]
