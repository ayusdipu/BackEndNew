from rest_framework import serializers
from Pembelian.models import NotaPembelian, DetailPembelian

class NotaPembelianSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaPembelian
        fields = (
            'no_nota_beli',
            'no_SJ_masuk',
            'supplier',
            'gudang_cabang',
            'faktur_atau_tidak',
            'hutang_standing',
            'diorder_oleh',
            'nilai_nota_beli',
            'jatuh_tempo_beli',
            'status_nota_beli',
            'status_barang_beli',
            'divisi_kantor',
            'perusahaan_kantor',
            'total_volume_nota',
            'cluster_pembeli',
        )


class DetailPembelianSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailPembelian
        fields = (
            'no_nota_beli',
            'no_SJ_masuk',
            'nama_produk',
            'kemasan_produk',
            'jumlah_order_beli',
            'harga_beli_pcs',
            'kantor_cabang',
            'divisi_kantor',
            'perusahaan_kantor',
            'supplier'
            
        )