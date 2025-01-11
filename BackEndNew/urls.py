"""
URL configuration for BackEndNew project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Customer import views as c_views
from Driver import views as d_views
from LedgerKas import views as l_views
from Pembelian import views as beli_views
from Penjualan import views as jual_views
from Produk import views as p_views
from Salesman import views as sales_views
from Stok import views as stok_views
from SuratJalanKeluar import views as sjk_views
from SuratJalanMasuk import views as sjm_views
from UserProfile import views as profile_views
from rest_framework import routers


router = routers.DefaultRouter()
#Customer
router.register('registeredcustomer',c_views.RegisteredCustomerView)
router.register('loyaltypointcustomer',c_views.LoyaltyPointCustomerView)
router.register('datapotensicustomer',c_views.DataPotensiCustomerView)
router.register('dailyregisteredcustomer',c_views.DailyRegisteredCustomerReportView)
router.register('kontrakoutletpromotion',c_views.KontrakOutletPromotionView)
#Driver
router.register('driver',d_views.DriverView)
#LedgerKas
router.register('kas',l_views.KasView)
router.register('masterakun',l_views.MasterAkunView)
router.register('tabelneracaawal',l_views.TabelNeracaAwalView)
router.register('jurnalentry',l_views.JurnalEntryView)
#Pembelian
router.register('notapembelian',beli_views.NotaPembelianView)
router.register('detailpembelian',beli_views.DetailPembelianView)
#Penjualan
router.register('notapenjualan',jual_views.NotaPenjualanView)
router.register('detailpenjualan',jual_views.DetailPenjualanView)
#Produk
router.register('produk',p_views.ProdukView)
router.register('produkpromotion',p_views.ProdukPromotionView)
#Salesman
router.register('tugassalesman',sales_views.TugasSalesmanView)
router.register('targetsalesman',sales_views.TargetSalesmanView)
#Stok
router.register('stok',stok_views.StokView)
router.register('stoktransit',stok_views.StokTransitView)
router.register('lokasistok',stok_views.LokasiStokView)
#SuratJalanKeluar
router.register('sjkeluar',sjk_views.SJKeluarView)
router.register('detailsjkeluar',sjk_views.DetailSJKeluarView)
router.register('detaillokasikeluarproduk',sjk_views.DetailLokasiKeluarProdukView)
#SuratJalanMasuk
router.register('sjmasuk',sjm_views.SJMasukView)
router.register('detailsjmasuk',sjm_views.DetailSJMasukView)
#Profile
router.register('profile',profile_views.ProfileView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
]
