## Jika choice ada di Tabel (urut dari atas) sebelumnya maka akan direuse diselanjutnya 
## SEMUA PENGAJUAN DAN PERUBAHAN DISINI HARUS PERSETUJUAN DIREKTUR, MANAGER TIDAK BERHAK MERUBAH OPSI CHOICE

## CHOICES di Customer ##

choice_kategori_outlet = [
    ('2W','2W'),
    ('4W','4W'),
    ('6W','6W'),
    ('2W4W','2W4W'),
    ('4W6W','4W6W'),
    ('2W6W','2W6W'),
    ('2W4W6W','2W4W6W'),
    ('Pabrik','Pabrik'),
    ('Tambang','Tambang'),
    ('Alat Berat','Alat Berat'),
    ('Sub Contractor','Sub Contractor'),
    ('Crusher','Crusher'),
    ('Kapal Tangker','Kapal Tangker'),
    ('Kapal Nelayan','Kapal Nelayan'),
    ('Pembangkit','Pembangkit'),
    ('PO Bus','PO Bus'),
    ('Trucking','Trucking'),
    ('Logistik','Logistik'),
    ('Perkebunan','Perkebunan'),
    ('Peternakan','Peternakan'),
    ('Pengolahan','Pengolahan'),
    ('Industri Lain','Industri Lain')
]


choice_level_outlet = [
    ('kecil','kecil'),
    ('sedang','sedang'),
    ('besar','besar'),
    ('sangat besar','sangat besar')
]

choice_tipe_outlet = [
    ('kelilingan','kelilingan'),
    ('toko','toko'),
    ('bengkel','bengkel'),
    ('spbu','spbu'),
    ('bengkel own channel','bengkel own channel'),
    ('industri','industri'),
    ('KAM','KAM'),
    ('atpm','atpm')
]

choice_bentuk_usaha_outlet = [
    ('PT','PT'),
    ('CV','CV'),
    ('Koperasi','Koperasi'),
    ('Yayasan','Yayasan'),
    ('UD','UD'),
    ('BUMN','BUMN'),
    ('BUMD','BUMD'),
    ('Perorangan','Perorangan')
]

choice_lebar_muka_jalan = [
    ('lebih kecil dari 4m','lebih kecil dari 4m'),
    ('4m sampai 8m','4m sampai 8m'),
    ('lebih dari 8m','lebih dari 8m'),
]

choice_tipe_lokasi_outlet = [
    ('R1','R1'),
    ('R2','R2'),
    ('R3','R3'),
    ('R4','R4')
]

choice_kondisi_outlet = [
    ('terawat','terawat'),
    ('kurang terawat','kurang terawat'),
    ('tidak terawat','tidak terawat')
]

choice_oli_dominan = [
    ('Shell Motor','Shell Motor'),
    ('Shell Mobil','Shell Mobil'),
    ('Pertamina','Pertamina'),
    ('MPX','MPX'),
    ('Federal','Federal'),
    ('Evalube','Evalube'),
    ('Merek Lain','Merek Lain')
]

choice_bisnis_fokus_outlet = [
    ('ban','ban'), 
    ('oli','oli'),
    ('aki','aki'),
    ('sparepart','sparepart'),
    ('bisnis lain','bisnis lain')
]


choice_estimasi_nilai_stok = [
    ('dibawah 5 juta','dibawah 5 juta'),
    ('5-20 juta','5-20 juta'),
    ('diatas 20 juta','diatas 20 juta')
]

choice_cluster_outlet = [
    ('Industri','Industri'),
    ('KAM','KAM'),
    ('cikebu','cikebu'),
    ('babawopa','babawopa'),
    ('temapur','temapur'),
    ('DIY','DIY'),
    ('Luar Cluster','Luar Cluster')
]

choice_divisi_kantor = [
    ('Pelumas','Pelumas'), 
    ('LPG NPSO','LPG NPSO'),
    ('LPG PSO','LPG PSO'),
    ('Minyak Inmar','Minyak Inmar'),
    ('Customer Goods','Customer Goods')
]

choice_perusahaan_kantor = [
    ('PT. Gelora Putra Perkasa','PT. Gelora Putra Perkasa'),
    ('PT. Gelora Portalindo','PT. Gelora Portalindo'),
    ('PT. Buana Rahayu','PT Buana Rahayu'),
    ('PT. Sochi Jaya Sentosa','PT. Sochi Jaya Sentosa'),
    ('PT. Serayu Mitra Jaya','PT. Serayu Mitra Jaya')
]

choice_rute_kunjungan = [
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('belum ada','belum ada')
]

choice_tipe_promo = [
    ('single produk','single produk'), 
    ('by merek','by merek'),
    ('by submerek','by submerek'),
    ('by tiersegmen','by tiersegmen'),
    ('by usersegmen','by usersegmen'),
    ('by kategori','by kategori'),
    ('by klasifikasi','by klasifikasi'),
    ('by spek','by spek'),
    ('by produsen','by produsen'),
    ('by jenis','by jenis'),
    ('all produk','all produk')
]

## CHOICES di Produk ##
choice_kemasan = [
    ('Dus','Dus'),
    ('Botol','Botol'),
    ('Drum','Drum'),
    ('Pail','Pail'),
    ('Pcs','Pcs'),
    ('Ikat','Ikat')
]

choice_isi_pack = [
    (0,0),
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (8,8),
    (10,10),
    (12,12),
    (15,15),
    (20,20),
    (24,24),
    (25,25),
    (30,30),
    (32,32),
    (35,35),
    (48,48),
    (50,50),
    (56,56),
    (60,60),
    (70,70),
    (100,100),
    (150,150),
    (180,180),
    (200,200)
]

choice_volume_pcs = [
    (0,0),
    (0.05,0.05),
    (0.07,0.07),
    (0.12,0.12),
    (0.15,0.15),
    (0.16,0.16),
    (0.3,0.3),
    (0.4,0.4),
    (0.5,0.5),
    (0.65,0.65),
    (0.7,0.7),
    (0.8,0.8),
    (1.0,1.0),
    (1.2,1.2),
    (3.5,3.5),
    (4.0,4.0),
    (5.0,5.0),
    (10.0,10.0),
    (16.0,16.0),
    (18.0,18.0),
    (20.0,20.0),
    (178.0,178.0),
    (200.0,200.0),
    (209.0,209.0)
]

choice_merek = [
    ('Enduro','Enduro'),('Fastron','Fastron'),('Mesran','Mesran'),('Meditran','Meditran'),
    ('Prima XP','Prima XP'),('Rored','Rored'),('Pertamina','Pertamina'),('Gemuk Pertamina','Gemuk Pertamina'),
    ('Masri','Masri'),('Medripal','Medripal'),('Kompen','Kompen'),('Turalik','Turalik'),('Trafolube','Trafolube'),
    ('Turbolube','Turbolube'),('Salyx','Salyx'),('Translik','Translik'),('Enviro','Enviro'),
    ('Diloka','Diloka'),('Gandar','Gandar'),('GC Lube','GC Lube'),('NG Lube','NG Lube'),('Knito','Knito'),
    ('Sebana','Sebana'),('Silinap','Silinap'),('Steelo','Steelo'),('Termo','Termo'),('MPX','MPX'),
    ('Federal','Federal'),('Mobil','Mobil'),('SPX','SPX'),('Advance','Advance'),('Helix','Helix'),
    ('Evalube','Evalube'),('Idemitsu','Idemitsu'),('Top1','Top1'),('Rimula','Rimula'),('Castrol','Castrol'),
    ('Orange','Orange'),('Jumbo','Jumbo'),('Ban AHM'),('Aki Yuasa'),('Aki GS'),('Agip','Agip'),
    ('Repsol','Repsol'),('Yamalube','Yamalube'),('Ban IRC','Ban IRC'),('Busi NGK','Busi NGK'),
    ('Megacool','Megacool'),('Busi Champion','Busi Champion'),('Motul','Motul'),('Unnoco','Unnoco'),
    ('Treebond','Treebond'),('Ban Kingland','Ban Kingland'),('TMO','TMO'),('Fortag','Fortag'),
    ('Prestone','Prestone')
]

choice_submerek = [
    ('Enduro Racing', 'Enduro Racing'), ('Enduro Matic', 'Enduro Matic'), ('Enduro Matic S', 'Enduro Matic S'),
    ('Enduro Matic G', 'Enduro Matic G'), ('Enduro Gear Matic', 'Enduro Gear Matic'), ('Enduro Matic V', 'Enduro Matic V'),
    ('Enduro Sport', 'Enduro Sport'), ('Enduro 4T', 'Enduro 4T'), ('Prima XP 10W-40', 'Prima XP 10W-40'),
    ('Prima XP 20W-50', 'Prima XP 20W-50'), ('Mesran 40', 'Mesran 40'), ('Mesran B40', 'Mesran B40'),
    ('Mesrania 2T', 'Mesrania 2T'), ('Mesran Marine', 'Mesran Marine'), ('Fastron Gold', 'Fastron Gold'),
    ('Fastron Techno', 'Fastron Techno'), ('Fastron Diesel', 'Fastron Diesel'), ('Fastron EcoGreen', 'Fastron EcoGreen'),
    ('Fastron Platinum', 'Fastron Platinum'), ('Coolant', 'Coolant'), ('ATF', 'ATF'), ('Break Fluid', 'Break Fluid'),
    ('Gemuk SGX', 'Gemuk SGX'), ('Gemuk EPX', 'Gemuk EPX'), ('Enviro', 'Enviro'), ('Diloka', 'Diloka'),
    ('Gandar', 'Gandar'), ('GC Lube M', 'GC Lube M'), ('GC Lube Syn', 'GC Lube Syn'), ('Knito', 'Knito'),
    ('NG Lube', 'NG Lube'), ('Maxcool NC', 'Maxcool NC'), ('Maxcool SM', 'Maxcool SM'), ('Maxcool Syn', 'Maxcool Syn'),
    ('Maxcool WS', 'Maxcool WS'), ('Rinsol', 'Rinsol'), ('Rubbsol', 'Rubbsol'), ('Rusguard', 'Rusguard'),
    ('Slideway', 'Slideway'), ('Refro', 'Refro'), ('Sebana P', 'Sebana P'), ('Silinap', 'Silinap'),
    ('Spreeze', 'Spreeze'), ('Steelo', 'Steelo'), ('Termo', 'Termo'), ('Termo XT', 'Termo XT'),
    ('Trafolube', 'Trafolube'), ('Meditran SC', 'Meditran SC'), ('Meditran S40', 'Meditran S40'),
    ('Meditran SX Bio', 'Meditran SX Bio'), ('Meditran SX', 'Meditran SX'), ('Mesran', 'Mesran'),
    ('Mesran Super', 'Mesran Super'), ('Mesran Super Motor', 'Mesran Super Motor'), ('Rored EPA', 'Rored EPA'),
    ('Rored HDA', 'Rored HDA'), ('Rored MTF', 'Rored MTF'), ('Gemuk HDX-2', 'Gemuk HDX-2'), ('Gemuk LI CX-2', 'Gemuk LI CX-2'),
    ('Gemuk Super EPX-2', 'Gemuk Super EPX-2'), ('Gemuk Super HDX-2', 'Gemuk Super HDX-2'), ('Gemuk WR-NL', 'Gemuk WR-NL'),
    ('Gemuk X-NL2', 'Gemuk X-NL2'), ('Gemuk X-NL3', 'Gemuk X-NL3'), ('Kompen', 'Kompen'), ('Masri FLG', 'Masri FLG'),
    ('Masri RG', 'Masri RG'), ('Masri SMG', 'Masri SMG'), ('Masri Syn', 'Masri Syn'), ('Meditran', 'Meditran'),
    ('Meditran E', 'Meditran E'), ('Meditran GEO', 'Meditran GEO'), ('Meditran P', 'Meditran P'), ('Meditran S', 'Meditran S'),
    ('Meditran SMX', 'Meditran SMX'), ('Meditran SV', 'Meditran SV'), ('Meditran SXV', 'Meditran SXV'), ('Medripal', 'Medripal'),
    ('Salyx', 'Salyx'), ('Salyx C', 'Salyx C'), ('Salyx DF', 'Salyx DF'), ('Translik', 'Translik'),
    ('Turalik', 'Turalik'), ('Turalik C', 'Turalik C'), ('Turalik CX', 'Turalik CX'), ('Turalik T', 'Turalik T'),
    ('Turalik V', 'Turalik V'), ('Turalik XT', 'Turalik XT'), ('Turbolube', 'Turbolube'), ('Turbolube XT', 'Turbolube XT'),
    ('AHM Chainlube', 'AHM Chainlube'), ('AHM Gear', 'AHM Gear'), ('Brake Fluid', 'Brake Fluid'),
    ('AHM Coolant', 'AHM Coolant'), ('Fortag Chain Lube', 'Fortag Chain Lube'), ('Carb Cleaner 2B', 'Carb Cleaner 2B'),
    ('Carb Cleaner', 'Carb Cleaner'), ('Prestone Rem', 'Prestone Rem'), ('TMO', 'TMO'), ('Yamaha YTZ', 'Yamaha YTZ'),
    ('AHM Ban K59 A12', 'AHM Ban K59 A12'), ('AHM Ban K59 A72', 'AHM Ban K59 A72'), ('AHM Ban KVB', 'AHM Ban KVB'),
    ('AHM Ban K93', 'AHM Ban K93'), ('AHM Ban KOJ', 'AHM Ban KOJ'), ('AHM Ban KOW', 'AHM Ban KOW'),
    ('AHM Ban KPH', 'AHM Ban KPH'), ('AHM Ban KTM', 'AHM Ban KTM'), ('AHM Ban KWW', 'AHM Ban KWW'),
    ('Alfabatt', 'Alfabatt'), ('AHM Bearing', 'AHM Bearing'), ('Busi AHM U20', 'Busi AHM U20'), ('Busi AHM U22', 'Busi AHM U22'),
    ('AHM Filter Udara', 'AHM Filter Udara'), ('AHM Gearset', 'AHM Gearset'), ('IRC BD Ring 17', 'IRC BD Ring 17'),
    ('IRC BD Ring 18', 'IRC BD Ring 18'), ('IRC BD Ring 14', 'IRC BD Ring 14'), ('IRC BL Ring 12 TL', 'IRC BL Ring 12 TL'),
    ('IRC BL Ring 17', 'IRC BL Ring 17'), ('IRC BL Ring 18', 'IRC BL Ring 18'), ('IRC BL Ring 13 TL', 'IRC BL Ring 13 TL'),
    ('IRC BL Ring 19', 'IRC BL Ring 19'), ('IRC BL Ring 20', 'IRC BL Ring 20'), ('IRC BL Ring 21', 'IRC BL Ring 21'),
    ('IRC BL Ring 22', 'IRC BL Ring 22'), ('IRC BL Ring 23', 'IRC BL Ring 23'), ('IRC BL Ring 24', 'IRC BL Ring 24'),
    ('IRC BL Ring 25', 'IRC BL Ring 25'), ('IRC BL Ring 14', 'IRC BL Ring 14'), ('IRC BL Ring 14 TL', 'IRC BL Ring 14 TL'),
    ('IRC BL Ring 16', 'IRC BL Ring 16'), ('AHM Kabel Speedo', 'AHM Kabel Speedo'), ('AHM Kampas Rem', 'AHM Kampas Rem'),
    ('King Jaguar BL Ring 14', 'King Jaguar BL Ring 14'), ('King Jaguar BL Ring 17', 'King Jaguar BL Ring 17'),
    ('King Tiger BL Ring 14', 'King Tiger BL Ring 14'), ('AHM Lampu KFV', 'AHM Lampu KFV'), ('AHM Oil Seal', 'AHM Oil Seal'),
    ('AHM Pelindung Knalpot', 'AHM Pelindung Knalpot'), ('AHM Rantai Keteng', 'AHM Rantai Keteng'), ('AHM Roller', 'AHM Roller'),
    ('AHM Rumah Roller', 'AHM Rumah Roller'), ('AHM Seal Shock', 'AHM Seal Shock'), ('AHM Shockbeker Assy', 'AHM Shockbeker Assy'),
    ('AHM Vanbelt', 'AHM Vanbelt'), ('Agip 2T', 'Agip 2T'), ('MPX1', 'MPX1'), ('MPX2', 'MPX2'),
    ('MPX3', 'MPX3'), ('Castrol Active', 'Castrol Active'), ('Castrol Active Matic', 'Castrol Active Matic'),
    ('Castrol 2T', 'Castrol 2T'), ('Castrol 4T', 'Castrol 4T'), ('Castrol Magnatec', 'Castrol Magnatec'),
    ('Castrol Power', 'Castrol Power'), ('Evalube 2T', 'Evalube 2T'), ('Evalube 2T Pro', 'Evalube 2T Pro'),
    ('Evalube 4T', 'Evalube 4T'), ('Federal Flick', 'Federal Flick'), ('Federal Gear', 'Federal Gear'),
    ('Federal Matic Orange', 'Federal Matic Orange'), ('Federal Ultratec', 'Federal Ultratec'), ('Federal XX', 'Federal XX'),
    ('Idemitsu 2T', 'Idemitsu 2T'), ('Motul 3100', 'Motul 3100'), ('Motul 510', 'Motul 510'),
    ('Motul 5100', 'Motul 5100'), ('Motul Scooter', 'Motul Scooter'), ('Jumbo Rem', 'Jumbo Rem'),
    ('Jumbo Shock', 'Jumbo Shock'), ('Orange Tropical', 'Orange Tropical'), ('Repsol MXR3', 'Repsol MXR3'),
    ('Repsol MXR Matic', 'Repsol MXR Matic'), ('Shell 2TSX', 'Shell 2TSX'), ('Shell AX3', 'Shell AX3'),
    ('Shell AX5', 'Shell AX5'), ('Shell AX5 Sc', 'Shell AX5 Sc'), ('Shell AX7', 'Shell AX7'),
    ('Shell AX7 Sc', 'Shell AX7 Sc'), ('Shell HX3', 'Shell HX3'), ('Shell HX5', 'Shell HX5'),
    ('Shell HX6', 'Shell HX6'), ('Shell HX7', 'Shell HX7'), ('Shell HX8', 'Shell HX8'),
    ('Shell RX4', 'Shell RX4'), ('Shell RX4 LDP', 'Shell RX4 LDP'), ('SPX1', 'SPX1'),
    ('SPX2', 'SPX2'), ('Top1', 'Top1'), ('Unoco Coolant', 'Unoco Coolant'),
    ('Yamalube Matic', 'Yamalube Matic'), ('Yamalube Silver', 'Yamalube Silver'), ('Yamalube Sport', 'Yamalube Sport'),
    ('Yamalube Super Matic', 'Yamalube Super Matic'), ('GS GM5Z', 'GS GM5Z'), ('GS GTZ5S', 'GS GTZ5S'),
    ('GS GTZ6V', 'GS GTZ6V'), ('Yuasa YB5LB', 'Yuasa YB5LB'), ('Yuasa YTZ5V', 'Yuasa YTZ5V'),
    ('Yuasa YTZ6V', 'Yuasa YTZ6V'), ('Champion RG4HC', 'Champion RG4HC'), ('Champion Z9Y', 'Champion Z9Y'),
    ('NGK-BP7ES', 'NGK-BP7ES'), ('NGK-BP7HS', 'NGK-BP7HS'), ('NGK-BP8ES', 'NGK-BP8ES'),
    ('NGK-BP8HS', 'NGK-BP8HS'), ('NGK-C7HSA', 'NGK-C7HSA'), ('NGK-CPR6EA', 'NGK-CPR6EA'),
    ('NGK-D6HSA', 'NGK-D6HSA'), ('NGK-D8EA', 'NGK-D8EA'), ('TREEBOND', 'TREEBOND'),
    ('NGK-DP8EA', 'NGK-DP8EA'), ('NGK-T5999', 'NGK-T5999'), ('NGK-T6000', 'NGK-T6000'),
    ('Yamaha YTZ Kering', 'Yamaha YTZ Kering')
]

choice_tier = [
    ('Very High Tier','Very High Tier'),
    ('High Tier','High Tier'),
    ('Middle Tier','Middle Tier'),
    ('Low Tier','Low Tier'),
    ('Very Low Tier','Very Low Tier')
]

choice_user = [
    ('2W','2W'),
    ('4W','4W'),
    ('6W','6W'),
    ('Industrial','Industrial')
]


choice_kategori = [
    ('Ban','Ban'),
    ('Oli','Oli'),
    ('Aki','Aki'),
    ('Busi','Busi'),
    ('Sparepart','Sparepart')
]

choice_klasifikasi = [
    ('Retail','Retail'),
    ('Industri','Industri')
]

choice_produsen = [
    ('Pertamina', 'Pertamina'), ('Exxon Federal', 'Exxon Federal'), ('Honda AHM', 'Honda AHM'), 
    ('Yamaha', 'Yamaha'), ('Repsol', 'Repsol'), ('Shell', 'Shell'), ('Castrol', 'Castrol'), 
    ('Idemitsu', 'Idemitsu'), ('Orange Oil', 'Orange Oil'), ('Motul', 'Motul'), ('United', 'United'), 
    ('Top1', 'Top1'), ('WGI Evalube', 'WGI Evalube'), ('Agip', 'Agip'), ('Gajah Tunggal', 'Gajah Tunggal'), 
    ('NGK', 'NGK'), ('Yuasa', 'Yuasa'), ('Megacool', 'Megacool'), ('AHM', 'AHM'), 
    ('Jumbo', 'Jumbo'), ('Prestone', 'Prestone'), ('Toyota TMO', 'Toyota TMO'), ('Ecco', 'Ecco'), 
    ('GS', 'GS'), ('Champion', 'Champion'), ('Kingland', 'Kingland'), ('Treebond Inc', 'Treebond Inc')
]

choice_jenis = [
    ('Fast Moving','Fast Moving'),
    ('Slow Moving','Slow Moving')
]

choice_debit_kredit = [
    ('debit','debit'),
    ('kredit','kredit')
]