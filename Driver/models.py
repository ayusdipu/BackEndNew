from django.db import models

# Create your models here.
class Driver(models.Model):
    no_kendaraan = models.CharField(max_length=200,blank=True,null=True)
    nama_supir = models.CharField(max_length=200,blank=True,null=True)
    no_telepon_supir = models.CharField(max_length=200,blank=True,null=True)
    jenis_kendaraan = models.CharField(max_length=200,blank=True,null=True)
    merek_kendaraan = models.CharField(max_length=200,blank=True,null=True)
    tahun_kendaraan = models.CharField(max_length=200,blank=True,null=True)
    status_kendaraan = models.CharField(max_length=200,blank=True,null=True,default="belum kerja")
    max_berat = models.IntegerField(null=True,blank=True)
    max_dus = models.IntegerField(null=True,blank=True)
    max_rupiah = models.IntegerField(null=True,blank=True)