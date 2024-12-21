from django.db import models

# Create your models here.
class Stok(models.Model):
    # Buat halaman untuk menginput real stok di gudang. Setelah submit nanti ada halaman yang hanya menampilkan produk yang hasil opname sengketa, jika diklik menampilkan kartu stoknya
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kode_produk = models.CharField(max_length=200,blank=True,null=True)
    jumlah_barang = models.IntegerField(null=False, default=0)
    gudang_cabang = models.CharField(max_length=200,blank=True,null=True)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)
    opname_id = models.CharField(max_length=200,blank=True,null=True)
    hasil_opname = models.BooleanField(default=True) #hasil opname sesuai atau tidak, default sesuai
    nominal_selisih = models.IntegerField(null=False, default=0) #perbandingan stok buku (SJMasuk-SJKeluar) dengan opname fisik di gudang
    timestamp = models.DateTimeField(auto_now=False,null=True,blank=True)

class StokTransit(models.Model):
    #Ini adalah stok extra diluar SJ Masuk - SJ Keluar karena barang masih on transit
    no_nota_transit = models.CharField(max_length=200,blank=True,null=True)
    no_SJ_keluar = models.CharField(max_length=200,blank=True,null=True)
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kode_produk = models.CharField(max_length=200,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False,null=True,blank=True)
    harga_modal_pcs = models.IntegerField(null=True,blank=True)
    jumlah_barang = models.IntegerField(null=False, default=0)
    tujuan_kirim = models.CharField(max_length=200,blank=True,null=True)
    jenis_transit = models.CharField(max_length=200,blank=True,null=True)
    gudang_cabang = models.CharField(max_length=200,blank=True,null=True)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)


class LokasiStok(models.Model):
    nama_lokasi = models.CharField(max_length=200,blank=True,null=True) #Buatkan nama lokasi seperti A1, A2 dsb
    deskripsi_lokasi = models.CharField(max_length=200,blank=True,null=True) #ini adalah verbal penjelasan dimana lokasinya, misal atas kanan
    foto_lokasi = models.ImageField(null=True,blank=True,upload_to='photo_lokasi_gudang/')
    gudang_cabang = models.CharField(max_length=200,blank=True,null=True)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)