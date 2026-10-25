# NUSA Kasir Creator Sandbox (Studio & Automation Edition)

[![Release](https://img.shields.io/badge/Release-v2.3.0%2B171-blue.svg)](https://github.com/halugoods/nusa-sandbox/releases/tag/v2.3.0%2B171)
[![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Flutter%203.x-green.svg)]()
[![Sandbox](https://img.shields.io/badge/Engine-16--in--1%20Dynamic%20Switcher-orange.svg)]()
[![Privacy](https://img.shields.io/badge/Privacy%20Shield-100%25%20In--App%20Mock-red.svg)]()

> **NUSA Kasir Creator Sandbox** adalah build khusus dari ekosistem aplikasi kasir Android **NUSA Kasir** yang dioptimalkan untuk **pembuatan konten video tutorial, demonstrasi publik, dan otomasi screen recording via ADB**.
> 
> Build ini menggabungkan seluruh 8 varian usaha dan 2 mode operasional ke dalam **1 APK tunggal** dengan **Zero Privacy Leak** (tanpa dialog OS Android untuk galeri atau kontak) serta **Deterministic Flow** (bypass spinner/jeda jaringan).

---

## 🚀 4 Pilar Utama Sandbox Edition

1. **16-in-1 Dynamic State Switcher**:
   Cukup 1 APK yang dapat beralih seketika ke **8 Varian Usaha** (`kelontong`, `fnb`, `laundry`, `bengkel`, `salon`, `apotek`, `fotocopy`, `servis`) dan **2 Mode Operasional** (`Pro/Cloud` vs `Lite/Offline`) tanpa recompile atau re-install.
2. **Zero Privacy Leak (Total In-App Mocking)**:
   Aplikasi dilarang keras memicu dialog bawaan OS Android yang dapat mengekspos data pribadi kreator (MediaStore Galeri Foto dan Kontak Telepon). Seluruhnya diganti dengan In-App Mock UI yang terkurasi.
3. **Deterministic Content Flow (Bypass Jeda/Spinner)**:
   Alur Google Sign-In, aktivasi lisensi, unduh Local AI, pairing WhatsApp Gateway, simulasi bayar QRIS, dan pencetakan struk termal dibuat instan dan deterministik (0ms – 1.8s) agar otomasi video presisi.
4. **Rich Out-of-the-Box Dummy Data (30 Hari Transaksi + Domain Spesifik)**:
   Setiap kali varian dipilih, database lokal langsung terisi produk berfoto resolusi tinggi, riwayat transaksi 30 hari terakhir, sesi kasir aktif, serta fitur domain lengkap (meja resto, resep BOM, tiket servis, reservasi salon, resep apotek, dsb).

---

## 🎛️ Cara Mengakses State Switcher (2 Jalur)

### Jalur 1: Dari Layar Awal Login / Onboarding (Disarankan untuk Konten Tutorial)
Di bagian atas layar pertama aplikasi (`ActivationScreen`), terdapat pill badge mengambang:
`[ 🧪 NUSA CREATOR SANDBOX: AKTIF (TAP UNTUK SWITCH) ]`
* **Ketuk badge tersebut** untuk langsung memunculkan bottom sheet **NUSA Creator Studio Control Center**.
* Pilih Varian Usaha & Mode Operasional.
* Tersedia 2 tombol aksi:
  1. **"Terapkan & Mulai dari Awal (Onboarding)"**: Mereset lisensi dan sesi, mengisi database seed, lalu tetap berada di layar Login/Aktivasi agar kreator dapat merekam alur tutorial dari pembuatan akun atau aktivasi lisensi.
  2. **"Terapkan & Langsung Masuk Kasir (POS)"**: Mengaktifkan lisensi Pro Lifetime, login otomatis sebagai Owner, dan langsung navigasi ke terminal kasir POS (`/kasir`).

### Jalur 2: Dari Pengaturan (Secret 5x Tap)
Jika sudah berada di dalam aplikasi:
1. Masuk ke menu **Pengaturan** -> **Tentang Aplikasi**.
2. Cari baris **"Kebijakan Privasi"** (Privacy Policy).
3. **Ketuk 5 kali secara cepat dalam jendela 2 detik**.
4. Haptic feedback getar akan aktif dan modal sheet kontrol akan terbuka seketika.

---

## 📊 Matriks 8 Varian Usaha & Dummy Data Terkurasi

| Varian | Package ID | Warna Primer | Fitur Domain & Seed Data Terkurasi |
| :--- | :--- | :--- | :--- |
| **Kelontong** | `com.nusa.kelontong` | `#F97316` (Oranye) | Sembako, barcode produk, loyalty 5 pelanggan, 2 piutang aktif, 38 transaksi 30 hari. |
| **F&B (Resto/Kafe)** | `com.nusa.fnb` | `#DC2626` (Merah) | 10 Meja dine-in (Meja 01–10), 2 Open Tabs aktif, Kitchen Display (KDS), Resep & Bahan Baku (BOM), 8 stok bahan mentah. |
| **Laundry** | `com.nusa.laundry` | `#EC4899` (Pink) | 4 Pesanan laundry berjenjang (Cuci Kering, Setrika, Bedcover, Cuci Sepatu Express), pelacakan rak simpan. |
| **Bengkel** | `com.nusa.bengkel` | `#2563EB` (Biru) | 4 Tiket servis motor/mobil dengan plat nomor (B 1234 NUSA), teknisi ditugaskan, suku cadang & oli. |
| **Salon** | `com.nusa.salon` | `#8B5CF6` (Ungu) | 4 Reservasi perawatan & styling dengan jam booking, stylist ditugaskan, produk kecantikan. |
| **Apotek** | `com.nusa.apotek` | `#059669` (Hijau Tua) | 3 Resep Dokter formal (Nama Dokter, SIP, Signa/aturan pakai, dosis obat), cetak etiket obat 58mm, copy resep. |
| **Fotocopy** | `com.nusa.fotocopy` | `#0D9488` (Teal) | 8 Layanan cetak (Print A4, Jilid Skripsi, Laminating, Brosur Warna), 4 antrean pesanan cetak aktif. |
| **Servis Elektronik** | `com.nusa.servis` | `#4B5563` (Slate) | 4 Tiket servis gadget (iPhone 13 ganti LCD, ROG Laptop pasta & kipas, Samsung A54, iPad Air). |

---

## 🛡️ Zero Privacy Leak: Fitur Mocking

1. **Mock In-App Photo Gallery**:
   * Saat tombol tambah foto produk ditekan, aplikasi **TIDAK** membuka galeri Android fisik.
   * Muncul In-App Sheet berisi 6–8 foto produk realistis berlatar putih bersih sesuai varian aktif (misal beras, kecap, kopi, sampo) + opsi kamera dummy instan.
2. **Mock In-App Contact Picker**:
   * Tombol "Cari di Kontak HP" tidak meminta permission `READ_CONTACTS`.
   * Menampilkan daftar kontak dummy bernuansa Indonesia: *Budi Santoso*, *Siti Nurhaliza*, *Pak RT Joko*, *Ibu Maya Bakery*, lengkap dengan search bar.
3. **Mock Google Sign-In**:
   * Dialog otentik Google Account Picker: *Toko Berkah (`tokoberkah.nusa@gmail.com`)* atau *Owner Demo*.
   * Bypass Google Play Services dalam 400ms shimmer loading.
4. **Mock Lisensi Lite**:
   * Input key acak apa pun langsung divalidasi sukses (animasi hijau 300ms) tanpa request ke cloud worker.
5. **Instant Local AI Model Downloader**:
   * Tombol "Unduh Model AI" menjalankan simulasi progress bar 0% -> 100% tepat **1.8 detik** tanpa mengunduh file 400MB asli.
   * Asisten chat dilengkapi bank respons cerdas kontekstual UMKM.
6. **Virtual Bluetooth Printer & QRIS Simulator**:
   * Langsung mendeteksi printer virtual `RPP02N-Thermal-58mm`.
   * Cetak struk memunculkan sheet animasi struk virtual resolusi tinggi yang dapat di-scroll.
   * Pembayaran QRIS ShopeePay dilengkapi tombol floating *"Simulasi Pelanggan Bayar"* dengan audio chime kasir instan.

---

## 📦 Download Release APKs

Rilis build resmi untuk versi **`v2.3.0+171`**:

* **[nusa-sandbox.apk (Pro / Cloud)](https://github.com/halugoods/nusa-sandbox/releases/download/v2.3.0%2B171/nusa-sandbox.apk)**:
  * Default mode: Pro (Cloud Aktif).
  * Dilengkapi 16-in-1 switcher instan ke Mode Lite & 8 Varian Usaha.
* **[nusa-sandbox_lite.apk (Lite / Offline)](https://github.com/halugoods/nusa-sandbox/releases/download/v2.3.0%2B171/nusa-sandbox_lite.apk)**:
  * Default mode: Lite (Murni Offline, Lisensi Lokal).
  * Dilengkapi 16-in-1 switcher instan ke Mode Pro & 8 Varian Usaha.

### Cara Install via ADB:
```bash
adb install -r nusa-sandbox.apk
# atau untuk Lite:
adb install -r nusa-sandbox_lite.apk
```

---

## 🤖 Petunjuk untuk AI Agent di Sesi Sebelah

Bagi AI Agent yang bertugas membuat script otomasi video (e.g. Hypit, ADB multi-skill studio, screen recording automation):

1. **Koordinat UI & Gestur**:
   Baca file [`UI_CHANGELOG_STUDIO.md`](UI_CHANGELOG_STUDIO.md) untuk melihat daftar persentase koordinat tap (`%W, %H`), widget keys, dan layout per-varian.
2. **Playbook Skenario Video**:
   Baca file [`PLAYBOOK_SANDBOX.md`](PLAYBOOK_SANDBOX.md) untuk rangkaian urutan perintah ADB tap, input teks, dan transisi layar otomatis.
3. **Sinkronisasi**:
   Setiap kali ada rilis produksi baru di NUSA Kasir, repository ini akan di-update secara paralel dengan release tag yang sama.
