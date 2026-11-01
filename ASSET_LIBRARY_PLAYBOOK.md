# NUSA Kasir - Master Asset Library Playbook (Natural Mapping Blueprint)

Dokumen ini adalah cetak biru (*blueprint*) pustaka aset visual terstruktur per-varian usaha untuk NUSA Kasir. Pustaka ini digunakan sebagai referensi visual dan basis data CLI automation.

---

## 📂 Struktur Direktori Baku

Semua tangkapan layar wajib disimpan di direktori kerja CLI automation:
`C:\Users\ertyui\ZCodeProject\cli-automation\nusa-kasir\assets\content_library/`
(atau path relatif `assets/content_library/` dari root `cli-automation/nusa-kasir/`):
```text
assets/content_library/
├── 00_global_auth/          (Layar Onboarding & Aktivasi Universal)
├── 01_kelontong/            (Varian Kelontong: Oranye #F97316)
├── 02_fnb/                  (Varian F&B / Kafe / Resto: Merah Crimson #DC2626)
├── 03_laundry/              (Varian Laundry Kiloan/Satuan: Pink Rose #EC4899)
├── 04_bengkel/              (Varian Bengkel Motor: Kuning Amber #EAB308)
├── 05_salon/                (Varian Salon & Barbershop: Biru #3B82F6)
├── 06_apotek/               (Varian Apotek & Toko Obat: Hijau Emerald #10B981)
├── 07_fotocopy/             (Varian Fotocopy & Percetakan: Ungu Violet #8B5CF6)
└── 08_servis/               (Varian Servis HP & Elektronik: Biru Navy #152C63)
```

---

## 📸 Checklist Screenshot Per Varian (Natural Pacing)

Setiap screenshot harus diambil secara natural (beri jeda 1.5 – 2.0 detik setelah aksi untuk memastikan layar sudah ter-render sempurna):

### 🏛️ Direktori 00: `00_global_auth/` (Universal Onboarding)
| File Asset | Layar / Interaksi | Deskripsi Tampilan |
| :--- | :--- | :--- |
| `auth_01_welcome_onboarding.png` | Layar Selamat Datang | Tampilan pembuka aplikasi dengan logo NUSA dan slogan *"Cara Cerdas Kelola Usaha"*. |
| `auth_02_google_sign_in_sheet.png` | Pop-up Akun Google | Lembar pilihan akun Google Sign-In native (Mode Pro). |
| `auth_03_license_key_input.png` | Form Input Lisensi | Field input kode serial lisensi key lifetime (Mode Lite / 100% Offline). |
| `auth_04_activation_success_anim.png` | Modal Sukses | Animasi centang hijau status toko aktif permanen. |
| `auth_05_store_profile_setup.png` | Form Profil Toko | Form pengisian nama usaha, nomor WhatsApp, dan alamat toko. |
| `auth_06_variant_picker_sheet.png` | Pilihan Varian Usaha | Grid ikon 8 industri varian NUSA Kasir. |

---

### 🛒 Direktori 01 s/d 08: Layar Inti Per Varian Usaha
Lakukan pemetaan natural untuk setiap varian (`01_kelontong` sampai `08_servis`) dengan urutan berikut:

#### 1. Kasir & Transaksi POS
- `01_pos_catalog_grid.png`: Halaman utama kasir dengan foto produk Flow MCP terisi rapi sesuai varian.
- `02_category_filter_active.png`: Tampilan katalog saat salah satu tab kategori produk disentuh.
- `03_cart_items_active.png`: Bilah keranjang belanja bawah terisi 2–3 item transaksi.
- `04_item_detail_notes_sheet.png`: Lembar pop-up ubah jumlah quantity (+/-) atau diskon barang.

#### 2. Pembayaran & Struk
- `05_payment_checkout_methods.png`: Layar checkout kasir dengan pilihan metode bayar (Tunai, QRIS, Kasbon).
- `06_cash_tender_keypad.png`: Layar bayar tunai dengan tombol uang pas dan hitung kembalian cepat.
- `07_qris_dynamic_display.png`: Kode QRIS dinamis siap dipindai oleh pelanggan.
- `08_receipt_digital_preview.png`: Pratinjau struk thermal transaksi lengkap dengan rincian barang.
- `09_whatsapp_share_preview.png`: Lembar struk digital WhatsApp internal (`MockWhatsAppSheet`).

#### 3. Operasional & Fitur Spesifik Varian
- `10_variant_specialty_feature.png`: Fitur khas varian:
  * Kelontong: Lembar catatan kasbon / hutang pelanggan.
  * FnB: Denah meja tamu (*table management*) atau pesanan dapur (*KDS*).
  * Laundry: Pilihan tarif kiloan vs satuan atau status antrean cucian.
  * Bengkel: Form input plat nomor polisi / kilometer kendaraan dan nama mekanik.
  * Salon: Pilihan kapster/stylist atau komisi layanan.
  * Apotek: Rincian resep obat atau etiket aturan minum 58mm.
  * Fotocopy: Hitung tarif lembar print warna vs hitam-putih.
  * Servis: Form penerimaan unit servis, catatan kerusakan, dan pola kunci.

#### 4. Manajemen & Pengaturan
- `11_closing_shift_summary.png`: Rekapitulasi tutup shift kasir & total uang di laci.
- `12_stock_inventory_list.png`: Halaman daftar stok barang fisik dengan alert stok menipis.
- `13_transactions_history.png`: Riwayat daftar transaksi penjualan yang telah selesai.
- `14_settings_printer_setup.png`: Pengaturan koneksi printer Bluetooth thermal (58mm/80mm).
- `15_lan_pc_connect_screen.png`: Layar *"Sambungkan ke Komputer"* (Web POS kasir di laptop/PC).
- `16_asisten_nusa_offline_chat.png`: Layar chat interaktif bersama Asisten NUSA AI Offline.

---

## ⚠️ Larangan Mutlak Saat Pengambilan Screenshot

1. **DILARANG Screenshot Layar Blank / Loading**: Selalu pastikan spinner loading hilang sebelum memotret.
2. **DILARANG Screenshot Tertutup Dialog Usang**: Pastikan pop-up sebelumnya sudah ditutup sebelum memotret layar baru.
3. **DILARANG Menghasilkan File Berukuran Kembar**: Jika ukuran file dan tampilan identik dengan file sebelumnya, proses harus diulang (*re-take*).
4. **SIMPAN PERMANEN**: Seluruh screenshot yang sudah valid tetap berada di `assets/content_library/` untuk digunakan oleh CLI automation.
