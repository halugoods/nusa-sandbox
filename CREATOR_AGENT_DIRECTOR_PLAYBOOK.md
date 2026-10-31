# Playbook Panduan AI Creator Agent: Orkestrasi Rekam Layar & Demo Dinamis (NUSA Kasir)

Dokumen ini adalah acuan baku operasional untuk AI Creator Agent dalam mengeksekusi demo aplikasi, screen recording ADB, dan produksi konten visual NUSA Kasir secara presisi, mulus, dan 100% bebas dari kesan palsu (*zero slop*).

---
---

## 2. Matriks Resmi Lisensi: Lite vs Pro

Creator Agent WAJIB memahami perbedaan hakiki antara mode Lite dan Pro saat menyusun skrip atau mendemokan fitur:

| Fitur / Kemampuan | NUSA Kasir Lite | NUSA Kasir Pro |
| :--- | :---: | :---: |
| **Harga Lisensi** | **Rp 249.000 Sekali Bayar Seumur Hidup** | **Rp 499.000 Sekali Bayar Seumur Hidup** |
| **Biaya Bulanan / Sewa** | **Rp 0 (Tanpa Biaya Tambahan)** | **Rp 0 (Tanpa Biaya Tambahan)** |
| **Konektivitas Internet** | **100% Offline Murni (0 Kuota Internet)** | **Offline Tetap Jalan + Cloud Sync Otomatis** |
| **Model Akun & Login** | Aktivasi Email + Lisensi Key (Tanpa Google) | Google Sign-In + Profil Cloud |
| **Kasir & Penjualan POS Cepat** | ✅ Lengkap (Barcode, Diskon, Pajak) | ✅ Lengkap (Barcode, Diskon, Pajak) |
| **Cetak Struk Bluetooth (58/80mm)**| ✅ Lengkap (Semua Printer Thermal) | ✅ Lengkap (Semua Printer Thermal) |
| **Katalog Produk & Manajemen Stok** | ✅ Lengkap (Kategori, Varian, Pengingat) | ✅ Lengkap (Kategori, Varian, Pengingat) |
| **Catat Pelanggan & Hutang-Piutang** | ✅ Lengkap (Jatuh Tempo & Riwayat) | ✅ Lengkap (Jatuh Tempo & Riwayat) |
| **Laporan Omzet, Laba & Terlaris** | ✅ Lengkap (Tersimpan Lokal di HP) | ✅ Lengkap (Lokal + Dashboard Cloud) |
| **Backup & Pemulihan Data** | ✅ Backup Lokal SQLite/NUS1 | ✅ Cloud Backup Otomatis (Cloudflare R2) + Lokal |
| **Sinkronisasi Kasir & Owner (Multi-HP)**| ❌ (1 HP Standalone) | ✅ Sinkron Realtime <1 Detik (Kasir & Owner Beda HP) |
| **Asisten NUSA (AI Assistant Cerdas)** | ❌ | ✅ Analisis Penjualan & Chat Rekomendasi Bisnis |
| **Toko Online / Web Storefront Mandiri** | ❌ | ✅ Website Toko Online per-toko (/toko/[slug]) |
| **Export Spreadsheet (Excel / Google Sheets)** | ❌ | ✅ Export Otomatis ke Google Sheets & Excel |
| **Multi-Cabang & Manajemen Karyawan** | ❌ (1 Toko / 1 Akun) | ✅ Multi-Cabang & Hak Akses PIN Kasir |
| **Metode Pembayaran QRIS** | ✅ QRIS Statis (Scan & Bayar) | ✅ QRIS Dinamis & QRIS Statis |


## 1. Filosofi & Karakteristik Produksi

1. **Durasi 100% Dinamis & Narrative-Driven**:
   - Dilarang keras mematok durasi kaku (misal 15 detik, 30 detik, atau 60 detik mati).
   - Panjang video dan jeda per beat sepenuhnya ditentukan oleh alur cerita naskah, kompleksitas transaksi, dan ritme natural suara pengisi suara (*voiceover* 1.0x native speed).
2. **Tampilan 100% Like-Production**:
   - Aplikasi sandbox terlihat identik seutuhnya dengan aplikasi resmi di Google Play Store.
   - Tidak ada label, banner, atau teks tiruan ("Simulasi", "Sandbox", "Privacy Shield", atau "Mock").
   - Semua pop-up sistem (Photo Picker, Contact Picker, Google Sign-In, WhatsApp Share) adalah kloning 1:1 antarmuka asli Android & One UI.
3. **Privasi Mutlak & Anti-Bocor Data**:
   - WhatsApp asli pengguna tidak pernah dibuka saat demo. Modul `MockWhatsAppSheet` menangani simulasi struk WhatsApp di dalam layar aplikasi secara tertutup.
   - Foto dan nomor kontak pribadi perangkat aman 100% dari rekaman.

---

## 2. Kalibrasi Perangkat: Samsung Galaxy Z Flip 3 & Emulator Dinamis

Direktor otomasi (`tools/nusa_director.py`) mendeteksi resolusi layar otomatis via `adb shell wm size`.

### Profil Acuan Utama: Samsung Galaxy Z Flip 3
- **Resolusi Fisik**: `1080 x 2640` piksel.
- **Rasio Layar**: `22:9` (Ultra-tall).
- **Safe Zone**:
  - Top status bar: 120 px.
  - Bottom navigation bar: 140 px.
- **Sistem Koordinat Dinamis**:
  Semua koordinat di `tools/action_matrix.json` menggunakan format persentase normalisasi `(x_pct, y_pct)` dari rentang `0.0` sampai `1.0`. Jika dieksekusi di HP fisik Samsung Z Flip 3, emulator Android Studio, maupun cloud phone, sistem mengalikan persentase terhadap lebar ($W$) dan tinggi ($H$) fisik secara matematis presisi tanpa offset meleset.

---

## 3. Direktori Cheat Code Senyap (Headless Trigger)

Creator Agent mengeksekusi transisi lisensi, login, dan konfirmasi tanpa perlu memencet tombol aneh di layar.

| Kebutuhan Alur | Perintah ADB Intent Headless | Efek Visual di Layar |
| :--- | :--- | :--- |
| **Bypass Login & Lisensi Pro** | `adb shell am start -n com.nusa.kelontong/com.example.nusa_kasir.MainActivity --es action AUTH_PRO` | Langsung masuk ke layar Kasir Pro dengan katalog aktif. |
| **Bypass Login & Lisensi Lite** | `adb shell am start -n com.nusa.kelontong/com.example.nusa_kasir.MainActivity --es action AUTH_LITE` | Langsung masuk ke layar Kasir Lite (mode offline 0 biaya cloud). |
| **Mulai Tutorial Onboarding Baru** | `adb shell am start -n com.nusa.kelontong/com.example.nusa_kasir.MainActivity --es action ONBOARDING` | Mengosongkan sesi dan membuka layar Aktivasi / Sambutan pertama. |
| **Ganti Varian Usaha Instan** | `adb shell am start -n com.nusa.kelontong/com.example.nusa_kasir.MainActivity --es variant nusa-{variant} --ez pro true` | Mengubah tema, warna primer, dan katalog ke varian target (< 0.5s). |

---

## 4. Alur Koreografi Aksi Berdasarkan Naskah

### Fase 1: Memilih Produk & Keranjang Belanja
1. Ketuk tab kategori atau cari produk:
   `director.tap("pos_screen.category_tab_1")`
2. Tambahkan 2–3 item ke keranjang belanja:
   `director.tap("pos_screen.product_item_r1_c1")`
   `director.wait(0.4)`
   `director.tap("pos_screen.product_item_r1_c2")`
   `director.wait(0.3)`
3. Buka ringkasan keranjang / tekan tombol bayar:
   `director.tap("pos_screen.btn_bayar_checkout")`

### Fase 2: Pembayaran QRIS Dinamis atau Tunai
- **Opsi QRIS Dinamis**:
  1. Pilih tab QRIS: `director.tap("checkout_screen.tab_qris")`.
  2. Layar menampilkan QRIS resmi dan status elegan: *"Menunggu pembayaran dari pelanggan..."*.
  3. Konfirmasi pembayaran otomatis: ketuk indikator QRIS `director.tap("checkout_screen.qris_status_pill")`.
- **Opsi Tunai**:
  1. Pilih nominal cepat (misal Rp 100.000): `director.tap("checkout_screen.nominal_100k")`.
  2. Tekan konfirmasi bayar: `director.tap("checkout_screen.btn_konfirmasi_bayar")`.

### Fase 3: Lembar Struk & Berbagi Nota
1. Muncul lembar struk interaktif dengan suara denting sukses (*success chime*).
2. Cetak Struk via Printer Bluetooth: `director.tap("receipt_screen.btn_print_thermal")`.
3. Bagikan Struk ke WhatsApp Pelanggan:
   `director.tap("receipt_screen.btn_share_wa")`
   Layar WhatsApp internal (`MockWhatsAppSheet`) meluncur mulus dari bawah menampilkan nama pelanggan (*Budi Santoso*), jam pengiriman, dan centang dua biru dengan format teks nota rapi tebal-miring.
4. Selesai dan kembali ke kasir untuk transaksi baru:
   `director.tap("receipt_screen.btn_transaksi_baru")`.

---

## 5. Rujukan Slogan & Standar Bahasa

- **Slogan Resmi Merek**: **"Cara Cerdas Kelola Usaha"**
- Dilarang menggunakan istilah teknis pengembang (SQLite, Drift, Cloudflare, API, Backend).
- Dilarang memakai frasa AI slop yang kaku ("orkestrasi paripurna", "rekayasa ekosistem", "aplikasi serba 1 HP"). Gunakan bahasa pedagang Indonesia yang ramah, ringkas, dan solutif.
