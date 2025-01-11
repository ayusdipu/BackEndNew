from rest_framework import serializers
from Penjualan.models import NotaPenjualan, DetailPenjualan

class NotaPenjualanSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaPenjualan
        fields = (
            'nama_outlet',
            'kode_outlet',
            'no_nota_jual',
            'no_SJ_keluar',
            'jenis_penjualan',
            'jenis_faktur',
            'nilai_nota_jual',
            'piutang_standing',
            'kantor_cabang',
            'nama_salesman',
            'status_nota',
            'status_barang',
            'tanggal_nota',
            'jatuh_tempo_nota',
            'divisi_kantor',
            'perusahaan_kantor',
        )


class DetailPenjualanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailPenjualan
        fields = (
            'no_nota_jual',
            'nama_produk',
            'kemasan_produk',
            'jumlah_order',
            'harga_jual_pcs',
            'discount_produk',
            'kode_outlet',
            'no_SJ_keluar',
            'subtotal_vol',
            'tanggal_nota',
        )