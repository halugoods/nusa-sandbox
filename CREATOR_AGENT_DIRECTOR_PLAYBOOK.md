# Playbook Panduan AI Creator Agent: Orkestrasi Rekam Layar & Mapping Natural (NUSA Kasir)

Dokumen ini adalah acuan baku operasional untuk AI Creator Agent dalam mengeksekusi demo aplikasi, pemetaan screenshot, dan produksi konten visual NUSA Kasir secara presisi, natural, dan bebas dari ketergesa-gesaan (*anti-rushed*).

---

## 1. Prinsip Kerja Natural & Pacing Manusiawi (Zero Rushing)

1. **Jeda Render Flutter Wajib (1.5 – 2.5 Detik)**:
   - DILARANG KERAS mengeksekusi aksi bertubi-tubi dengan jeda instan (misal 0.2s - 0.3s).
   - Di aplikasi Flutter, setiap animasi transisi rute, pemuatan data katalog, dan pergeseran lembar pop-up (*modal sheet*) membutuhkan waktu render 1.5 hingga 2.5 detik agar antarmuka stabil dan utuh.
   - **Aturan Baku**: Buka Layar/Menu $\rightarrow$ Tunggu 1.5–2.0 detik $\rightarrow$ Amati layar $\rightarrow$ Ambil Screenshot $\rightarrow$ Lanjut ke aksi berikutnya.

2. **Protokol Layar Lipat (Samsung Galaxy Z Flip 3 / Foldable)**:
   - Pastikan layar utama HP terbuka aktif (*unfolded*) saat mengambil screenshot.
   - Pada HP foldable dengan layar luar (*SubScreen/Cover Screen*), SurfaceFlinger memiliki multi-display.
   - Selalu targetkan layar utama fisik bagian dalam (**Display ID `4630947232161729154`**):
     ```bash
     adb shell screencap -d 4630947232161729154 -p /sdcard/screen.png
     adb pull /sdcard/screen.png <path_tujuan.png>
     adb shell rm /sdcard/screen.png
     ```

3. **Verifikasi Bebas Duplikat (*Zero-Duplicate Rule*)**:
   - Dilarang menyimpan tangkapan layar jika gambar identik dengan layar sebelumnya.
   - Jika layar belum berubah, tunggu sejenak atau lakukan navigasi ulang. Jangan memotret layar yang sama berulang kali di bawah nama file berbeda.

4. **Kewajiban Menangkap Layar Modal & Sub-Menu Interaktif**:
   - DILARANG hanya memotret daftar menu terluar.
   - Wajib melakukan ketukan (*tap*) untuk membuka lembar pop-up (*modal sheet*) dan sub-halaman:
     - **Header Dashboard**: Ketuk ikon awan untuk memotret *Modal Sinkronisasi Cloud*, ketuk ikon lonceng untuk memotret *Notification Center Drawer*.
     - **Kartu Dashboard**: Potret kondisi default kartu profil staf (*Front Card*), lalu ketuk tombol flip untuk memotret kartu *Ringkasan Hari Ini / Laba Penjualan*.
     - **Pengaturan**: Buka sub-menu *Fitur & Hak Akses* (Tab 1 Kelola Fitur & Tab 2 RBAC), *Data Toko*, *Toko Online*, *Pembayaran QRIS/Bank*, *Pengaturan Struk WYSIWYG*, dan *LAN POS*.
     - **Fitur Khusus Varian**: Buka *KDS Dapur* (`/kitchen-display`), *Resep & HPP* (`/recipes`), *Alur Pesanan Dine-in vs Takeaway*, *Split Bill QRIS*, *Form Tiket Servis Baru*, *Kanvas Pola Kunci HP*, *Resep Obat Apotek*, dll.

---

## 2. Direktori Cheat Code Senyap (Headless Control)

Creator Agent mengeksekusi transisi lisensi, login, dan pergantian varian tanpa memunculkan menu debug di layar rekaman:

| Kebutuhan Alur | Perintah ADB Intent Headless | Efek Aktual di Layar |
| :--- | :--- | :--- |
| **Bypass Login & Lisensi Pro** | `adb shell am start -n com.nusa.kelontong/com.example.nusa_kasir.MainActivity --es action AUTH_PRO` | Langsung masuk kasir mode Pro dengan katalog terisi lengkap. |
| **Bypass Login & Lisensi Lite** | `adb shell am start -n com.nusa.kelontong/com.example.nusa_kasir.MainActivity --es action AUTH_LITE` | Langsung masuk kasir mode Lite (offline murni $0 biaya cloud). |
| **Mulai Tutorial Onboarding Baru** | `adb shell am start -n com.nusa.kelontong/com.example.nusa_kasir.MainActivity --es action ONBOARDING` | Mengosongkan sesi dan membuka layar sambutan awal toko baru. |
| **Ganti Varian Usaha Instan** | `adb shell am start -n com.nusa.kelontong/com.example.nusa_kasir.MainActivity --es variant nusa-{variant} --ez pro true` | Mengubah warna tema, produk, dan fitur varian target (< 1 detik). |

> *Catatan*: Parameter `variant` menerima salah satu dari 8 varian: `kelontong`, `fnb`, `laundry`, `bengkel`, `salon`, `apotek`, `fotocopy`, atau `servis`.

---

## 3. Matriks Resmi Lisensi: Lite vs Pro

Creator Agent WAJIB memahami perbedaan hakiki antara mode Lite dan Pro saat mendemokan fitur:

| Kemampuan / Benefit | NUSA Kasir Lite | NUSA Kasir Pro |
| :--- | :---: | :---: |
| **Harga Lisensi** | **Rp 249.000 Sekali Bayar Seumur Hidup** | **Rp 499.000 Sekali Bayar Seumur Hidup** |
| **Biaya Bulanan / Potongan** | **Rp 0 (Tanpa Biaya Tambahan)** | **Rp 0 (Tanpa Biaya Tambahan)** |
| **Konektivitas Internet** | **100% Offline Murni (0 Kuota Internet)** | **Offline Tetap Jalan + Cloud Sync Otomatis** |
| **Model Akun & Login** | Aktivasi Email + Lisensi Key (Tanpa Google) | Google Sign-In + Profil Cloud |
| **Kasir & Penjualan POS Cepat** | ✅ Lengkap (Barcode, Diskon, Pajak) | ✅ Lengkap (Barcode, Diskon, Pajak) |
| **Cetak Struk Bluetooth (58/80mm)**| ✅ Lengkap (Semua Printer Thermal) | ✅ Lengkap (Semua Printer Thermal) |
| **Katalog Produk & Kelola Stok** | ✅ Lengkap (Kategori, Varian, Pengingat) | ✅ Lengkap (Kategori, Varian, Pengingat) |
| **Catat Pelanggan & Hutang-Piutang** | ✅ Lengkap (Jatuh Tempo & Riwayat) | ✅ Lengkap (Jatuh Tempo & Riwayat) |
| **Laporan Omzet & Laba Bersih** | ✅ Lengkap (Tersimpan Lokal di HP) | ✅ Lengkap (Lokal + Dashboard Cloud) |
| **Asisten NUSA (AI Cerdas)** | ✅ **100% Offline On-Device** (Local LLM di HP) | ✅ **Hybrid** (On-Device + Cloud Intelligence) |
| **Sambungkan ke Komputer (LAN POS)**| ✅ **1 Komputer / PC Kasir** (via WiFi Lokal HP) | ✅ **Multi-PC Kasir Simultan** (WiFi Lokal + Remote) |
| **Sinkronisasi Multi-HP (Kasir & Owner)**| ❌ (1 HP Standalone) | ✅ **Sinkron Realtime <1 Detik** (Beda HP/Lokasi) |
| **Backup & Keamanan Data** | ✅ Backup Lokal Terenkripsi (NUS1) | ✅ **Cloudflare R2 Otomatis** + Backup Lokal |
| **Toko Online / Web Storefront** | ❌ | ✅ **Website Toko Mandiri** (`/toko/[slug]`) |
| **Ekspor Google Sheets** | ❌ (Ekspor CSV / PDF Lokal) | ✅ **Sinkron Langsung ke Google Sheets** |
| **Multi-Cabang & PIN Karyawan** | ❌ (1 Toko Mandiri) | ✅ **Multi-Cabang & Hak Akses PIN Kasir** |
| **Metode Pembayaran QRIS** | ✅ QRIS Statis (Scan & Bayar) | ✅ QRIS Dinamis & QRIS Statis |

---

## 4. Rujukan Slogan & Standar Komunikasi Merek

- **Slogan Resmi Merek**: **"Cara Cerdas Kelola Usaha"**
- **Standar Lisensi**: *"Beli lisensi key sekali untuk seumur hidup tanpa biaya bulanan"*
- **Anti-Slop**: Gunakan bahasa pedagang Indonesia yang membumi, ringkas, dan solutif. Dilarang menggunakan istilah teknis pengembang (SQLite, Drift, Cloudflare, API, Backend) maupun kosakata AI buatan yang aneh (*"orkestrasi paripurna"*, *"rekayasa ekosistem"*).
