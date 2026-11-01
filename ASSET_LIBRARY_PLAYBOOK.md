# NUSA Kasir - Master Asset Library Playbook (Production-Grade Natural Mapping)

Dokumen ini adalah cetak biru (*blueprint*) pustaka aset visual terstruktur untuk NUSA Kasir. Pustaka ini memetakan seluruh antarmuka operasional nyata aplikasi secara mendalam, manusiawi, dan bebas dari ketergesa-gesaan.

---

## 📂 Struktur Direktori Baku

Semua tangkapan layar wajib disimpan di direktori kerja CLI automation:
`C:\Users\ertyui\ZCodeProject\cli-automation\nusa-kasir\assets\content_library/`
(atau path relatif `assets/content_library/` dari root `cli-automation/nusa-kasir/`):

```text
assets/content_library/
├── 00_global_auth/                     (Autentikasi, Login, Onboarding & Setup)
├── 00_global_dashboard_settings/       (Pusat Kendali Toko, Header & Pengaturan)
├── 01_kelontong/                       (Varian Kelontong: Oranye #F97316)
├── 02_fnb/                             (Varian F&B / Kafe / Resto: Merah Crimson #DC2626)
├── 03_laundry/                         (Varian Laundry Kiloan/Satuan: Pink Rose #EC4899)
├── 04_bengkel/                         (Varian Bengkel Motor: Kuning Amber #EAB308)
├── 05_salon/                           (Varian Salon & Barbershop: Biru #3B82F6)
├── 06_apotek/                          (Varian Apotek & Toko Obat: Hijau Emerald #10B981)
├── 07_fotocopy/                        (Varian Fotocopy & Percetakan: Ungu Violet #8B5CF6)
└── 08_servis/                          (Varian Servis HP & Elektronik: Biru Navy #152C63)
```

---

## 📸 Checklist Screenshot Lengkap

### 🏛️ Direktori 00: `00_global_auth/` (Autentikasi, Onboarding & Setup)
| File Asset | Layar / Interaksi | Deskripsi Tampilan |
| :--- | :--- | :--- |
| `01_welcome_login_screen.png` | Layar Masuk / Login | Form login email dan password (*"Masuk untuk lanjut ke aplikasi"*). |
| `02_register_account_sheet.png` | Form Pendaftaran | Lembar pendaftaran akun toko baru (*"Belum punya akun? Daftar"*). |
| `03_forgot_password_sheet.png` | Lupa Kata Sandi | Dialog pemulihan kata sandi via email. |
| `04_google_sign_in_sheet.png` | Google Sign-In | Lembar pilihan akun Google native (*Mode Pro*). |
| `05_license_lite_activation.png` | Aktivasi NUSA Lite | Form input email & serial key lisensi seumur hidup (*Mode Lite / Offline*). |
| `06_restore_cloud_backup.png` | Pulihkan Cadangan Cloud | Dialog otomatis deteksi backup di Cloudflare R2 / Google Drive. |
| `07_activation_success_modal.png` | Status Toko Aktif | Modal konfirmasi aktivasi toko sukses permanen. |
| `08_store_setup_profile.png` | Form Setup Toko | Setup awal pasca aktivasi (*Nama Usaha, Nama Pemilik, PIN Owner 6-digit*). |
| `09_pin_keypad_attendance.png` | Masukkan PIN Staf | Keypad PIN login karyawan pendukung Biometrik, scan kartu NFC, dan scan Barcode ID. |

---

### ⚙️ Direktori 00-B: `00_global_dashboard_settings/` (Pusat Kendali Toko, Header & Pengaturan)
| File Asset | Layar / Interaksi | Deskripsi Tampilan |
| :--- | :--- | :--- |
| `01_dashboard_front_card.png` | Dashboard Utama (Default) | Tampilan utama kasir dengan **Kartu Depan (*Front Card*) Profil Staf Aktif**: foto avatar, nama, role, jam masuk kerja, status presensi, dan grid menu 3D lengkap. |
| `02_dashboard_flipped_card.png` | Dashboard Utama (Flipped) | Kartu atas dibalik menampilkan **Ringkasan Hari Ini**: Laba Penjualan, Omzet, Transaksi, dan Selisih Uang Laci Kasir. |
| `03_cloud_sync_modal_sheet.png` | Modal Sinkronisasi Cloud | Sheet yang terbuka saat **ikon awan di header di-tap**: status awan hijau/kuning/merah, waktu sync terakhir, tombol *Tarik Data Cloud (Pull Now)*, *Unggah Data Lokal (Push Now)*, dan status WebSocket RoomDO realtime. |
| `04_notification_drawer.png` | Lonceng Notifikasi | Drawer yang terbuka saat **ikon lonceng di header di-tap**: pengingat absen harian, alert stok menipis, pesanan toko online baru, dan status in-app update APK. |
| `05_branch_switcher_sheet.png` | Pemilih Cabang Toko | Lembar ganti cabang usaha instan (Multi-Cabang). |
| `06_closing_shift_real_modal.png` | Tutup Shift Kasir Riil | Modal tutup shift: input hitungan uang kas fisik di laci per pecahan (Rp 100k s/d Rp 1k), hitung selisih kas fisik vs sistem, dan cetak struk rekap kasir. |
| `07_feature_management_tab.png` | Kelola Fitur (Tab 1) | Layar `Fitur & Hak Akses` Tab 1: toggle switch on/off 26 fitur toko dan drag-and-drop urutan menu dashboard. |
| `08_role_permissions_rbac.png` | Hak Akses Role (Tab 2) | Layar `Fitur & Hak Akses` Tab 2: tree-view checklist perizinan role (Owner, Manager, Kasir, Admin, Stylist, Teknisi). |
| `09_store_data_screen.png` | Form Data Toko | Form profil bisnis lengkap: nama toko, alamat fisik, nomor WhatsApp, pemilik, dan logo toko. |
| `10_payment_settings_qris.png` | Pengaturan Pembayaran | Form upload gambar QRIS toko (decode otomatis Tag 54 dinamis) dan daftar rekening multi-bank & e-wallet. |
| `11_receipt_wysiwyg_settings.png` | Pengaturan Struk WYSIWYG | Pratinjau struk thermal live realtime, switch ukuran kertas 58mm vs 80mm, upload logo struk hitam-putih, teks header & footer ucapan terima kasih, dan toggle tampilkan info toko. |
| `12_printer_bluetooth_sheet.png` | Printer Bluetooth SPP | Sheet pindai printer thermal Bluetooth, pasangkan perangkat, auto-print, dan tombol tes print. |
| `13_lan_pos_web_screen.png` | Sambungkan ke Komputer | Layar LAN POS: QR Code untuk dipindai browser laptop/PC, alamat IP lokal port 8080, sesi terhubung, dan akses remote tunnel. |
| `14_online_store_setup.png` | Setup Toko Online | Pengaturan web storefront: custom slug URL toko (`/toko/[slug]`), jam operasional, WA pesanan, dan kurir. |
| `15_online_orders_pipeline.png` | Pesanan Online Masuk | Manajemen order online pelanggan: tab Menunggu, Diterima, Diproses, Dikirim, Selesai. |
| `16_online_storefront_view.png` | Pratinjau Toko Online Web | Tampilan website belanja online pelanggan di browser smartphone. |
| `17_id_card_studio_screen.png` | Studio Kartu ID | Studio pembuat dan pencetak kartu member pelanggan & ID Card staf fisik ber-barcode/QR. |
| `18_promo_design_studio.png` | Studio Desain Promosi | Pembuat poster promosi, diskon, dan kupon voucher toko ala Canva di HP. |
| `19_backup_restore_screen.png` | Backup & Restore Terenkripsi | Layar pencadangan database lokal terenkripsi NUS1 AES-256-GCM dan sinkronisasi otomatis Cloudflare R2. |

---

### 🛒 Direktori 01: `01_kelontong/` (Sembako & Ritel Rute Tradisional)
- `01_pos_catalog_grid.png`: Halaman utama kasir kelontong dengan produk sembako dan foto tajam.
- `02_category_filter_active.png`: Filter kategori produk (Beras, Minyak, Mie, Bumbu).
- `03_cart_items_active.png`: Keranjang belanja terisi barang sembako.
- `04_item_detail_notes_sheet.png`: Lembar pop-up ubah harga khusus atau diskon satuan item.
- `05_grosir_tier_pricing_sheet.png`: **Harga Grosir Bertingkat** (diskon otomatis per lusin, renteng, dus, karton).
- `06_shelf_price_tag_print.png`: **Cetak Label Rak / Price Tag** dengan barcode barang untuk ditempel di etalase.
- `07_barcode_scanner_camera_active.png`: Layar aktif pemindai barcode kamera HP super cepat.
- `08_kasbon_customer_book_sheet.png`: **Buku Kasbon / Catatan Hutang Pelanggan** lengkap dengan tanggal jatuh tempo.
- `09_debt_installments_history.png`: Riwayat pembayaran cicilan hutang dan bukti pelunasan.
- `10_payment_checkout_methods.png`: Checkout kasir pilihan Tunai, QRIS, Transfer, dan Kasbon.
- `11_cash_tender_keypad.png`: Layar bayar tunai dengan tombol uang pas dan hitung kembalian cepat.
- `12_qris_dynamic_display.png`: Kode QRIS dinamis siap scan.
- `13_receipt_thermal_preview.png`: Pratinjau struk thermal belanja sembako.
- `14_whatsapp_share_preview.png`: Struk digital WhatsApp.
- `15_stock_inventory_list.png`: Daftar stok fisik sembako dengan alert stok menipis.
- `16_transactions_history.png`: Riwayat transaksi selesai.
- `17_finance_cashflow_overview.png`: Arus kas uang masuk dan keluar.
- `18_finance_expense_sheet.png`: Catatan pengeluaran operasional toko.
- `19_product_catalog_management.png`: Daftar kelola produk dan harga beli/jual.
- `20_product_add_edit_form.png`: Form tambah produk baru dan scan barcode otomatis.
- `21_customer_crm_directory.png`: Buku kontak pelanggan warung.
- `22_employee_attendance_roster.png`: Presensi shift jaga warung.
- `23_suppliers_vendor_contacts.png`: Daftar supplier distributor sembako.
- `24_asisten_nusa_offline_chat.png`: Konsultasi AI kasir offline.

---

### 🍽️ Direktori 02: `02_fnb/` (Resto, Kafe, Kopi & Kuliner)
- `01_pos_catalog_grid.png`: Halaman kasir FnB foto makanan lezat dan tab kategori (*Makanan Utama, Minuman, Camilan*).
- `02_category_filter_active.png`: Filter kategori menu aktif.
- `03_cart_items_active.png`: Keranjang belanja meja FnB.
- `04_item_detail_notes_sheet.png`: Catatan khusus koki dapur (*"pedas sedang, tanpa daun bawang"*).
- `05_order_flow_meja_picker_sheet.png`: **Alur Pesanan & Meja FnB** (*Makan di Tempat / Dine In, Bungkus / Take Away, Delivery, Reservasi*).
- `06_table_reservasi_grid.png`: **Denah & Daftar Meja Tamu** (Meja Kosong, Terisi, Dipesan, kapasitas kursi).
- `07_table_active_order_detail.png`: Detail pesanan meja yang sedang berjalan (*Hold Bill*).
- `08_table_add_edit_form.png`: Form tambah meja baru atau atur denah area lantai.
- `09_kitchen_display_system_kds.png`: **Kitchen Display System (KDS) Digital**: tiket pesanan dapur real-time (*Menunggu ➔ Dimasak ➔ Siap Diantar*).
- `10_recipes_bom_management.png`: **Manajemen Resep & HPP Bahan Baku**: komposisi porsi resep, kalkulasi HPP otomatis, dan margin laba.
- `11_raw_materials_inventory.png`: Stok bahan baku mentah (gram, kg, liter, butir).
- `12_payment_checkout_methods.png`: Checkout kasir FnB.
- `13_split_bill_dialog.png`: **Fitur Split Bill**: bagi tagihan meja secara rata atau pilih per orang.
- `14_split_bill_dynamic_qris.png`: **QRIS Dinamis Split Bill** terpisah per orang yang membayar.
- `15_cash_tender_keypad.png`: Bayar tunai dan hitung uang kembalian.
- `16_receipt_thermal_preview.png`: Pratinjau struk kasir dengan tombol **"Cetak Struk Dapur"**.
- `17_receipt_kitchen_order_ticket.png`: **Struk Dapur Fisik (KOT)** khusus koki tanpa harga.
- `18_whatsapp_share_preview.png`: Struk digital WhatsApp.
- `19_stock_inventory_list.png`: Stok minuman & makanan kemasan.
- `20_transactions_history.png`: Riwayat transaksi resto.
- `21_finance_cashflow_overview.png`: Arus kas resto.
- `22_finance_expense_sheet.png`: Pengeluaran belanja pasar harian.
- `23_product_add_edit_form.png`: Form tambah menu resto baru.
- `24_customer_crm_directory.png`: Data pelanggan langganan.
- `25_asisten_nusa_offline_chat.png`: Asisten NUSA AI Offline.

---

### 🧺 Direktori 03: `03_laundry/` (Laundry Kiloan & Satuan)
- `01_pos_laundry_services_grid.png`: Katalog layanan laundry (Cuci Kering, Setrika, Bedcover, Jas).
- `02_laundry_weight_scale_input.png`: **Pilihan Tarif Kiloan vs Satuan & Input Timbangan Berat Cucian** (e.g. 3.5 kg x Rp 7.000).
- `03_laundry_perfume_and_rack_sheet.png`: **Pilihan Aroma Parfum Pewangi & Nomor Rak Cucian** (e.g. Akasia, Rak A2).
- `04_laundry_status_pipeline_screen.png`: **Pipeline Status Cucian**: *Masuk ➔ Antre Cuci ➔ Dikeringkan ➔ Disetrika ➔ Siap Diambil ➔ Selesai*.
- `05_laundry_thermal_tag_print.png`: **Cetak Label Tag Baju Kertas Tahan Air** untuk disematkan di pakaian pelanggan.
- `06_laundry_whatsapp_ready_notify.png`: **WhatsApp Otomatis**: *"Halo Kak, cucian Anda sudah rapi dan siap diambil..."*.
- `07_payment_checkout_methods.png`: Checkout pembayaran cucian (Bisa bayar di muka / DP atau bayar saat ambil).
- `08_cash_tender_keypad.png`: Hitung tunai & kembalian.
- `09_qris_dynamic_display.png`: QRIS dinamis laundry.
- `10_receipt_thermal_preview.png`: Struk tanda terima cucian dengan rincian berat dan aroma.
- `11_whatsapp_share_preview.png`: E-struk WA.
- `12_stock_inventory_list.png`: Stok deterjen, softener, dan plastik packing.
- `13_transactions_history.png`: Riwayat order laundry.
- `14_finance_cashflow_overview.png`: Arus kas masuk dan keluar.
- `15_finance_expense_sheet.png`: Biaya operasional sabun, air, dan listrik.
- `16_product_add_edit_form.png`: Tambah tarif layanan baru.
- `17_customer_crm_directory.png`: Database pelanggan laundry.
- `18_asisten_nusa_offline_chat.png`: Konsultasi cerdas Asisten NUSA.

---

### 🔧 Direktori 04: `04_bengkel/` (Bengkel Motor & Mobil)
- `01_pos_sparepart_service_grid.png`: Katalog gabungan Jasa Bengkel dan Sparepart motor/mobil.
- `02_bengkel_ticket_intake_form.png`: **Form Tiket Servis Bengkel**: Input Plat Nomor Polisi (e.g. B 1234 XYZ), Merk/Tipe Kendaraan, dan Kilometer (Odometer).
- `03_bengkel_service_queue_pipeline.png`: **Antrean Servis Bengkel**: *Diagnosa ➔ Estimasi ➔ Pengerjaan ➔ Selesai*.
- `04_bengkel_parts_and_labor_cart.png`: Keranjang gabungan sparepart (Oli MPX + Kampas) dan ongkos jasa mekanik.
- `05_bengkel_mechanic_assignment.png`: Penugasan Mekanik penanggung jawab & bagi hasil komisi montir.
- `06_bengkel_receipt_thermal.png`: Struk servis memuat plat nomor, KM kendaraan, rincian part, dan ongkos pasang.
- `07_bengkel_service_reminder_wa.png`: **Pengingat Servis Berkala WhatsApp**: jadwal ganti oli rutin 2.000 KM berikutnya.
- `08_payment_checkout_methods.png`: Checkout pembayaran bengkel.
- `09_cash_tender_keypad.png`: Bayar tunai bengkel.
- `10_qris_dynamic_display.png`: QRIS bengkel.
- `11_stock_sparepart_inventory.png`: Stok suku cadang, oli, kampas, busi.
- `12_transactions_history.png`: Riwayat transaksi servis bengkel.
- `13_finance_cashflow_overview.png`: Arus kas bengkel.
- `14_finance_expense_sheet.png`: Belanja sparepart grosir.
- `15_customer_crm_directory.png`: Buku pemilik kendaraan langganan.
- `16_asisten_nusa_offline_chat.png`: Asisten NUSA AI Offline.

---

### 💇 Direktori 05: `05_salon/` (Salon, Barbershop & Spa)
- `01_pos_treatment_services_grid.png`: Menu layanan potong rambut, creambath, coloring, treatment.
- `02_booking_appointment_screen.png`: **Layar Booking & Reservasi Jadwal Tamu Salon**.
- `03_booking_add_form_sheet.png`: Form booking jam kedatangan tamu, layanan yang dipilih, dan stylist pilihan.
- `04_stylist_assignment_and_commission.png`: Penentuan kapster/stylist per layanan dan perhitungan komisi kerja.
- `05_stylist_performance_report.png`: **Laporan Kinerja & Omzet Per Stylist** (`/laporan/stylist`).
- `06_stylist_personal_earnings_screen.png`: **Layar Pendapatan Saya** untuk kapster melihat komisi harian (`/pendapatan-saya`).
- `07_payment_checkout_methods.png`: Checkout kasir salon.
- `08_cash_tender_keypad.png`: Pembayaran tunai salon.
- `09_qris_dynamic_display.png`: QRIS salon.
- `10_receipt_thermal_preview.png`: Struk perawatan salon mencantumkan nama kapster.
- `11_stock_inventory_list.png`: Stok shampoo, pomade, pewarna rambut.
- `12_transactions_history.png`: Riwayat transaksi salon.
- `13_finance_cashflow_overview.png`: Arus kas salon.
- `14_finance_expense_sheet.png`: Biaya perlengkapan salon.
- `15_customer_crm_directory.png`: Database pelanggan member salon.
- `16_asisten_nusa_offline_chat.png`: Konsultasi Asisten NUSA.

---

### 💊 Direktori 06: `06_apotek/` (Apotek & Toko Obat)
- `01_pos_otc_medicine_catalog.png`: Katalog obat bebas (OTC), vitamin, dan suplemen.
- `02_prescription_management_screen.png`: **Layar Kelola Resep Dokter**: status *Baru ➔ Diproses ➔ Siap ➔ Diambil*.
- `03_prescription_intake_form.png`: **Form Resep Dokter**: Nama Dokter, SIP, Nama Pasien, Usia, Berat Badan (BB).
- `04_prescription_signa_chips.png`: **Chip Signa Cepat**: aturan pakai obat (*"3x1 tablet sesudah makan"*, *"tetes mata kiri & kanan"*).
- `05_prescription_compound_paten.png`: Form obat racikan (puyer/kapsul) vs obat paten.
- `06_medicine_thermal_label_58mm.png`: **Cetak Label Etiket Obat Thermal 58mm** untuk ditempel di botol/plastik obat.
- `07_prescription_copy_apograph.png`: **Cetak Salinan Resep (Apograph)** resmi apotek.
- `08_medicine_batch_expiry_alert.png`: Pelacakan nomor batch pabrik dan tanggal kedaluwarsa obat.
- `09_payment_checkout_methods.png`: Checkout kasir apotek.
- `10_cash_tender_keypad.png`: Bayar tunai obat.
- `11_qris_dynamic_display.png`: QRIS apotek.
- `12_receipt_thermal_preview.png`: Struk pembelian obat dengan info aturan pakai.
- `13_stock_inventory_list.png`: Stok obat fisik dan peringatan stok obat menipis.
- `14_transactions_history.png`: Riwayat transaksi apotek.
- `15_finance_cashflow_overview.png`: Arus kas apotek.
- `16_finance_expense_sheet.png`: Pembelian obat ke PBF (Pedagang Besar Farmasi).
- `17_customer_crm_directory.png`: Data pasien apotek.
- `18_asisten_nusa_offline_chat.png`: Asisten NUSA AI Offline.

---

### 🖨️ Direktori 07: `07_fotocopy/` (Fotocopy & Percetakan)
- `01_pos_paper_atk_grid.png`: Katalog kertas, ATK, map, dan alat tulis kantor.
- `02_print_order_calculator_sheet.png`: **Kalkulator Order Cetak**: hitung lembar fotocopy/print x tarif per lembar.
- `03_print_paper_and_binding_picker.png`: Pilihan kertas (*A4, F4 / Folio, A3, Warna vs BW*) dan jenis jilid (*Mika, Spiral, Lakban, Hardcover*).
- `04_print_order_pipeline_screen.png`: Antrean pekerjaan cetak: *Pending ➔ Sedang Dicetak ➔ Selesai ➔ Diambil*.
- `05_print_portal_qr_upload_screen.png`: **Portal Kirim File Pelanggan (`/print-portal`)**: upload dokumen via browser HP pelanggan lewat scan QR code lokal.
- `06_payment_checkout_methods.png`: Checkout kasir fotocopy.
- `07_cash_tender_keypad.png`: Pembayaran tunai kasir fotocopy.
- `08_qris_dynamic_display.png`: QRIS fotocopy.
- `09_receipt_thermal_preview.png`: Struk order fotocopy dan print.
- `10_stock_inventory_list.png`: Stok rim kertas, tinta toner printer, dan ATK.
- `11_transactions_history.png`: Riwayat order cetak.
- `12_finance_cashflow_overview.png`: Arus kas fotocopy.
- `13_finance_expense_sheet.png`: Pembelian kertas rim dan isi ulang toner.
- `14_customer_crm_directory.png`: Pelanggan langganan percetakan.
- `15_asisten_nusa_offline_chat.png`: Konsultasi Asisten NUSA.

---

### 📱 Direktori 08: `08_servis/` (Servis HP & Elektronik)
- `01_pos_catalog_grid.png`: Katalog sparepart dan jasa perbaikan device.
- `02_service_tickets_pipeline.png`: **Pipeline Tiket Servis Lengkap**: *Diagnosa ➔ Estimasi ➔ Perbaikan ➔ Selesai ➔ Diambil*.
- `03_service_intake_form.png`: **Form Tiket Servis Baru**: Input tipe HP/Laptop, keluhan kerusakan, dan kelengkapan unit bawaan.
- `04_service_pattern_pin_draw.png`: **Kanvas Gambar Pola Kunci Layar HP (Pattern Lock / PIN)** milik pelanggan.
- `05_service_cost_dp_sheet.png`: Down Payment (DP) tanda jadi servis dan estimasi total biaya.
- `06_service_parts_labor_split.png`: Rincian biaya jasa pengerjaan teknisi ditambah sparepart (LCD, baterai, konektor).
- `07_service_status_transition_sheet.png`: Lembar pembaruan status pengerjaan tiket servis.
- `08_service_thermal_claim_receipt.png`: **Cetak Struk Tanda Terima Klaim Servis Barcode** untuk dibawa pulang pelanggan.
- `09_service_whatsapp_notify_done.png`: **WhatsApp Otomatis**: *"Halo Kak, unit iPhone/HP Anda sudah selesai diservis dan dapat diambil..."*.
- `10_service_warranty_card_preview.png`: **Kartu Garansi Servis 30 Hari**.
- `11_service_technician_commission.png`: Penugasan teknisi dan komisi pengerjaan.
- `12_payment_checkout_methods.png`: Checkout pelunasan servis.
- `13_cash_tender_keypad.png`: Bayar tunai servis.
- `14_qris_dynamic_display.png`: QRIS servis.
- `15_receipt_thermal_preview.png`: Struk pelunasan servis thermal.
- `16_stock_sparepart_inventory.png`: Stok sparepart LCD, IC, baterai, konektor charger.
- `17_transactions_history.png`: Riwayat pengerjaan unit servis.
- `18_finance_cashflow_overview.png`: Arus kas servis.
- `19_finance_expense_sheet.png`: Pembelian sparepart kanibalan / grosir.
- `20_customer_crm_directory.png`: Database pelanggan servis.
- `21_asisten_nusa_offline_chat.png`: Konsultasi cerdas Asisten NUSA.

---

## ⚠️ Aturan Mutlak Operasional Screenshot

1. **Jeda Render Manusiawi (1.5 – 2.5 Detik)**: Beri waktu aplikasi me-render animasi transisi, lembar pop-up, dan data katalog secara utuh sebelum mengambil screenshot.
2. **Display ID Layar Utama Samsung Flip/Fold**: Selalu targetkan layar bagian dalam dengan Display ID `4630947232161729154`.
3. **Buka Sheet / Modal Riil**: Dilarang hanya memotret menu daftar luar. Wajib klik tombol atau sheet target (klik ikon awan sync, klik lonceng notifikasi, klik menu sub-pengaturan, klik fitur KDS/Resep/Tiket) agar antarmuka interaktifnya terpotret sempurna.
4. **Zero Script Harvester Blind Loop**: Dilarang menggunakan script otomatisasi buta tanpa pengawasan visual. Navigasi dijalankan secara natural dan terkontrol.
5. **Simpan Permanen**: Seluruh tangkapan layar yang sah tersimpan rapi di direktori `assets/content_library/` untuk digunakan oleh CLI automation.
