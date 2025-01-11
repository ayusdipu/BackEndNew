# produk/serializers.py

from rest_framework import serializers
from SuratJalanKeluar.models import SJKeluar, DetailSJKeluar, DetailLokasiKeluarProduk

class SJKeluarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SJKeluar
        fields = [
            'no_nota_keluar',
            'no_SJ_keluar',
            'no_kendaraan',
            'nama_pengirim',
            'tanggal_kirim',
            'gudang_awal',
            'tujuan_kirim',
            'jenis_sj_keluar',
            'status_kiriman',
            'modal_SJ_keluar',
        ]

class DetailSJKeluarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailSJKeluar
        fields = [
            'nama_produk',
            'kode_produk',
            'jumlah_order',
            'kemasan_produk',
            'no_nota_keluar',
            'no_SJ_keluar',
            'harga_beli_produk',
        ]

class DetailLokasiKeluarProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailLokasiKeluarProduk
        fields = [
            'no_nota_keluar',
            'no_SJ_keluar',
            'kode_keluar_produk',
            'nama_produk',
            'kode_produk',
            'jumlah_produk',
            'harga_modal_produk',
            'kemasan_produk',
            'gudang_awal',
            'lokasi_produk',
        ]
