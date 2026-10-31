# NUSA Kasir - Master Asset Library Playbook (136 Granular Interaction Blueprint)

Dokumen ini adalah cetak biru (*blueprint*) katalog visual terlengkap untuk seluruh layar, menu, modal pop-up, *floating action sheet*, dan interaksi mikro di **8 Varian Usaha NUSA Kasir**. Dirancang khusus agar **AI Creator Agent (Vision Multimodal)** dapat mempelajari setiap detail aplikasi tanpa ada satu fitur atau interaksi pun yang terlewat.

---

## 📑 Daftar Isi Struktur Direktori

```text
assets/content_library/
├── 00_global_auth/          (6 Layar: Onboarding, Login Google, Lisensi, Profil Toko)
├── 01_kelontong/            (14 Layar & Sheet: Kasir, Grosir, Barcode, Stok, Kasbon, Shift, Laba)
├── 02_fnb/                  (12 Layar & Sheet: Meja, Pesanan Dapur, KDS, Resep BOM, Split Bill)
├── 03_laundry/              (10 Layar & Sheet: Kiloan, Desimal Timbangan, Rak, Status Cuci, Tag Nota)
├── 04_bengkel/              (10 Layar & Sheet: Plat Nomor, Mekanik, Jasa vs Part, Riwayat Servis, SPK)
├── 05_salon/                (10 Layar & Sheet: Stylist, Komisi Karyawan, Treatment, Payout Laporan)
├── 06_apotek/               (12 Layar & Sheet: Resep Dokter, Signa, Etiket Obat, Expired Alert, Apograph)
├── 07_fotocopy/             (12 Layar & Sheet: Hitung Lembar, Jilid, Spanduk, PC Portal File, Antrean)
├── 08_servis/               (10 Layar & Sheet: Tanda Terima Masuk, Pola Layar, Status Pengerjaan, Garansi)
├── 09_shared_pos_flow/      (10 Layar & Sheet: Keranjang, Detail Item, Diskon Global, Pilihan Bayar, QRIS, Struk)
├── 10_shared_settings/      (12 Layar & Sheet: Printer Bluetooth, 58/80mm, Sambungkan PC, PIN Staf, Backup, Studio)
└── 11_shared_operations/    (18 Layar & Sheet: Buku Kas, Pengeluaran, Stok Opname, Retur, Supplier, Kulakan PO, Presensi, Desain Promosi, ID Card Studio, Pesanan Online, Tanya AI, Multi-Cabang)
```

**Total Aset Terdokumentasi**: **136 Layar & Interaksi Mikro Granular**

---

## 🏛️ Bagian 1: 00_global_auth (Onboarding & Aktivasi Akun)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `auth_01_welcome_onboarding.png` | Screen | Layar selamat datang pertama kali membuka aplikasi. | Menampilkan logo NUSA Kasir, tagline "Cara Cerdas Kelola Usaha", dan pilihan masuk. |
| `auth_02_google_sign_in_sheet.png` | Floating Sheet | Pop-up pilihan akun Google Sign-In (Mode Pro). | Daftar akun email Google untuk sinkronisasi cloud multi-device. |
| `auth_03_license_key_input.png` | Screen | Form aktivasi kode lisensi resmi (Mode Lite / 100% Offline). | Field teks kode serial lisensi key lifetime seumur hidup. |
| `auth_04_activation_success_anim.png` | Modal Dialog | Animasi centang hijau sukses aktivasi lisensi. | Modal popup ucapan selamat toko resmi aktif permanen. |
| `auth_05_store_profile_setup.png` | Screen | Form awal pengisian identitas toko setelah aktivasi. | Input nama toko, jenis usaha, nomor HP pemilik, dan alamat. |
| `auth_06_variant_picker_sheet.png` | Floating Sheet | Pilihan 8 varian usaha spesifik saat setup awal. | Grid ikon visual 8 industri NUSA Kasir. |

---

## 🛒 Bagian 2: 09_shared_pos_flow (Alur Transaksi & Pembayaran Universal)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `pos_01_catalog_empty_cart.png` | Screen | Tampilan awal POS kasir saat keranjang masih kosong. | Grid produk berfoto, search bar, dan tombol kategori. |
| `pos_02_category_filter_chips.png` | Interaction | Pilihan filter kategori produk yang sedang aktif. | Menampilkan chip kategori horizontal (Makanan, Minuman, Sembako, dll). |
| `pos_03_cart_bar_bottom_active.png` | Floating Bar | Bar melayang bawah saat item mulai dimasukkan ke keranjang. | Menampilkan badge jumlah item, total belanja, dan tombol "Bayar ->". |
| `pos_04_item_detail_modifier_sheet.png` | Floating Sheet | Modal interaksi ketukan pada salah satu produk di keranjang. | Input jumlah quantity (+/-), catatan khusus per item, dan diskon per barang. |
| `pos_05_global_discount_sheet.png` | Modal Dialog | Modal input diskon keseluruhan nota belanja / kode promo. | Pilihan diskon persen (%) atau nominal rupiah (Rp). |
| `pos_06_customer_picker_sheet.png` | Floating Sheet | Modal pemilihan nama pelanggan / tambah pelanggan baru. | Daftar pelanggan langganan (VIP, Member, Umum). |
| `pos_07_payment_methods_sheet.png` | Floating Sheet | Layar pilihan metode pembayaran. | Pilihan: Tunai, QRIS, Transfer Bank, dan Kasbon / Hutang. |
| `pos_08_cash_fast_tender_keypad.png` | Sub-Screen | Layar pembayaran tunai dengan tombol uang cepat. | Tombol uang pas, Rp 20rb, Rp 50rb, Rp 100rb, dan hitung kembalian instan. |
| `pos_09_qris_dynamic_display.png` | Sub-Screen | Tampilan kode QRIS dinamis di layar HP. | Kode QRIS ShopeePay/NUSA valid siap scan pelanggan. |
| `pos_10_receipt_thermal_preview.png` | Floating Sheet | Pratinjau struk kasir gulungan kertas thermal 58mm/80mm. | Rincian belanja, logo toko, footer ucapan, dan tombol cetak/share WA. |

---

## 📦 Bagian 3: 01_kelontong (Varian Kelontong & Minimarket)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_grid_kelontong.png` | Screen | Katalog produk sembako, minyak, beras, dan rokok. | Grid 2 kolom kartu produk dengan harga eceran dan sisa stok. |
| `02_grosir_tier_pricing_sheet.png` | Floating Sheet | Modal pengaturan harga bertingkat grosir vs eceran. | Contoh: beli 1 pcs Rp 5.000, beli 1 lusin otomatis Rp 4.500/pcs. |
| `03_barcode_scanner_active.png` | Camera View | Layar scanner barcode menggunakan kamera belakang HP. | Bingkai kotak bidik merah membaca kode barcode produk kemasan. |
| `04_product_add_floating_sheet.png` | Floating Sheet | Modal formulir tambah produk sembako baru. | Upload foto produk, input nama barang, scan barcode, HPP, harga jual. |
| `05_product_edit_stock_sheet.png` | Floating Sheet | Modal penyesuaian stok opname fisik di gudang. | Input stok masuk, barang rusak (waste), dan sisa stok riil. |
| `06_shelf_label_print_preview.png` | Sub-Screen | Pratinjau cetak label harga rak minimarket (*price tag*). | Tampilan barcode dan harga jual untuk diselipkan di rak toko. |
| `07_kasbon_debt_customer_sheet.png` | Floating Sheet | Pencatatan transaksi belanja yang dibayar kasbon / hutang. | Pilih nama langganan, input tanggal jatuh tempo, dan nominal hutang. |
| `08_debt_installments_history.png` | Sub-Screen | Riwayat pembayaran cicilan kasbon pelanggan. | Catatan tanggal bayar cicilan dan sisa sisa hutang yang belum lunas. |
| `09_closing_shift_summary.png` | Floating Sheet | Rekap tutup shift kasir toko kelontong. | Modal awal kas, total uang laci tunai, penjualan QRIS, dan sisa uang kas. |
| `10_daily_profit_loss_report.png` | Sub-Screen | Laporan laba bersih dan laba kotor harian toko sembako. | Perhitungan otomatis omzet dikurangi harga modal belanja barang (HPP). |
| `11_best_seller_product_ranking.png` | Sub-Screen | Peringkat produk paling laku (Best Seller). | Grafik dan daftar produk dengan omzet tertinggi bulan ini. |
| `12_bulk_excel_import_sheet.png` | Floating Sheet | Modal upload ribuan produk sekaligus via file Excel. | Tombol unduh template Excel dan tombol upload massal. |
| `13_stock_low_alert_banner.png` | Component | Peringatan banner stok barang menipis (*minimum stock*). | Notifikasi merah barang yang perlu segera dibelanjakan ulang. |
| `14_receipt_with_store_logo.png` | Sub-Screen | Pratinjau struk kasir lengkap dengan logo toko kelontong. | Menampilkan foto logo toko di bagian paling atas struk. |

---

## 🍽️ Bagian 4: 02_fnb (Varian Kuliner, Kafe & Resto)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_grid_fnb_menu.png` | Screen | Daftar menu makanan, minuman, dan camilan berfoto. | Tampilan menu kafe dengan badge harga dan varian rasa. |
| `02_table_management_grid.png` | Sub-Screen | Denah visual meja tamu (Dine-in). | Kotak Meja 1–12 berwarna hijau (kosong) dan merah (terisi tamu). |
| `03_table_occupancy_detail_sheet.png` | Floating Sheet | Detail pesanan yang sedang aktif di meja tamu tertentu. | Rincian makanan yang dipesan tamu meja tersebut dan durasi makan. |
| `04_move_merge_table_dialog.png` | Modal Dialog | Modal aksi pindah meja atau gabung meja pelanggan. | Pilihan nomor meja tujuan untuk menggabungkan tagihan. |
| `05_dine_in_vs_takeaway_toggle.png` | Component | Pilihan pesanan "Makan di Tempat" vs "Bungkus / Bawa Pulang". | Segmented control di bagian atas keranjang kasir. |
| `06_product_modifier_topping_sheet.png` | Floating Sheet | Modal pilihan topping, tingkat kepedasan, dan ukuran cup. | Checkbox topping (Boba +3rb, Jelly +2rb, Less Sugar, Normal Ice). |
| `07_kitchen_order_ticket_print.png` | Sub-Screen | Pratinjau tiket pesanan fisik untuk ditempel di dapur / bar. | Nota khusus koki berisi nomor meja, daftar menu, dan catatan rasa. |
| `08_kitchen_display_system_kds.png` | Full Screen | Layar Dapur Digital (KDS) untuk monitor koki di dapur. | Kartu pesanan masuk dengan tombol centang "Selesai Dimasak". |
| `09_recipe_bom_management.png` | Screen | Pengaturan Resep & Bahan Baku (Bill of Materials). | Daftar takaran bahan mentah per resep menu makanan/minuman. |
| `10_recipe_ingredient_add_sheet.png` | Floating Sheet | Modal input takaran bahan baku (gram bubuk kopi, ml susu, cup). | Pengurangan otomatis stok bahan baku setiap menu terjual. |
| `11_split_bill_payment_modal.png` | Floating Sheet | Modal pisah tagihan bayar per orang dalam 1 meja tamu. | Pilihan menu yang ingin dibayar masing-masing pelanggan. |
| `12_fnb_daily_closing_report.png` | Sub-Screen | Laporan penjualan harian resto per kategori makanan vs minuman. | Omzet makanan, minuman, biaya servis restoran, dan total pengunjung. |

---

## 🧺 Bagian 5: 03_laundry (Varian Laundry Kiloan & Satuan)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_services_laundry.png` | Screen | Katalog layanan cuci komplit, cuci kering, setrika, dan sepatu. | Pilihan paket reguler, kilat 1 hari, dan ekspres 3 jam. |
| `02_kiloan_vs_satuan_selector.png` | Component | Pilihan mode hitungan tarif per kilogram vs per potong baju. | Tab pemisah tarif kiloan desimal dengan tarif satuan helai. |
| `03_weight_decimal_keypad_sheet.png` | Floating Sheet | Keypad input angka timbangan desimal (misal 3.75 kg). | Kalkulator hitung otomatis tarif: berat $\times$ harga per kilo. |
| `04_rack_hanger_assignment_dialog.png` | Modal Dialog | Modal penetapan nomor rak / lemari penyimpanan baju. | Input nomor rak (contoh: Rak A-04) agar baju tidak tertukar. |
| `05_perfume_fragrance_selector.png` | Component | Pilihan aroma parfum laundry langganan pelanggan. | Pilihan aroma (Sakura, Lavender, Ocean Fresh, Akasia). |
| `06_order_status_pipeline_sheet.png` | Floating Sheet | Pelacakan status pengerjaan cucian bertingkat. | Tahapan: Diterima $\rightarrow$ Dicuci $\rightarrow$ Disetrika $\rightarrow$ Siap Ambil $\rightarrow$ Selesai. |
| `07_laundry_tag_receipt_preview.png` | Sub-Screen | Nota struk tanda terima laundry dengan nomor kantong. | Informasi rincian pakaian, jumlah potong, dan janji selesai. |
| `08_whatsapp_ready_pickup_modal.png` | Modal Dialog | Modal kirim pesan WA otomatis saat cucian siap diambil. | Template pesan: "Halo kak, cucian atas nama Budi sudah wangi & siap diambil". |
| `09_laundry_production_queue.png` | Screen | Antrean kerja cucian harian berdasarkan tanggal janji selesai. | Daftar antrean cucian yang mendesak harus segera disetrika. |
| `10_laundry_revenue_report.png` | Sub-Screen | Rekapitulasi omzet kiloan vs satuan bulan ini. | Total berat kiloan yang dicuci dan keuntungan bersih pemilik. |

---

## 🔧 Bagian 6: 04_bengkel (Varian Bengkel Motor & Mobil)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_sparepart_oil_grid.png` | Screen | Katalog oli mesin, kampas rem, busi, dan ban berfoto. | Daftar suku cadang dengan kode part dan stok gudang. |
| `02_vehicle_intake_form_sheet.png` | Floating Sheet | Form pencatatan data kendaraan masuk saat pelanggan datang. | Input nomor plat polisi, merk kendaraan, tipe, dan angka kilometer (KM). |
| `03_mechanic_assignment_sheet.png` | Floating Sheet | Pilihan teknisi / montir yang mengerjakan servis. | Dropdown nama mekanik untuk perhitungan bagi hasil jasa. |
| `04_service_fee_sparepart_split.png` | Floating Sheet | Pemisahan biaya jasa servis dengan harga suku cadang. | Struk menampilkan: Jasa Pasang Rp 35.000 + Oli MPX Rp 55.000 = Rp 90.000. |
| `05_vehicle_service_history_sheet.png` | Sub-Screen | Riwayat servis riil kendaraan berdasarkan plat nomor. | Riwayat riil kapan terakhir ganti oli, servis karbu/injeksi, atau ganti ban. |
| `06_work_order_spk_preview.png` | Sub-Screen | Surat Perintah Kerja (SPK) bengkel untuk mekanik. | Lembar instruksi pengerjaan perbaikan di meja mekanik. |
| `07_bengkel_official_invoice.png` | Sub-Screen | Nota struk bengkel resmi lengkap dengan rincian garansi. | Nota cetak termal rapi untuk diberikan ke pemilik kendaraan. |
| `08_mechanic_commission_summary.png` | Sub-Screen | Rekapitulasi upah bagi hasil mekanik bengkel. | Total pendapatan jasa per montir untuk pembayaran gaji harian/mingguan. |
| `09_sparepart_restock_alert.png` | Component | Peringatan stok oli dan sparepart fast-moving menipis. | Indikator stok minimum agar bengkel tidak kehabisan oli mesin. |
| `10_bengkel_monthly_sales_report.png` | Sub-Screen | Laporan laba bengkel: pendapatan jasa vs margin suku cadang. | Pemisahan keuntungan murni jasa dengan laba jual sparepart. |

---

## ✂️ Bagian 7: 05_salon (Varian Salon & Barbershop)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_salon_services_grid.png` | Screen | Daftar menu potong rambut, pewarnaan, creambath, dan spa. | Kartu layanan perawatan dengan durasi pengerjaan dan harga. |
| `02_stylist_kapster_select_sheet.png` | Floating Sheet | Modal pilihan terapis, kapster, atau hair stylist yang melayani. | Foto dan nama staf salon yang bertugas melayani tamu. |
| `03_treatment_package_bundling_sheet.png` | Floating Sheet | Pilihan paket bundling hemat perawatan rambut. | Contoh: Paket Potong + Cuci Rambut + Pijat Relaksasi. |
| `04_stylist_commission_calculator.png` | Floating Sheet | Perhitungan komisi persentase otomatis per layanan. | Contoh: Jasa Potong Rp 50.000 $\rightarrow$ Komisi Kapster 40% (Rp 20.000). |
| `05_customer_hair_notes_sheet.png` | Floating Sheet | Catatan preferensi model rambut pelanggan setia. | Catatan model potong (contoh: Fade 2 jari, cat warna ash grey). |
| `06_salon_receipt_with_stylist_name.png` | Sub-Screen | Nota struk kasir salon yang mencantumkan nama kapster. | Struk mencantumkan nama stylist yang menangani pelanggan. |
| `07_stylist_daily_payout_report.png` | Sub-Screen | Laporan rekapan komisi harian per kapster/stylist. | Rincian jumlah kepala yang dipotong dan total komisi yang cair hari ini. |
| `08_appointment_queue_list.png` | Screen | Antrean reservasi dan walk-in pelanggan salon. | Status kursi salon: Sedang Dilayani vs Menunggu Antrean. |
| `09_product_retail_upsell_sheet.png` | Component | Penjualan produk retail (pomade, vitamin rambut, shampoo). | Transaksi produk perawatan bersamaan dengan jasa potong. |
| `10_salon_performance_analytics.png` | Sub-Screen | Analisis layanan kecantikan yang paling diminati. | Perbandingan omzet jasa haircut, coloring, dan perawatan wajah. |

---

## 💊 Bagian 8: 06_apotek (Varian Apotek & Toko Obat)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_medicine_catalog_grid.png` | Screen | Katalog obat bebas (lingkaran hijau), bebas terbatas (biru), dan keras (merah K). | Tampilan obat dalam satuan strip, botol, box, dan blister. |
| `02_prescription_doctor_intake_sheet.png` | Floating Sheet | Form pencatatan resep dokter resmi. | Input nama dokter, nomor SIP, nama pasien, usia, dan berat badan (BB anak). |
| `03_signa_dosage_rule_picker.png` | Floating Sheet | Pilihan aturan pakai obat cepat (*signa*). | Opsi: 3x1 sehari sesudah makan, 2x1 tablet, sebelum tidur, tetes mata. |
| `04_medicine_etiket_print_preview.png` | Sub-Screen | Pratinjau etiket aturan pakai obat 58mm untuk ditempel di botol/plastik. | Label stiker putih berisi nama apotek, nama pasien, dan aturan pakai. |
| `05_batch_number_expiry_sheet.png` | Floating Sheet | Pencatatan nomor batch pabrik dan tanggal kadaluarsa obat. | Input tanggal expired saat penerimaan barang dari PBF / distributor. |
| `06_expiry_date_alert_warning_list.png` | Sub-Screen | Daftar peringatan obat yang mendekati masa kadaluarsa (30/60/90 hari). | Peringatan merah obat yang harus segera dipisah atau diretur. |
| `07_official_apograph_copy_receipt.png` | Sub-Screen | Salinan resep resmi (apograph) bertanda tangan apoteker. | Lembar salinan resep dengan tanda "detur" (sudah diserahkan). |
| `08_unit_conversion_calculator_sheet.png` | Floating Sheet | Konversi satuan obat (1 Box = 10 Strip = 100 Tablet). | Penyesuaian harga jual saat pembeli membeli eceran tablet atau per strip. |
| `09_controlled_medicine_report.png` | Sub-Screen | Laporan pengeluaran obat resep dokter. | Laporan pencatatan obat resep untuk kebutuhan pembukuan farmasi. |
| `10_apotek_daily_margin_report.png` | Sub-Screen | Laporan laba penjualan obat bebas vs obat resep. | Keuntungan bersih apotek dengan margin HPP obat. |
| `11_supplier_pbf_purchase_order.png` | Sub-Screen | Surat pesanan barang ke Pedagang Besar Farmasi (PBF). | Form restock obat yang habis dengan nama distributor. |
| `12_customer_drug_allergy_record.png` | Component | Catatan riwayat alergi obat pelanggan pada profil pasien. | Peringatan merah peringatan alergi (contoh: Alergi Amoxicillin). |

---

## 🖨️ Bagian 9: 07_fotocopy (Varian Fotocopy & Percetakan)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_print_copy_services_grid.png` | Screen | Daftar tarif fotocopy BW/warna, jilid skripsi, laminating, dan ATK. | Kartu jasa percetakan dengan harga satuan per lembar. |
| `02_per_page_pricing_calculator.png` | Floating Sheet | Kalkulator hitung otomatis jasa cetak dokumen per lembar. | Input jumlah halaman $\times$ rangkap $\times$ ukuran kertas (A4/F4/A3). |
| `03_color_mode_paper_selector.png` | Component | Pilihan mode warna cetak: Hitam Putih (BW) vs Warna Laser. | Segmented selector penentu tarif harga otomatis. |
| `04_binding_laminating_options_sheet.png` | Floating Sheet | Modal pilihan jilid buku (lakban biasa, spiral kawat, hardcover skripsi). | Pilihan finishing jilid tinta emas dan laminating panas tebal. |
| `05_banner_meteran_calculator_dialog.png` | Modal Dialog | Kalkulator hitung spanduk / banner per meter persegi ($P \times L$). | Input panjang $\times$ lebar meter $\times$ bahan Flexi 280gr / 340gr. |
| `06_pc_portal_file_queue_screen.png` | Screen | Tampilan antrean file kiriman pembeli di aplikasi HP. | Daftar berkas PDF/Word pelanggan yang masuk lewat portal toko. |
| `07_pc_portal_download_detail_modal.png` | Floating Sheet | Detail pesanan cetak pelanggan dan spesifikasi dokumen. | Nama pembeli, nomor WA, jumlah rangkap, dan tombol unduh. |
| `08_fotocopy_job_ticket_receipt.png` | Sub-Screen | Nota struk tanda terima antrean cetak dengan jam janji selesai. | Struk berisi nomor antrean pengerjaan cetak untuk pembeli. |
| `09_atk_retail_item_catalog.png` | Sub-Screen | Penjualan alat tulis kantor (kertas rim HVS, map folio, pulpen). | Transaksi barang fisik ATK bersamaan dengan jasa print. |
| `10_pc_portal_web_browser_view.png` | Browser View | Tampilan layar monitor PC operator saat membuka `localhost:8080/portal-file`. | Antarmuka desktop monitor operator yang sedang klik tombol "Unduh ke PC". |
| `11_production_paper_waste_log.png` | Component | Catatan kertas rusak / gagal cetak (*paper waste*). | Pencatatan limbah kertas cetak untuk audit modal toko. |
| `12_fotocopy_daily_sales_recap.png` | Sub-Screen | Laporan omzet harian: pendapatan fotocopy, print, jilid, dan ATK. | Pembagian porsi pendapatan jasa mesin dengan jualan kertas/ATK. |

---

## 📱 Bagian 10: 08_servis (Varian Servis HP & Elektronik)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_sparepart_device_grid.png` | Screen | Katalog suku cadang LCD, baterai original, konektor charger, dan casing. | Daftar komponen servis dengan ketersediaan stok fisik. |
| `02_unit_intake_receipt_complaint_sheet.png` | Floating Sheet | Form tanda terima servis masuk saat pelanggan menyerahkan unit. | Input merk/tipe HP, keluhan kerusakan, kelengkapan (unit, charger, dus). |
| `03_screen_pattern_pin_draw_sheet.png` | Floating Sheet | Lembar gambar pola kunci layar (pattern lock) atau PIN HP pelanggan. | Gambar grid 3x3 pola layar untuk pengujian teknisi setelah selesai servis. |
| `04_cost_estimate_down_payment_dialog.png` | Modal Dialog | Pencatatan estimasi total biaya servis dan uang muka (DP). | Input perkiraan harga sparepart + jasa perbaikan + uang muka pelanggan. |
| `05_intake_claim_receipt_preview.png` | Sub-Screen | Cetak nota tanda terima servis resmi untuk dibawa pulang pelanggan. | Nota struk thermal berisi nomor tiket servis, syarat klaim, dan nomor WA toko. |
| `06_repair_status_pipeline_sheet.png` | Floating Sheet | Pengubahan status pengerjaan unit servis di meja teknisi. | Status bertingkat: Unit Masuk $\rightarrow$ Sedang Dicek $\rightarrow$ Menunggu Sparepart $\rightarrow$ Selesai $\rightarrow$ Diambil. |
| `07_whatsapp_service_done_notify_modal.png` | Modal Dialog | Modal kirim notifikasi WA otomatis: "HP Anda sudah selesai diperbaiki". | Pesan otomatis rincian biaya yang harus dibayar saat pengambilan. |
| `08_service_warranty_card_print.png` | Sub-Screen | Cetak kartu garansi servis resmi (garansi 7 hari / 30 hari). | Syarat garansi: segel tidak rusak, tidak terkena air, nota asli dibawa. |
| `09_technician_commission_payout.png` | Sub-Screen | Rekapitulasi bagi hasil ongkos servis teknisi per unit selesai. | Perhitungan gaji atau persentase komisi bagi hasil teknisi servis. |
| `10_servis_monthly_revenue_report.png` | Sub-Screen | Laporan laba usaha servis: keuntungan jasa perbaikan vs jual sparepart/aksesoris. | Rekap total unit selesai diperbaiki dan omzet bulanan konter servis. |

---

## ⚙️ Bagian 11: 10_shared_settings (Pengaturan Sistem, Hardware & Keamanan)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `set_01_settings_menu_main.png` | Screen | Menu utama pengaturan aplikasi NUSA Kasir. | Daftar menu: Profil Toko, Printer, Hubungkan PC, Karyawan, Backup. |
| `set_02_store_data_edit_form.png` | Sub-Screen | Form pengaturan identitas toko lengkap. | Ganti nama toko, nomor WhatsApp kasir, alamat, dan upload gambar logo toko. |
| `set_03_receipt_footer_tax_sheet.png` | Floating Sheet | Pengaturan pesan catatan kaki struk (*footer*) dan pajak resto/PPN. | Contoh footer: "Barang yang dibeli tidak dapat ditukar", PPN 11%. |
| `set_04_printer_bluetooth_scanner_sheet.png` | Floating Sheet | Modal pencarian dan pairing printer thermal Bluetooth di sekitar. | Daftar perangkat Bluetooth aktif (Panda, Iware, VSC, Eppos, Sunmi). |
| `set_05_printer_paper_width_selector.png` | Component | Pilihan lebar kertas printer thermal: 58mm vs 80mm. | Tombol toggle ukuran kertas dan tombol "Uji Cetak Struk". |
| `set_06_lan_pc_connect_screen.png` | Screen | Layar menu "Sambungkan ke Komputer" (Web POS & Portal File). | Menampilkan status server aktif, alamat IP lokal (`http://192.168.x.x:8080`), dan petunjuk Chrome. |
| `set_07_lan_pairing_pin_modal.png` | Modal Dialog | Modal tampilan PIN pairing 4-digit acak untuk otorisasi PC kasir. | Angka PIN keamanan (misal: 2803) untuk dimasukkan di browser komputer. |
| `set_08_employee_list_roles.png` | Sub-Screen | Daftar staf karyawan kasir beserta jabatan (Kasir, Staf, Owner). | Pengelolaan akun karyawan toko. |
| `set_09_employee_add_pin_access_sheet.png` | Floating Sheet | Modal pembuatan akun kasir baru dan proteksi PIN. | Toggle pembatasan akses: Kunci laporan laba, kunci ubah harga, kunci hapus transaksi. |
| `set_10_backup_restore_sheet.png` | Floating Sheet | Modal simpan cadangan data (*backup*) & pulihkan data (*restore*). | Tombol simpan file cadangan `.nus1` ke kartu memori / Google Drive. |
| `set_11_creator_studio_control_sheet.png` | Floating Sheet | Modal rahasia Creator Studio Control Sheet (hasil 5x tap logo). | Pengontrol instan beralih 8 varian dan mode Pro/Lite untuk pembuatan konten. |
| `set_12_about_license_version_info.png` | Sub-Screen | Layar informasi lisensi resmi, versi aplikasi (`v2.3.0+171`), dan tombol cek update. | Status lisensi aktif seumur hidup (Lifetime) tanpa biaya bulanan. |

---

## 💼 Bagian 12: 11_shared_operations (Buku Kas, Stok Opname, Retur, Supplier, Presensi & Studio)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `op_01_shift_cash_drawer_open.png` | Floating Sheet | Modal buka kasir & input modal awal uang laci saat toko baru buka. | Field input nominal modal kas kecil kasir di awal hari kerja. |
| `op_02_finance_cashflow_overview.png` | Screen | Layar pembukuan Buku Kas toko (arus kas masuk vs kas keluar). | Ringkasan saldo kas toko, total pemasukan penjualan, dan total pengeluaran operasional. |
| `op_03_finance_expense_record_sheet.png` | Floating Sheet | Modal formulir pencatatan biaya pengeluaran operasional toko. | Input jenis beban (listrik, air, gaji harian, sewa tempat, sampah) dan upload foto nota bon. |
| `op_04_stock_opname_audit_screen.png` | Screen | Layar audit stok opname fisik barang di toko & gudang. | Tabel pencocokan stok sistem vs hitungan fisik riil di rak barang. |
| `op_05_stock_adjustment_confirm_dialog.png` | Modal Dialog | Modal konfirmasi penyesuaian selisih stok (barang rusak, expired, hilang). | Dialog peringatan penyesuaian selisih sebelum stok riil diperbarui permanen. |
| `op_06_transactions_history_list.png` | Screen | Daftar seluruh riwayat transaksi penjualan & filter tanggal/kasir. | Kartu transaksi nota penjualan dengan status lunas, kasbon, dan metode bayar. |
| `op_07_transaction_detail_receipt_view.png` | Sub-Screen | Detail rincian nota transaksi belanja & tombol cetak ulang struk. | Rincian item barang terjual, nama kasir, jam transaksi, dan tombol "Cetak Struk Ulang". |
| `op_08_transaction_refund_return_dialog.png` | Modal Dialog | Modal proses retur barang / refund pengembalian uang konsumen. | Pilihan pengembalian barang rusak atau salah beli dengan input alasan retur. |
| `op_09_suppliers_vendor_list.png` | Screen | Daftar buku kontak pemasok / agen distributor barang kulakan. | Kartu pemasok lengkap dengan nama sales, nomor WhatsApp, dan alamat gudang distributor. |
| `op_10_supplier_add_vendor_sheet.png` | Floating Sheet | Modal formulir tambah pemasok / distributor langganan baru. | Input nama distributor, no HP sales, nomor rekening, dan tempo pembayaran (TOP). |
| `op_11_purchase_order_restock_screen.png` | Screen | Form faktur pembelian barang kulakan masuk (*Purchase Order*). | Input barang masuk dari supplier, harga beli modal (HPP baru), dan tanggal jatuh tempo faktur. |
| `op_12_attendance_clockin_screen.png` | Screen | Layar absensi kehadiran staf kasir & rekap jam kerja harian. | Tombol jam masuk / jam pulang, status hadir/izin, dan rekap jam kerja mingguan. |
| `op_13_promo_design_studio_editor.png` | Screen | Studio pembuat flyer & materi promosi diskon media sosial. | Kanvas desain template otomatis siap upload ke WhatsApp Story dan Instagram Feed. |
| `op_14_id_card_member_studio.png` | Screen | Studio pembuat kartu member pelanggan & ID Card staf kasir. | Kartu cetak ID Card dua sisi lengkap dengan QR Code barcode member toko. |
| `op_15_online_orders_dashboard.png` | Screen | Dashboard kelola pesanan masuk dari toko online web / WhatsApp. | Tab status pesanan online: Pesanan Baru $\rightarrow$ Sedang Diproses $\rightarrow$ Dikirim $\rightarrow$ Selesai. |
| `op_16_online_storefront_preview.png` | Web / Screen | Pratinjau etalase toko online mandiri yang dilihat oleh pembeli. | Halaman belanja online responsif per-toko dengan katalog produk dan tombol pesan via WA. |
| `op_17_ai_business_consultant_chat.png` | Screen | Layar konsultasi pintar Asisten AI Toko NUSA Kasir. | Percakapan tanya jawab analisis performa toko, saran produk laris, dan strategi omzet. |
| `op_18_multibranch_outlet_manager.png` | Screen | Layar pengelolaan multi-cabang outlet dan pantau stok antar-toko. | Daftar cabang usaha (Cabang 1, Cabang 2), pemindahan staf, dan transfer mutasi stok. |

---

## 🎯 Panduan untuk AI Creator Agent (Vision Multimodal Reasoning)

Ketika AI Creator Agent membaca direktori aset ini:
1. **Pola Penamaan**: Nama file diawali dengan nomor urut kronologis (`01_`, `02_`, dst.) yang menunjukkan urutan alami alur kerja (*user flow*) seorang pedagang.
2. **Konteks Interaksi**: Kata kunci seperti `_sheet`, `_dialog`, `_modal`, dan `_keypad` menandakan elemen UI melayang yang muncul di atas layar utama akibat ketukan tombol pengguna.
3. **Penyusunan Konten Otomatis**:
   - Jika membuat konten *Carousel Edukasi*, pilih 5–7 gambar berurutan dari satu varian (misal: `01_pos_grid` $\rightarrow$ `04_product_add` $\rightarrow$ `02_grosir_tier` $\rightarrow$ `07_kasbon` $\rightarrow$ `10_daily_profit`).
   - Jika membuat video pendek TikTok/Reels, pasangkan screenshot interaksi mikro yang relevan saat narasi membicarakan fitur tersebut (misal saat narasi membahas kembalian, pasangkan `pos_08_cash_fast_tender_keypad.png`).
