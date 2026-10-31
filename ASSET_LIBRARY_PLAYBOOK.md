# NUSA Kasir - Master Asset Library Playbook (198 Granular Per-Variant Blueprint)

Dokumen ini adalah cetak biru (*blueprint*) katalog visual terlengkap dan **100% mandiri per-varian usaha** untuk NUSA Kasir. Setiap varian memiliki pustaka aset visual utuh yang mempertahankan **warna tema khas, identitas produk riil, tata letak menu khusus, dan alur operasionalnya masing-masing** tanpa tercampur dengan varian lain.

---

## 📑 Daftar Isi Struktur Direktori Per-Varian

```text
assets/content_library/
├── 00_global_auth/          (6 Aset: Welcome Onboarding, Google Sign-in, Lisensi Key, Variant Picker)
├── 01_kelontong/            (24 Aset Lengkap: Hijau Emerald #10B981 - POS Sembako, Grosir, Barcode, Kasbon, Shift, Kas, Stok)
├── 02_fnb/                  (24 Aset Lengkap: Oranye Amber #F59E0B - POS Kuliner, Meja Dine-in, KDS, Resep BOM, Split Bill, Kas)
├── 03_laundry/              (24 Aset Lengkap: Biru Cyan #06B6D4 - POS Cuci, Timbangan kg, Rak Baju, Status Cuci, Tag Nota, Kas)
├── 04_bengkel/              (24 Aset Lengkap: Merah Crimson #EF4444 - POS Part, Nopol/KM, Montir, Jasa vs Part, SPK Garansi, Kas)
├── 05_salon/                (24 Aset Lengkap: Pink Rose #F43F5E - POS Treatment, Stylist, Komisi, Bundling, Booking, Payout, Kas)
├── 06_apotek/               (24 Aset Lengkap: Hijau Teal #14B8A6 - POS Obat, Resep Dokter, Signa, Etiket 58mm, Expired, SP PBF, Kas)
├── 07_fotocopy/             (24 Aset Lengkap: Biru Indigo #6366F1 - POS Print/Jilid, Hitung Lembar, Banner, Portal File PC, Kas)
└── 08_servis/               (24 Aset Lengkap: Ungu Violet #8B5CF6 - POS Part, Tanda Terima, Pola 3x3, Status Servis, Garansi, Kas)
```

**Total Aset Terdokumentasi**: **198 Layar & Interaksi Mikro Granular**

---

## 🏛️ Direktori 00: 00_global_auth (Onboarding & Aktivasi Akun Universal)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `auth_01_welcome_onboarding.png` | Screen | Layar selamat datang pertama kali membuka aplikasi. | Menampilkan logo NUSA Kasir, tagline "Cara Cerdas Kelola Usaha", dan tombol masuk. |
| `auth_02_google_sign_in_sheet.png` | Floating Sheet | Pop-up pilihan akun Google Sign-In (Mode Pro). | Daftar akun email Google untuk sinkronisasi cloud multi-device. |
| `auth_03_license_key_input.png` | Screen | Form aktivasi kode lisensi resmi (Mode Lite / 100% Offline). | Field teks kode serial lisensi key lifetime seumur hidup. |
| `auth_04_activation_success_anim.png` | Modal Dialog | Animasi centang hijau sukses aktivasi lisensi. | Modal popup ucapan selamat toko resmi aktif permanen. |
| `auth_05_store_profile_setup.png` | Screen | Form awal pengisian identitas toko setelah aktivasi. | Input nama toko, jenis usaha, nomor HP pemilik, dan alamat. |
| `auth_06_variant_picker_sheet.png` | Floating Sheet | Pilihan 8 varian usaha spesifik saat setup awal. | Grid ikon visual 8 industri NUSA Kasir. |

---

## 🛒 Direktori 01: 01_kelontong (Varian Kelontong & Minimarket - Hijau Emerald)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_catalog_grid.png` | Screen | Katalog produk sembako, minyak, beras, dan rokok berfoto. | Kartu produk 2 kolom dengan harga eceran dan sisa stok fisik. |
| `02_category_filter_chips.png` | Interaction | Pilihan filter kategori sembako yang sedang aktif. | Menampilkan chip horizontal: Makanan, Minuman, Sembako, Rokok. |
| `03_barcode_scanner_active.png` | Camera View | Layar scanner barcode menggunakan kamera belakang HP. | Bingkai kotak bidik merah membaca kode barcode kemasan. |
| `04_cart_bottom_active.png` | Floating Bar | Bar melayang bawah saat keranjang terisi barang belanjaan. | Badge jumlah item, total belanja, dan tombol "Bayar ->". |
| `05_item_quantity_notes_sheet.png` | Floating Sheet | Modal ubah jumlah quantity (+/-) dan catatan khusus per item. | Input jumlah pcs, diskon per barang, dan catatan. |
| `06_grosir_tier_pricing_sheet.png` | Floating Sheet | Modal pengaturan harga bertingkat grosir vs eceran. | Contoh: beli 1 pcs Rp 5.000, beli 1 lusin otomatis Rp 4.500/pcs. |
| `07_shelf_label_price_tag.png` | Sub-Screen | Pratinjau cetak label harga rak minimarket (*price tag*). | Tampilan barcode dan harga jual untuk diselipkan di rak toko. |
| `08_kasbon_customer_sheet.png` | Floating Sheet | Pencatatan transaksi belanja yang dibayar kasbon / hutang. | Pilih nama langganan, input tanggal jatuh tempo, dan nominal hutang. |
| `09_debt_installments_history.png` | Sub-Screen | Riwayat pembayaran cicilan kasbon pelanggan. | Catatan tanggal bayar cicilan dan sisa hutang yang belum lunas. |
| `10_product_add_form_sheet.png` | Floating Sheet | Modal formulir tambah produk sembako baru. | Upload foto produk, nama barang, scan barcode, HPP, harga jual. |
| `11_payment_methods_sheet.png` | Floating Sheet | Layar checkout pilihan cara bayar. | Pilihan: Tunai, QRIS, Transfer Bank, dan Kasbon. |
| `12_cash_fast_tender_keypad.png` | Sub-Screen | Layar pembayaran tunai dengan tombol uang cepat pas. | Tombol uang pas, Rp 20rb, Rp 50rb, Rp 100rb, dan hitung kembalian instan. |
| `13_qris_dynamic_display.png` | Sub-Screen | Tampilan kode QRIS dinamis siap scan. | Kode QRIS ShopeePay/NUSA valid siap scan pelanggan. |
| `14_receipt_thermal_preview.png` | Floating Sheet | Pratinjau struk thermal 58mm dengan logo toko sembako. | Rincian belanja, logo toko kelontong, footer ucapan terima kasih. |
| `15_closing_shift_summary.png` | Floating Sheet | Rekap tutup shift kasir toko kelontong. | Modal awal kas, total uang laci tunai, dan penjualan QRIS. |
| `16_finance_cashflow_overview.png` | Screen | Buku Kas toko sembako (arus kas masuk vs keluar). | Ringkasan saldo kas toko, omzet harian, dan total pengeluaran. |
| `17_finance_expense_sheet.png` | Floating Sheet | Modal formulir pencatatan biaya operasional toko kelontong. | Input beban listrik, air, sewa lapak, sampah harian. |
| `18_stock_inventory_list.png` | Screen | Daftar stok fisik sembako dan indikator stok menipis. | Indikator stok minimum agar toko tidak kehabisan beras/minyak. |
| `19_stock_opname_audit_sheet.png` | Screen | Formulir audit penyesuaian stok opname fisik di gudang. | Tabel pencocokan stok sistem vs hitungan fisik riil di rak. |
| `20_transactions_history_list.png` | Screen | Riwayat transaksi penjualan toko sembako & filter kasir. | Kartu nota penjualan lunas/kasbon dan tombol cetak ulang. |
| `21_transaction_refund_dialog.png` | Modal Dialog | Modal proses retur barang rusak atau salah beli. | Dialog input alasan pengembalian barang dan refund dana. |
| `22_suppliers_restock_sheet.png` | Screen | Daftar buku kontak pemasok agen sembako & form kulakan PO. | Kontak sales distributor mie instan, minyak goreng, dan beras. |
| `23_settings_printer_setup.png` | Floating Sheet | Pengaturan printer thermal Bluetooth 58mm/80mm toko kelontong. | Pencarian printer Bluetooth aktif dan opsi uji cetak. |
| `24_settings_lan_pc_connect.png` | Screen | Layar Sambungkan ke Komputer (Web POS kasir minimarket). | Alamat IP lokal LAN untuk kasir PC di meja komputer kasir. |

---

## 🍽️ Direktori 02: 02_fnb (Varian Kuliner, Kafe & Resto - Oranye Amber)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_fnb_menu_grid.png` | Screen | Katalog menu kafe: kopi, minuman segar, dan makanan. | Kartu menu kuliner dengan badge harga dan varian rasa. |
| `02_table_management_grid.png` | Sub-Screen | Denah visual meja tamu (Dine-in). | Kotak Meja 1–12 berwarna hijau (kosong) dan oranye (terisi tamu). |
| `03_table_occupancy_detail_sheet.png` | Floating Sheet | Detail pesanan aktif di meja tamu tertentu. | Rincian makanan yang sedang dinikmati tamu meja dan durasi makan. |
| `04_move_merge_table_dialog.png` | Modal Dialog | Modal aksi pindah meja atau gabung tagihan meja tamu. | Pilihan nomor meja tujuan untuk menggabungkan pesanan. |
| `05_dine_in_vs_takeaway_toggle.png` | Component | Pilihan pesanan "Makan di Tempat" vs "Bungkus / Takeaway". | Segmented control di atas keranjang kasir kafe. |
| `06_product_modifier_topping_sheet.png` | Floating Sheet | Modal pilihan topping, tingkat kepedasan, dan less/normal ice. | Checkbox topping: Boba +3rb, Jelly +2rb, Level 1-5, Less Sugar. |
| `07_cart_fnb_order_active.png` | Floating Bar | Bar pesanan meja kafe terisi makanan dan minuman. | Ringkasan pesanan dapur dan tombol lanjut pembayaran. |
| `08_kitchen_order_ticket_print.png` | Sub-Screen | Pratinjau tiket pesanan koki dapur / barista bar. | Nota khusus koki berisi nomor meja, menu, dan instruksi rasa. |
| `09_kitchen_display_system_kds.png` | Full Screen | Layar Dapur Digital (KDS) untuk monitor koki di dapur. | Kartu pesanan masuk dengan tombol centang "Selesai Dimasak". |
| `10_recipe_bom_management.png` | Screen | Pengaturan Resep & Bahan Baku (Bill of Materials). | Daftar takaran bahan mentah per resep makanan/minuman kafe. |
| `11_recipe_ingredient_add_sheet.png` | Floating Sheet | Modal input takaran bahan baku (gram bubuk kopi, ml susu). | Pengurangan otomatis stok bahan setiap menu terjual. |
| `12_split_bill_payment_modal.png` | Floating Sheet | Modal pisah tagihan bayar per orang dalam 1 meja tamu. | Pilihan menu yang ingin dibayar masing-masing pengunjung. |
| `13_payment_methods_sheet.png` | Floating Sheet | Layar checkout kasir kafe/resto. | Pilihan: Tunai, QRIS, Transfer Bank, dan Debit EDC. |
| `14_cash_fast_tender_keypad.png` | Sub-Screen | Pembayaran tunai kasir kafe & hitung kembalian cepat. | Tombol nominal uang pas dan perhitungan kembalian tamu. |
| `15_qris_dynamic_display.png` | Sub-Screen | Tampilan kode QRIS dinamis di meja kasir kafe. | QRIS siap scan untuk pembayaran pesanan makanan/minuman. |
| `16_receipt_thermal_preview.png` | Floating Sheet | Struk kasir kafe lengkap rincian nomor meja & biaya servis. | Nota thermal estetik kafe dengan footer password WiFi. |
| `17_fnb_daily_closing_report.png` | Sub-Screen | Laporan penjualan harian resto: makanan vs minuman. | Omzet makanan, minuman, servis resto, dan total tamu datang. |
| `18_finance_cashflow_overview.png` | Screen | Buku Kas harian resto/kafe (arus kas masuk vs keluar). | Ringkasan kas laci kasir kafe dan pencatatan belanja harian. |
| `19_finance_expense_sheet.png` | Floating Sheet | Catat belanja bahan makanan basah dapur & es batu. | Formulir pengeluaran belanja pasar harian koki dapur. |
| `20_stock_raw_materials_list.png` | Screen | Daftar stok bahan baku mentah (biji kopi, susu, cup, sedotan). | Peringatan bahan baku dapur yang menipis. |
| `21_transactions_history_list.png` | Screen | Riwayat transaksi meja kafe & rincian pesanan. | Arsip transaksi kasir kafe berdasarkan jam sibuk (*rush hour*). |
| `22_attendance_staff_shift.png` | Screen | Layar presensi absensi staf barista, waiter, dan koki dapur. | Jam masuk/pulang staf kafe per shift kerja. |
| `23_settings_printer_kitchen.png` | Floating Sheet | Pengaturan multi-printer: printer kasir & printer dapur. | Routing cetak otomatis nota kasir ke kasir dan tiket koki ke dapur. |
| `24_settings_lan_pc_connect.png` | Screen | Layar Sambungkan ke Komputer (Web POS & Monitor KDS PC). | Buka tampilan kasir atau KDS di layar monitor dapur via browser PC. |

---

## 🧺 Direktori 03: 03_laundry (Varian Laundry Kiloan & Satuan - Biru Cyan)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_services_laundry_grid.png` | Screen | Katalog layanan cuci komplit, cuci kering, setrika, bedcover. | Pilihan paket reguler, kilat 1 hari, dan ekspres 3 jam. |
| `02_kiloan_vs_satuan_selector.png` | Component | Pilihan mode hitungan tarif per kilogram vs per potong baju. | Tab pemisah tarif kiloan desimal dengan tarif satuan helai. |
| `03_weight_decimal_keypad_sheet.png` | Floating Sheet | Keypad input angka timbangan desimal (misal 3.75 kg). | Kalkulator hitung otomatis tarif: berat $\times$ harga per kilo. |
| `04_perfume_fragrance_selector.png` | Component | Pilihan aroma parfum laundry favorit pelanggan. | Pilihan aroma: Sakura, Lavender, Ocean Fresh, Akasia. |
| `05_rack_hanger_assignment_dialog.png` | Modal Dialog | Modal penetapan nomor rak / lemari penyimpanan baju. | Input nomor rak (contoh: Rak A-04) agar pakaian tidak tertukar. |
| `06_cart_laundry_order_active.png` | Floating Bar | Bar pesanan cucian pelanggan terisi paket kiloan. | Rincian jumlah kilo, parfum, dan tombol proses nota terima. |
| `07_order_status_pipeline_sheet.png` | Floating Sheet | Pelacakan status pengerjaan cucian bertingkat. | Tahapan: Diterima $\rightarrow$ Dicuci $\rightarrow$ Disetrika $\rightarrow$ Siap Ambil $\rightarrow$ Selesai. |
| `08_laundry_tag_receipt_preview.png` | Sub-Screen | Nota struk tanda terima laundry dengan nomor kantong. | Informasi rincian pakaian, jumlah potong, dan janji selesai. |
| `09_whatsapp_ready_pickup_modal.png` | Modal Dialog | Modal kirim pesan WA otomatis saat cucian siap diambil. | Template pesan: "Halo kak, cucian sudah wangi & siap diambil". |
| `10_laundry_production_queue.png` | Screen | Antrean kerja cucian harian berdasarkan tanggal janji selesai. | Daftar antrean cucian yang mendesak harus segera disetrika. |
| `11_payment_methods_sheet.png` | Floating Sheet | Layar pilihan cara bayar laundry (bisa DP di awal / bayar saat ambil). | Pilihan: Tunai, QRIS, Transfer Bank, dan Bayar Nanti. |
| `12_cash_fast_tender_keypad.png` | Sub-Screen | Pembayaran tunai uang muka cucian & kembalian. | Input uang muka (DP) atau pelunasan saat baju diambil. |
| `13_qris_dynamic_display.png` | Sub-Screen | Tampilan kode QRIS dinamis di meja kasir laundry. | QRIS pembayaran instan tanpa perlu uang kembalian koin. |
| `14_receipt_thermal_preview.png` | Floating Sheet | Struk thermal tanda terima cucian lengkap nomor kantong. | Struk thermal rapi untuk diselipkan di luar plastik packing baju. |
| `15_laundry_revenue_report.png` | Sub-Screen | Rekapitulasi omzet kiloan vs satuan bulan ini. | Total berat kiloan yang dicuci dan laba bersih pemilik laundry. |
| `16_finance_cashflow_overview.png` | Screen | Buku Kas operasional laundry (masuk vs keluar). | Rekap omzet harian dikurangi biaya beli deterjen, softener, gas dryer. |
| `17_finance_expense_sheet.png` | Floating Sheet | Catat belanja deterjen cair, parfum, plastik packing, gas. | Formulir pengeluaran rutin operasional mesin cuci. |
| `18_stock_detergent_chemical.png` | Screen | Stok bahan kimia laundry (deterjen, softener, parfum, tag pin). | Indikator stok sabun cuci agar tidak kehabisan saat mesin beroperasi. |
| `19_stock_opname_audit_sheet.png` | Screen | Audit stok bahan kimia laundry dan kemasan plastik. | Pencocokan stok jerigen deterjen riil di gudang. |
| `20_transactions_history_list.png` | Screen | Riwayat transaksi cucian pelanggan & status pelunasan. | Daftar nota cucian lunas vs belum lunas saat baju diambil. |
| `21_customer_loyalty_sheet.png` | Floating Sheet | Kartu member langganan cuci (cuci 10x gratis 1x). | Pencatatan otomatis poin transaksi member laundry. |
| `22_attendance_staff_shift.png` | Screen | Layar presensi staf pencuci dan operator setrika uap. | Absensi kehadiran harian staf laundry. |
| `23_settings_printer_setup.png` | Floating Sheet | Pengaturan printer thermal Bluetooth nota laundry 58mm. | Setting printer untuk cetak struk dan label nomor kantong. |
| `24_settings_lan_pc_connect.png` | Screen | Layar Sambungkan ke Komputer (Web POS counter laundry). | Buka kasir laundry di browser PC counter kasir. |

---

## 🔧 Direktori 04: 04_bengkel (Varian Bengkel Motor & Mobil - Merah Crimson)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_sparepart_oil_grid.png` | Screen | Katalog oli mesin, kampas rem, busi, dan ban berfoto. | Daftar suku cadang dengan kode part dan stok gudang. |
| `02_vehicle_intake_form_sheet.png` | Floating Sheet | Form pencatatan data kendaraan masuk saat pelanggan datang. | Input nomor plat polisi, merk kendaraan, tipe, dan angka KM. |
| `03_mechanic_assignment_sheet.png` | Floating Sheet | Pilihan teknisi / montir yang mengerjakan servis. | Dropdown nama mekanik untuk perhitungan bagi hasil jasa. |
| `04_service_fee_sparepart_split.png` | Floating Sheet | Pemisahan biaya jasa servis dengan harga suku cadang. | Struk menampilkan: Jasa Pasang Rp 35.000 + Oli MPX Rp 55.000. |
| `05_vehicle_service_history_sheet.png` | Sub-Screen | Riwayat servis riil kendaraan berdasarkan plat nomor. | Riwayat riil kapan terakhir ganti oli, servis karbu, atau ganti ban. |
| `06_cart_bengkel_order_active.png` | Floating Bar | Bar pesanan servis dan pembelian sparepart aktif. | Total biaya suku cadang ditambah upah jasa servis. |
| `07_work_order_spk_preview.png` | Sub-Screen | Surat Perintah Kerja (SPK) bengkel untuk mekanik. | Lembar instruksi pengerjaan perbaikan di meja mekanik. |
| `08_bengkel_official_invoice.png` | Sub-Screen | Nota struk bengkel resmi lengkap dengan rincian garansi. | Nota cetak termal rapi untuk diberikan ke pemilik kendaraan. |
| `09_mechanic_commission_summary.png` | Sub-Screen | Rekapitulasi upah bagi hasil komisi mekanik bengkel. | Total pendapatan jasa per montir untuk pencairan upah harian/mingguan. |
| `10_sparepart_restock_alert.png` | Component | Peringatan stok oli dan sparepart fast-moving menipis. | Indikator stok minimum agar bengkel tidak kehabisan oli mesin. |
| `11_payment_methods_sheet.png` | Floating Sheet | Layar checkout kasir bengkel. | Pilihan: Tunai, QRIS, Transfer Bank, dan Kasbon perbaikan. |
| `12_cash_fast_tender_keypad.png` | Sub-Screen | Pembayaran tunai ongkos servis & suku cadang. | Input uang tunai pemilik kendaraan dan hitung kembalian cepat. |
| `13_qris_dynamic_display.png` | Sub-Screen | QRIS dinamis di meja kasir konter bengkel. | QRIS pembayaran digital tanpa repot cari uang kembalian. |
| `14_receipt_thermal_preview.png` | Floating Sheet | Struk thermal bengkel resmi mencantumkan plat nomor & montir. | Rincian jasa, sparepart, dan syarat garansi servis. |
| `15_bengkel_monthly_sales_report.png` | Sub-Screen | Laporan laba bengkel: pendapatan jasa vs margin suku cadang. | Pemisahan keuntungan murni jasa dengan laba jual sparepart. |
| `16_finance_cashflow_overview.png` | Screen | Buku Kas bengkel (arus kas masuk servis vs kas keluar). | Ringkasan omzet harian bengkel dan beban operasional. |
| `17_finance_expense_sheet.png` | Floating Sheet | Catat belanja solar pembersih, majun, oli bekas, kompresor. | Formulir biaya pengeluaran harian bengkel. |
| `18_stock_sparepart_inventory.png` | Screen | Daftar stok gudang suku cadang & oli mesin. | Tabel stok sparepart motor/mobil lengkap dengan kode part. |
| `19_stock_opname_audit_sheet.png` | Screen | Formulir audit stok opname sparepart di rak mekanik. | Pencocokan fisik jumlah busi, kanvas rem, dan botol oli. |
| `20_transactions_history_list.png` | Screen | Riwayat servis kendaraan dan nota transaksi bengkel. | Arsip perbaikan kendaraan lengkap tanggal dan nama montir. |
| `21_suppliers_part_vendor_sheet.png` | Screen | Daftar distributor oli resmi dan agen suku cadang langganan. | Kontak sales grosir sparepart motor/mobil dan tempo bayar. |
| `22_attendance_mechanic_shift.png` | Screen | Layar presensi absensi mekanik dan staf kasir bengkel. | Catatan jam kerja harian mekanik. |
| `23_settings_printer_setup.png` | Floating Sheet | Pengaturan printer thermal Bluetooth 58mm/80mm bengkel. | Koneksi printer kasir dan cetak nota SPK montir. |
| `24_settings_lan_pc_connect.png` | Screen | Layar Sambungkan ke Komputer (Web POS meja kasir bengkel). | Akses kasir bengkel di layar komputer PC konter depan. |

---

## ✂️ Direktori 05: 05_salon (Varian Salon & Barbershop - Rose Velvet)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_salon_services_grid.png` | Screen | Daftar menu potong rambut, pewarnaan, creambath, dan spa. | Kartu layanan perawatan dengan durasi pengerjaan dan harga. |
| `02_stylist_kapster_select_sheet.png` | Floating Sheet | Modal pilihan terapis, kapster, atau hair stylist yang melayani. | Foto dan nama staf salon yang bertugas melayani tamu. |
| `03_treatment_package_bundling_sheet.png` | Floating Sheet | Pilihan paket bundling hemat perawatan kecantikan. | Contoh: Paket Potong + Cuci Rambut + Pijat Relaksasi. |
| `04_stylist_commission_calculator.png` | Floating Sheet | Perhitungan komisi persentase otomatis per layanan salon. | Contoh: Jasa Potong Rp 50.000 $\rightarrow$ Komisi Kapster 40% (Rp 20.000). |
| `05_customer_hair_notes_sheet.png` | Floating Sheet | Catatan preferensi model rambut pelanggan setia. | Catatan model potong (contoh: Fade 2 jari, cat warna ash grey). |
| `06_cart_salon_order_active.png` | Floating Bar | Bar pesanan salon terisi jasa perawatan & produk pomade. | Total jasa haircut ditambah belanja produk retail kecantikan. |
| `07_appointment_queue_list.png` | Screen | Antrean reservasi dan walk-in pelanggan salon. | Status kursi salon: Sedang Dilayani vs Menunggu Antrean. |
| `08_product_retail_upsell_sheet.png` | Component | Penjualan produk retail (pomade, vitamin rambut, shampoo). | Transaksi produk perawatan bersamaan dengan jasa potong. |
| `09_salon_receipt_stylist_name.png` | Sub-Screen | Nota struk kasir salon yang mencantumkan nama kapster. | Struk mencantumkan nama stylist yang menangani pelanggan. |
| `10_stylist_daily_payout_report.png` | Sub-Screen | Laporan rekapan komisi harian per kapster/stylist. | Rincian jumlah kepala yang dipotong dan total komisi yang cair hari ini. |
| `11_payment_methods_sheet.png` | Floating Sheet | Layar checkout kasir salon. | Pilihan: Tunai, QRIS, Transfer Bank, dan Debit Card. |
| `12_cash_fast_tender_keypad.png` | Sub-Screen | Bayar tunai kasir salon & input tips kapster. | Pembayaran tunai pelanggan salon dan kalkulator kembalian. |
| `13_qris_dynamic_display.png` | Sub-Screen | Tampilan kode QRIS dinamis di meja resepsionis salon. | QRIS pembayaran praktis tanpa sentuh uang fisik. |
| `14_receipt_thermal_preview.png` | Floating Sheet | Pratinjau struk thermal estetik salon nama stylist. | Desain struk elegan salon kecantikan / barbershop modern. |
| `15_salon_performance_analytics.png` | Sub-Screen | Analisis layanan kecantikan yang paling diminati. | Perbandingan omzet jasa haircut, coloring, dan perawatan wajah. |
| `16_finance_cashflow_overview.png` | Screen | Buku Kas salon (arus kas masuk treatment vs kas keluar). | Ringkasan saldo kas salon dan pencairan komisi harian. |
| `17_finance_expense_sheet.png` | Floating Sheet | Catat belanja shampoo, obat cat, handuk, vitamin rambut. | Formulir pengeluaran rutin bahan kecantikan salon. |
| `18_stock_beauty_products.png` | Screen | Stok produk perawatan & barang jualan retail. | Sisa botol shampoo, pomade, obat creambath di rak salon. |
| `19_stock_opname_audit_sheet.png` | Screen | Formulir audit stok fisik botol obat rambut di salon. | Pencocokan sisa botol obat kimia salon. |
| `20_transactions_history_list.png` | Screen | Riwayat transaksi perawatan salon & kapster bertugas. | Arsip transaksi treatment pelanggan salon. |
| `21_customer_membership_sheet.png` | Floating Sheet | Kartu member loyalitas salon (diskon khusus member). | Poin reward perawatan pelanggan setia salon. |
| `22_attendance_stylist_shift.png` | Screen | Layar presensi absensi hair stylist dan terapis salon. | Jam kehadiran staf kapster per shift. |
| `23_settings_printer_setup.png` | Floating Sheet | Pengaturan printer thermal Bluetooth 58mm meja kasir salon. | Pairing printer Bluetooth dan opsi cetak struk wangi. |
| `24_settings_lan_pc_connect.png` | Screen | Layar Sambungkan ke Komputer (Web POS resepsionis salon). | Buka kasir salon di komputer monitor meja depan. |

---

## 💊 Direktori 06: 06_apotek (Varian Apotek & Toko Obat - Hijau Teal)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_medicine_catalog_grid.png` | Screen | Katalog obat bebas (hijau), terbatas (biru), dan keras (K merah). | Tampilan obat dalam satuan strip, botol, box, dan blister. |
| `02_prescription_doctor_intake_sheet.png` | Floating Sheet | Form pencatatan resep dokter resmi. | Input nama dokter, nomor SIP, nama pasien, usia, dan berat badan. |
| `03_signa_dosage_rule_picker.png` | Floating Sheet | Pilihan aturan pakai obat cepat (*signa*). | Opsi: 3x1 sehari sesudah makan, 2x1 tablet, sebelum tidur. |
| `04_medicine_etiket_print_preview.png` | Sub-Screen | Pratinjau etiket aturan pakai obat 58mm untuk ditempel di botol/plastik. | Label stiker putih berisi nama apotek, nama pasien, dan aturan pakai. |
| `05_batch_number_expiry_sheet.png` | Floating Sheet | Pencatatan nomor batch pabrik dan tanggal kadaluarsa obat. | Input tanggal expired saat penerimaan barang dari PBF / distributor. |
| `06_cart_apotek_order_active.png` | Floating Bar | Bar pesanan kasir apotek terisi obat bebas & resep dokter. | Rincian obat yang dibeli pasien dan total biaya resep. |
| `07_expiry_date_alert_warning.png` | Sub-Screen | Daftar peringatan obat yang mendekati masa kadaluarsa (30/60/90 hari). | Peringatan merah obat yang harus segera dipisah atau diretur. |
| `08_official_apograph_copy_receipt.png` | Sub-Screen | Salinan resep resmi (apograph) bertanda tangan apoteker. | Lembar salinan resep dengan tanda "detur" (sudah diserahkan). |
| `09_unit_conversion_calculator.png` | Floating Sheet | Konversi satuan obat (1 Box = 10 Strip = 100 Tablet). | Penyesuaian harga jual saat pembeli membeli eceran tablet atau per strip. |
| `10_controlled_medicine_report.png` | Sub-Screen | Laporan pengeluaran obat resep dokter. | Laporan pencatatan obat resep untuk kebutuhan pembukuan farmasi. |
| `11_payment_methods_sheet.png` | Floating Sheet | Layar checkout kasir apotek. | Pilihan: Tunai, QRIS, Transfer Bank, dan Asuransi/Klaim. |
| `12_cash_fast_tender_keypad.png` | Sub-Screen | Pembayaran tunai kasir apotek & hitung kembalian cepat. | Tombol uang cepat dan perhitungan kembalian pasien apotek. |
| `13_qris_dynamic_display.png` | Sub-Screen | Tampilan kode QRIS dinamis di konter apotek. | QRIS siap scan untuk tebus obat di apotek. |
| `14_receipt_thermal_preview.png` | Floating Sheet | Nota struk apotek resmi nomor SIP dokter & nomor resep. | Struk thermal rapi mencantumkan nama apoteker penanggung jawab. |
| `15_apotek_daily_margin_report.png` | Sub-Screen | Laporan laba penjualan obat bebas vs obat resep. | Keuntungan bersih apotek dengan kalkulasi HPP obat. |
| `16_finance_cashflow_overview.png` | Screen | Buku Kas apotek (arus kas penjualan obat vs operasional). | Ringkasan saldo kas masuk apotek dan pembayaran ke distributor PBF. |
| `17_finance_expense_sheet.png` | Floating Sheet | Catat biaya operasional apotek & lisensi apoteker. | Formulir pengeluaran rutin apotek. |
| `18_stock_medicine_inventory.png` | Screen | Daftar stok obat gudang apotek & etalase depan. | Stok obat lengkap dengan nomor batch pabrik dan tanggal expired. |
| `19_stock_opname_audit_sheet.png` | Screen | Formulir audit stok opname obat fisik di rak apotek. | Pencocokan fisik sisa strip obat dan botol sirup. |
| `20_transactions_history_list.png` | Screen | Riwayat transaksi penebusan resep dokter & obat bebas. | Arsip transaksi obat apotek berdasarkan tanggal. |
| `21_supplier_pbf_purchase_order.png` | Sub-Screen | Surat pesanan barang ke Pedagang Besar Farmasi (PBF). | Form restock obat yang habis dengan nama distributor PBF resmi. |
| `22_customer_drug_allergy_record.png` | Component | Catatan riwayat alergi obat pelanggan pada profil pasien. | Peringatan merah alergi (contoh: Alergi Amoxicillin/Penisilin). |
| `23_settings_printer_setup.png` | Floating Sheet | Pengaturan printer thermal Bluetooth nota & etiket obat. | Setting printer untuk cetak struk belanja dan stiker etiket obat. |
| `24_settings_lan_pc_connect.png` | Screen | Layar Sambungkan ke Komputer (Web POS konter obat apotek). | Buka kasir apotek di layar komputer PC meja apoteker. |

---

## 🖨️ Direktori 07: 07_fotocopy (Varian Fotocopy & Percetakan - Biru Indigo)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_print_copy_services_grid.png` | Screen | Daftar tarif fotocopy BW/warna, jilid skripsi, laminating, ATK. | Kartu jasa percetakan dengan harga satuan per lembar. |
| `02_per_page_pricing_calculator.png` | Floating Sheet | Kalkulator hitung otomatis jasa cetak dokumen per lembar. | Input jumlah halaman $\times$ rangkap $\times$ ukuran kertas (A4/F4/A3). |
| `03_color_mode_paper_selector.png` | Component | Pilihan mode warna cetak: Hitam Putih (BW) vs Warna Laser. | Segmented selector penentu tarif harga otomatis. |
| `04_binding_laminating_options_sheet.png` | Floating Sheet | Modal pilihan jilid buku (lakban biasa, spiral kawat, hardcover). | Pilihan finishing jilid tinta emas dan laminating panas tebal. |
| `05_banner_meteran_calculator_dialog.png` | Modal Dialog | Kalkulator hitung spanduk / banner per meter persegi ($P \times L$). | Input panjang $\times$ lebar meter $\times$ bahan Flexi 280gr / 340gr. |
| `06_cart_fotocopy_order_active.png` | Floating Bar | Bar pesanan cetak dokumen & ATK terisi lembar cetak. | Total biaya cetak lembaran, jilid skripsi, dan ATK. |
| `07_pc_portal_file_queue_screen.png` | Screen | Tampilan antrean berkas kiriman pembeli di aplikasi HP. | Daftar berkas PDF/Word pelanggan yang masuk lewat portal toko. |
| `08_pc_portal_download_detail_modal.png` | Floating Sheet | Detail pesanan cetak pelanggan dan spesifikasi dokumen. | Nama pembeli, nomor WA, jumlah rangkap, dan tombol unduh. |
| `09_fotocopy_job_ticket_receipt.png` | Sub-Screen | Nota struk tanda terima antrean cetak dengan jam janji selesai. | Struk berisi nomor antrean pengerjaan cetak untuk pembeli. |
| `10_pc_portal_web_browser_view.png` | Browser View | Tampilan layar monitor PC operator saat buka `localhost:8080/portal-file`. | Antarmuka desktop monitor operator yang sedang klik "Unduh ke PC". |
| `11_payment_methods_sheet.png` | Floating Sheet | Layar checkout kasir percetakan/fotocopy. | Pilihan: Tunai, QRIS, Transfer Bank, dan Kasbon kantor/sekolah. |
| `12_cash_fast_tender_keypad.png` | Sub-Screen | Pembayaran tunai fotocopy & uang koin receh kembalian. | Tombol uang cepat dan perhitungan kembalian receh. |
| `13_qris_dynamic_display.png` | Sub-Screen | Tampilan kode QRIS dinamis di konter fotocopy. | QRIS pembayaran cetak kilat tanpa repot uang kembalian. |
| `14_receipt_thermal_preview.png` | Floating Sheet | Struk kasir fotocopy rincian jumlah lembar & jenis jilid. | Nota thermal rapi untuk dilampirkan pada dokumen pelanggan. |
| `15_fotocopy_daily_sales_recap.png` | Sub-Screen | Laporan omzet harian: pendapatan fotocopy, print, jilid, ATK. | Pembagian porsi pendapatan jasa mesin dengan jualan kertas/ATK. |
| `16_finance_cashflow_overview.png` | Screen | Buku Kas fotocopy (arus kas masuk jasa cetak vs operasional). | Ringkasan saldo kas toko dan pencatatan belanja kertas rim. |
| `17_finance_expense_sheet.png` | Floating Sheet | Catat belanja toner laser, tinta print, servis mesin fotocopy. | Formulir pengeluaran rutin percetakan. |
| `18_stock_paper_atk_inventory.png` | Screen | Stok kertas rim HVS (A4, F4, A3), plastik mika, lakban jilid. | Indikator stok rim kertas toko agar tidak kehabisan saat cetak massal. |
| `19_stock_opname_audit_sheet.png` | Screen | Formulir audit stok rim kertas dan catatan kertas rusak (*waste*). | Pencatatan limbah kertas cetak untuk audit modal toko. |
| `20_transactions_history_list.png` | Screen | Riwayat transaksi cetak dokumen & nota penjualan ATK. | Arsip nota pesanan cetak dan fotocopy pelanggan. |
| `21_supplier_paper_distributor.png` | Screen | Daftar agen distributor kertas rim HVS dan supplier toner mesin. | Kontak sales grosir kertas dan tempo pembayaran. |
| `22_attendance_operator_shift.png` | Screen | Layar presensi operator mesin fotocopy & staf desainer. | Catatan kehadiran staf percetakan. |
| `23_settings_printer_setup.png` | Floating Sheet | Pengaturan printer thermal Bluetooth 58mm/80mm kasir fotocopy. | Pairing printer Bluetooth dan opsi cetak nota tanda terima. |
| `24_settings_lan_pc_connect.png` | Screen | Layar Sambungkan ke Komputer (Web POS & Portal File PC). | Akses operator PC untuk kelola antrean cetak via browser PC. |

---

## 📱 Direktori 08: 08_servis (Varian Servis HP & Elektronik - Ungu Violet)

| File Asset | Tipe UI | Interaksi yang Ditangkap | Keterangan untuk AI Vision |
|:---|:---|:---|:---|
| `01_pos_sparepart_device_grid.png` | Screen | Katalog suku cadang LCD, baterai original, konektor charger. | Daftar komponen servis dengan ketersediaan stok fisik. |
| `02_unit_intake_receipt_sheet.png` | Floating Sheet | Form tanda terima servis masuk saat pelanggan menyerahkan unit. | Input merk/tipe HP, keluhan kerusakan, kelengkapan (unit, charger, dus). |
| `03_screen_pattern_pin_draw_sheet.png` | Floating Sheet | Lembar gambar pola kunci layar (pattern lock) atau PIN HP pelanggan. | Gambar grid 3x3 pola layar untuk pengujian teknisi setelah selesai servis. |
| `04_cost_estimate_down_payment_dialog.png` | Modal Dialog | Pencatatan estimasi total biaya servis dan uang muka (DP). | Input perkiraan harga sparepart + jasa perbaikan + uang muka pelanggan. |
| `05_cart_servis_order_active.png` | Floating Bar | Bar pesanan servis HP dan biaya jasa perbaikan aktif. | Total biaya suku cadang ditambah upah jasa servis teknisi. |
| `06_intake_claim_receipt_preview.png` | Sub-Screen | Cetak nota tanda terima servis resmi untuk dibawa pulang pelanggan. | Nota struk thermal berisi nomor tiket servis, syarat klaim, dan nomor WA. |
| `07_repair_status_pipeline_sheet.png` | Floating Sheet | Pengubahan status pengerjaan unit servis di meja teknisi. | Status bertingkat: Unit Masuk $\rightarrow$ Dicek $\rightarrow$ Tunggu Part $\rightarrow$ Selesai $\rightarrow$ Diambil. |
| `08_whatsapp_service_done_notify_modal.png` | Modal Dialog | Modal kirim notifikasi WA otomatis: "HP Anda sudah selesai diperbaiki". | Pesan otomatis rincian biaya yang harus dibayar saat pengambilan. |
| `09_service_warranty_card_print.png` | Sub-Screen | Cetak kartu garansi servis resmi (garansi 7 hari / 30 hari). | Syarat garansi: segel tidak rusak, tidak terkena air, nota asli dibawa. |
| `10_technician_commission_payout.png` | Sub-Screen | Rekapitulasi bagi hasil ongkos servis teknisi per unit selesai. | Perhitungan gaji atau persentase komisi bagi hasil teknisi servis. |
| `11_payment_methods_sheet.png` | Floating Sheet | Layar checkout sisa pelunasan biaya servis. | Pilihan: Tunai, QRIS, Transfer Bank, dan Potong DP. |
| `12_cash_fast_tender_keypad.png` | Sub-Screen | Pembayaran tunai pelunasan servis & kembalian cepat. | Kalkulator hitung pelunasan dikurangi uang muka (DP). |
| `13_qris_dynamic_display.png` | Sub-Screen | Tampilan kode QRIS dinamis di meja counter servis. | QRIS siap scan untuk pelunasan biaya perbaikan unit. |
| `14_receipt_thermal_preview.png` | Floating Sheet | Struk pelunasan servis resmi lengkap syarat garansi. | Nota thermal bukti lunas pengambilan unit dan masa garansi. |
| `15_servis_monthly_revenue_report.png` | Sub-Screen | Laporan laba usaha servis: keuntungan jasa perbaikan vs jual sparepart. | Rekap total unit selesai diperbaiki dan omzet bulanan konter servis. |
| `16_finance_cashflow_overview.png` | Screen | Buku Kas konter servis (arus kas masuk jasa vs operasional). | Ringkasan saldo kas konter dan pencairan upah teknisi. |
| `17_finance_expense_sheet.png` | Floating Sheet | Catat belanja timah solder, pasta flux, lem LCD, kawat jumper. | Formulir pengeluaran rutin alat servis meja teknisi. |
| `18_stock_sparepart_lcd_battery.png` | Screen | Stok komponen sparepart (LCD, baterai, fleksibel charger, obeng). | Daftar suku cadang siap pasang di etalase bengkel servis. |
| `19_stock_opname_audit_sheet.png` | Screen | Formulir audit stok komponen sparepart di laci teknisi. | Pencocokan stok fisik LCD dan baterai handphone. |
| `20_transactions_history_list.png` | Screen | Riwayat unit servis yang telah selesai & diambil pelanggan. | Arsip nota servis HP berdasarkan tanggal pengambilan. |
| `21_supplier_sparepart_distributor.png` | Screen | Buku kontak distributor sparepart HP dan supplier alat servis. | Kontak sales grosir LCD/baterai dan tempo pembayaran. |
| `22_attendance_technician_shift.png` | Screen | Layar presensi absensi teknisi servis dan staf kasir konter. | Catatan jam kerja harian teknisi perbaikan HP. |
| `23_settings_printer_setup.png` | Floating Sheet | Pengaturan printer thermal Bluetooth 58mm meja kasir servis. | Pairing printer Bluetooth dan opsi cetak tiket servis & kartu garansi. |
| `24_settings_lan_pc_connect.png` | Screen | Layar Sambungkan ke Komputer (Web POS & Meja Teknisi PC). | Akses teknisi di monitor komputer meja kerja untuk cek status unit. |

---

## 🎯 Panduan Khusus untuk AI Creator Agent (Vision Multimodal)

Ketika AI Creator Agent membaca pustaka visual per-varian ini:
1. **Zero Theme Mismatch**: Seluruh aset di dalam satu folder varian (misal `04_bengkel/`) memiliki warna tema, header, data seeded, dan terminologi yang 100% konsisten. DILARANG mencampurkan screenshot kelontong hijau ke video/konten bengkel merah.
2. **Konteks Spesifik Industri**:
   - Konten Kuliner $\rightarrow$ Ambil dari `02_fnb/` (ada Meja, KDS, Resep BOM).
   - Konten Laundry $\rightarrow$ Ambil dari `03_laundry/` (ada Timbangan kg desimal, Rak, Status Cuci).
   - Konten Bengkel $\rightarrow$ Ambil dari `04_bengkel/` (ada Nopol, KM, Mekanik, SPK Garansi).
   - Konten Salon $\rightarrow$ Ambil dari `05_salon/` (ada Hair Stylist, Komisi, Booking Kursi).
   - Konten Apotek $\rightarrow$ Ambil dari `06_apotek/` (ada Resep Dokter, Signa, Etiket 58mm).
   - Konten Fotocopy $\rightarrow$ Ambil dari `07_fotocopy/` (ada Hitung Lembar, Portal File PC).
   - Konten Servis HP $\rightarrow$ Ambil dari `08_servis/` (ada Tanda Terima, Pola 3x3, Status Servis).
   - Konten Kelontong $\rightarrow$ Ambil dari `01_kelontong/` (ada Grosir, Barcode, Kasbon, Shift).
3. **Penyusunan Konten Otomatis**:
   - Untuk **Video Tutorial 1 Menit**: Ambil `01_pos_...` $\rightarrow$ `06_domain_...` $\rightarrow$ `11_payment_methods_...` $\rightarrow$ `14_receipt_thermal_...` $\rightarrow$ `16_finance_cashflow_...`.
   - Untuk **Carousel Promosi 5 Slide**: Slide 1 Cover POS $\rightarrow$ Slide 2 Fitur Khas Varian $\rightarrow$ Slide 3 QRIS/Struk $\rightarrow$ Slide 4 Buku Kas/Laba $\rightarrow$ Slide 5 Lisensi Sekali Bayar Seumur Hidup.
