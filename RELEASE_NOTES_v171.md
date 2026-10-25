# NUSA Kasir Creator Sandbox v2.3.0+171 — Studio & Automation Edition

Build resmi NUSA Kasir Creator Sandbox khusus untuk pembuatan konten video tutorial, demonstrasi publik, dan otomasi ADB screen recording.

### ✨ Apa yang Baru di v2.3.0+171:
1. **Onboarding Variant Switcher Pill**:
   - Badge mengambang `[ 🧪 NUSA CREATOR SANDBOX: AKTIF (TAP UNTUK SWITCH) ]` di layar pertama Login / Aktivasi (`ActivationScreen`).
   - Memungkinkan kreator berpindah ke 8 varian usaha dan memilih:
     - **Terapkan & Mulai dari Awal (Onboarding)**: Reset lisensi dan data, tetap di layar awal untuk merekam alur pendaftaran toko, input lisensi, atau Google Sign-In.
     - **Terapkan & Langsung Masuk Kasir (POS)**: Bypasses auth, langsung menuju terminal kasir POS.
2. **Comprehensive Curated Dummy Data di Seluruh 8 Varian**:
   - Produk berfoto resolusi tinggi dari asset bundle `assets/mock_sandbox/products/{variant}/`.
   - Riwayat penjualan realistis selama **30 hari terakhir** (~38 transaksi per varian dengan Tunai, QRIS ShopeePay, dan Transfer Bank BCA).
   - Sesi kasir aktif hari ini (modal awal Rp 200.000) + 4 riwayat sesi kasir tutup.
   - Data fitur spesifik domain:
     - **F&B**: 10 Meja dine-in, 2 Open Tabs, 8 stok bahan baku resep (BOM), Kitchen Display (KDS).
     - **Bengkel**: 4 Tiket servis motor/mobil dengan plat nomor, teknisi, dan status pengerjaan.
     - **Salon**: 4 Reservasi styling & perawatan dengan jam booking dan stylist.
     - **Apotek**: 3 Resep Dokter formal (Dokter, SIP, Signa/aturan pakai, racikan).
     - **Fotocopy**: 8 Layanan cetak + 4 antrean pesanan cetak dokumen.
     - **Laundry**: 4 Pesanan cucian berjenjang (kiloan, bedcover, sepatu express).
     - **Servis**: 4 Tiket perbaikan gadget elektronik (iPhone, laptop gaming, Samsung).
     - **Kelontong**: 5 Pelanggan member loyalty poin & 2 piutang kasir.
3. **Zero Privacy Leak (Total In-App Mocking)**:
   - Mock In-App Photo Gallery (tanpa MediaStore OS fisik).
   - Mock In-App Contacts (tanpa permission `READ_CONTACTS`).
   - Mock Google Account Picker (`Toko Berkah` / `Owner Demo`).
   - Mock Lisensi Key (validasi sukses 300ms).
   - Instant Local AI Model Downloader (1.8s progress bar, zero network download).
   - Virtual Bluetooth SPP Printer (58mm scrollable receipt) & ShopeePay Dynamic QRIS Simulator.

### 📦 Aset Rilis yang Tersedia:
- `nusa-sandbox.apk` (Pro / Cloud Mode default, isolated package `com.nusa.dev`)
- `nusa-sandbox_lite.apk` (Lite / Offline Mode default, isolated package `com.nusa.dev`)
