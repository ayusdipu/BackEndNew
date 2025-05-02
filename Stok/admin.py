from django.contrib import admin
from .models import StokUtama
# Register your models here.
class StokUtamaAdmin(admin.ModelAdmin):
    list_display = [
        'nama_produk',
        'kode_produk',
        'jumlah_barang',
        'gudang_cabang',
        
        
       

    ]
    list_filter = ('gudang_cabang','nama_produk')
    search_fields = ('nama_produk','produsen_produk')

admin.site.register(StokUtama, StokUtamaAdmin)