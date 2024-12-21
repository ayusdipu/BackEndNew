from django.db import models

# Create your models here.
class TugasSalesman(models.Model):
    nama_sales = models.CharField(max_length=200,blank=True,null=True)
    timestamp = models.DateField(auto_now=False,null=True,blank=True)
    tugas_diberikan = models.CharField(max_length=200,blank=True,null=True)
    hasil_tugas = models.BooleanField(default=False)
    keterangan = models.CharField(max_length=200,blank=True,null=True)

class TargetSalesman(models.Model):
    nama_sales = models.CharField(max_length=200,blank=True,null=True)
    target_minimum = models.IntegerField(null=True,blank=True)
    target_incentive = models.IntegerField(null=True,blank=True)

