from rest_framework import serializers
from Stok.models import StokUtama, StokTransit, LokasiStok

class StokSerializer(serializers.ModelSerializer):
    class Meta:
        model = StokUtama
        fields = (
            'id',
            'nama_produk',
            'kode_produk',
            'jumlah_barang',
            'gudang_cabang',
            'divisi_kantor',
            'detail_lokasi',
            'perusahaan_kantor',
            
            
        )

class StokTransitSerializer(serializers.ModelSerializer):
    class Meta:
        model = StokTransit
        fields = (
            'no_nota_transit',
            'no_SJ_keluar',
            'nama_produk',
            'kode_produk',
            'timestamp',
            'harga_modal_pcs',
            'jumlah_barang',
            'tujuan_kirim',
            'jenis_transit',
            'gudang_cabang',
            'divisi_kantor',
            'perusahaan_kantor',
            
        )

class LokasiStokSerializer(serializers.ModelSerializer):
    class Meta:
        model = LokasiStok
        fields = (
            'nama_lokasi',
            'deskripsi_lokasi',
            'foto_lokasi',
            'gudang_cabang',
            'divisi_kantor',
            'perusahaan_kantor',
            
        )