# NUSA Kasir Creator Sandbox v2.3.0+171 — Studio & Automation Edition

Build resmi **NUSA Kasir Creator Sandbox (Unified 16-in-1)** khusus untuk pembuatan konten video tutorial, demonstrasi publik, dan otomasi ADB screen recording.

> **1 Aplikasi untuk Seluruh Kebutuhan**: Cukup install 1 file APK (`nusa-sandbox.apk`) untuk mencakup seluruh **8 Varian Usaha** x **2 Mode Operasional (Pro & Lite)** dengan peralihan instan tanpa perlu install ulang atau recompile.

---

### ✨ Fitur Utama v2.3.0+171:

1. **Unified 16-in-1 Dynamic State Switcher (1 APK Saja)**:
   - Cukup **1 APK tunggal** (`nusa-sandbox.apk`) untuk mengakses 16 kombinasi aplikasi NUSA Kasir:
     - **8 Varian Usaha**: Kelontong, F&B (Resto/Kafe), Laundry, Bengkel, Salon, Apotek, Fotocopy, Servis Elektronik.
     - **2 Mode Operasional**: Mode Pro (Cloud terhubung) vs Mode Lite (Offline lisensi).
   - Switcher dapat diakses melalui 3 jalur bersih bebas-slop:
     - **Layar Pertama (Onboarding/Login)**: Tap cepat 5x pada logo NUSA (bebas watermark/badge simulasi).
     - **Layar Pengaturan**: Masuk menu `Tentang Aplikasi` -> tap cepat 5x pada `Kebijakan Privasi`.
     - **Headless Switcher via ADB**: `adb shell am start -n com.nusa.dev/com.example.nusa_kasir.MainActivity --es variant <variant> --ez pro <bool> --ez onboarding <bool>`.

2. **Fleksibilitas Jalur Rekaman Konten**:
   - **Terapkan & Mulai dari Awal (Onboarding)**: Mereset akun dan data seed, lalu tetap berada di layar Login/Aktivasi agar kreator dapat mendemokan alur pendaftaran, input lisensi, atau Google Sign-In dari nol.
   - **Terapkan & Langsung Masuk Kasir (POS)**: Bypasses auth otomatis dan langsung masuk ke terminal kasir POS (`/kasir`).

3. **Data Dummy Terkurasi Lengkap di Seluruh 8 Varian**:
   - Produk dengan foto resolusi tinggi dari asset lokal `assets/mock_sandbox/products/{variant}/`.
   - Riwayat penjualan realistis selama **30 hari terakhir** (~38 transaksi per varian dengan Tunai, QRIS ShopeePay, dan Transfer Bank BCA).
   - Sesi kasir aktif hari ini (modal awal Rp 200.000) + 4 riwayat sesi tutup.
   - Data fitur spesifik domain:
     - **F&B**: 10 Meja dine-in, 2 Open Tabs, 8 stok bahan baku resep (BOM), Kitchen Display (KDS).
     - **Bengkel**: 4 Tiket servis motor/mobil dengan plat nomor, teknisi, dan status pengerjaan.
     - **Salon**: 4 Reservasi styling & perawatan dengan jam booking dan stylist.
     - **Apotek**: 3 Resep Dokter formal (Dokter, SIP, Signa/aturan pakai, racikan).
     - **Fotocopy**: 8 Layanan cetak + 4 antrean pesanan cetak dokumen.
     - **Laundry**: 4 Pesanan cucian berjenjang (kiloan, bedcover, sepatu express).
     - **Servis**: 4 Tiket perbaikan gadget elektronik (iPhone, laptop gaming, Samsung).
     - **Kelontong**: 5 Pelanggan member loyalty poin & 2 piutang kasir.

4. **Zero Privacy Leak (Total In-App Mocking)**:
   - Mock In-App Photo Gallery (tidak membuka galeri foto Android fisik).
   - Mock In-App Contacts (tanpa permission `READ_CONTACTS`).
   - Mock Google Account Picker (`Toko Berkah` / `Owner Demo`).
   - Mock Lisensi Key (validasi sukses 300ms tanpa request cloud).
   - Instant Local AI Model Downloader (1.8s progress bar, 0 network).
   - Virtual Bluetooth SPP Printer (58mm scrollable receipt) & ShopeePay Dynamic QRIS Simulator.

---

### 📦 Berkas Unduhan Rilis:
- **`nusa-sandbox.apk`** (172 MB, Package ID: `com.nusa.dev`)
  * Dapat di-install berdampingan dengan 8 aplikasi NUSA versi produksi tanpa bentrok package ID.
