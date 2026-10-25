# UI Delta & Workflow Changelog (v2.3.0+171 - Creator Sandbox Studio Edition)

## Ringkasan Perubahan UI & Visual
Rilis arsitektur **Creator Sandbox & Privacy Shield Engine** (`kCreatorSandbox`) untuk otomatisasi screen recording ADB, pembuatan konten video demonstrasi, dan presentasi publik tanpa risiko kebocoran data pribadi (Zero Privacy Leak) dan bebas ketergantungan perangkat keras fisik maupun koneksi cloud.

### 1. Secret 16-in-1 State Switcher & Onboarding Trigger:
- **Pemicu dari Layar Awal (Login / Aktivasi)**:
  - Terdapat floating pill interaktif di bagian atas layar login/aktivasi: `[ 🛠️ Sandbox: {Nama Varian} • {Pro/Lite} ▾ ]`.
  - Ketukan pada pill langsung membuka modal bottom sheet *"NUSA Creator Studio Control Center"*.
- **Pemicu Rahasia di Layar Pengaturan**:
  - 5x tap cepat dalam 2 detik pada link *"Kebijakan Privasi"* di layar `Pengaturan -> Tentang Aplikasi`.
- **Dua Opsi Penerapan State**:
  1. `Terapkan & Mulai dari Awal (Onboarding)`: Mereset sesi aktivasi lokal, me-reseed database lengkap dengan varian baru, dan tetap berada di layar Login/Aktivasi sehingga kreator dapat membuat tutorial alur pendaftaran dari langkah pertama.
  2. `Terapkan & Langsung Masuk Kasir (POS)`: Mengaktifkan lisensi instan, mendaftarkan sesi Owner, dan langsung me-redirect ke layar transaksi kasir (`/pos`).

### 2. Pre-Populated Rich Dummy Data (100% Siap Rekam per Varian):
- **Katalog Produk ber-Foto**: 57 produk terkurasi di `assets/mock_sandbox/products/{variant}/` yang langsung terhubung ke database Drift SQLite, lengkap dengan kategori, harga beli, harga jual, stok realistis, dan barcode.
- **Riwayat Transaksi 30 Hari Terakhir**: ~40 transaksi penjualan realistis yang tersebar sepanjang sebulan ke belakang dengan variasi metode pembayaran (Tunai, QRIS, Transfer) dan nominal yang pas dengan katalog produk varian.
- **Shift Kasir Aktif (Cashier Session)**: 4 sesi kasir masa lalu yang tertutup rapi dan 1 sesi kasir aktif untuk HARI INI dengan modal awal Rp 200.000, sehingga kasir langsung siap pakai tanpa perlu buka register manual.
- **Fitur Spesial 8 Domain Industri**:
  - **F&B**: 10 meja makan (Meja 01 s/d 10, kapasitas 2-8 kursi, status Kosong, Dipesan, dan Terisi), 2 Open Tabs pesanan aktif di Meja 02 & 05, serta 8 stok bahan baku dapur (Kopi, Susu, Gula Aren, Beras Ramos, Ayam, Telur, Minyak, Paper Cup).
  - **Bengkel**: 4 tiket servis motor (Honda Beat, Yamaha NMAX, Honda Vario, Suzuki Satria) lengkap dengan plat nomor, tahun kendaraan, keluhan, estimasi biaya, suku cadang, dan montir (Mas Agus / Mas Doni).
  - **Salon**: 4 janji temu / booking stylist (Cindy & Lisa) untuk Creambath, Blow Styling, Hair Color, dan Manicure lengkap dengan jam slot dan durasi.
  - **Apotek**: 3 resep dokter formal (dr. Joko Raharjo Sp.A, dr. Ratna Sp.PD, dr. Hendra) dengan nomor SIP resmi, dosis signa detail, dan status resep (Siap, Diproses, Diambil).
  - **Fotocopy**: 8 jenis layanan cetak & jilid + 4 order cetak aktif (Skripsi Jilid Hardcover, Brosur Art Paper, Undangan Warga, Laminating Ijazah).
  - **Laundry**: 4 antrean cucian (Cuci Komplit Kiloan, Bedcover King Size, Cuci Kilat 3 Jam, Cuci Sepatu Sneakers).
  - **Servis**: 4 tiket perbaikan gadget (iPhone 11 ganti LCD, Laptop ASUS ROG overheat thermal paste, Samsung A52 ganti baterai, iPad 9th port charging).
  - **Kelontong**: 5 data pelanggan tetap (Budi, Siti, Pak RT Joko, Ibu Maya, Hendra) dengan poin loyalitas & 2 catatan kasbon piutang aktif.
- **Pengaturan Pembayaran Terisi Otomatis**: QRIS EMVCo dinamis dummy, Bank BCA (8830-1234-5678 a/n TOKO NUSA INDONESIA), dan printer thermal 58mm aktif.

### 3. Total Privacy Shield & Zero-Leak Onboarding:
- **Mock Google Sign-In**: Dialog Material 3 Google Account Picker (*Toko Berkah* & *Owner Demo*) dengan 400ms shimmer -> bypass login tanpa Google Play Services asli.
- **Mock Aktivasi Lisensi Lite**: Validasi instan 300ms untuk key apa pun -> Lifetime Activated tanpa request cloud.
- **Form Setup Toko Bersih**: Layar `/setup` terisi otomatis nama toko sesuai varian, nama owner *"Budi Hartanto"*, dan PIN `123456`, serta mem-bypass total dialog izin Android native (`requestFirstInstallPermissions`).

---

## Peta Navigasi & Koordinat Interaksi
| Layar / Modal | Elemen / Tombol | Aksi / Trigger | Dampak Visual / Hasil |
|---|---|---|---|
| `Layar Login / Aktivasi` | Floating Pill Sandbox | Tap pill atas | Membuka `CreatorStudioControlSheet` sebelum login |
| `Pengaturan` -> `Tentang` | Teks `Kebijakan Privasi` | 5x Tap Cepat (<2.0 detik) | Haptic Feedback Heavy + Pop-up `CreatorStudioControlSheet` |
| `CreatorStudioControlSheet` | Segmented Control Mode | Tap `Mode Pro` / `Mode Lite` | Mengubah runtime state `isPro` dan flag `NusaConfig.isCloudEnabled` |
| `CreatorStudioControlSheet` | List 8 Varian Usaha | Tap kartu varian | Menyorot varian terpilih dengan border tebal & warna brand |
| `CreatorStudioControlSheet` | Tombol `Mulai dari Awal` | Tap tombol primer | Reseed DB lengkap, logout sesi, refresh `ActivationScreen` di varian baru |
| `CreatorStudioControlSheet` | Tombol `Langsung ke Kasir` | Tap tombol sekunder | Reseed DB lengkap, login Owner, langsung navigasi ke `/kasir` |
| `Form Tambah Produk` | Kotak Gambar / Foto | Tap tile kamera | Membuka `MockGallerySheet` (katalog in-app) tanpa memicu MediaStore OS |
| `MockGallerySheet` | Tile `Ambil dari Kamera` | Tap (slot 0) | Mengembalikan sampel foto acak varian 0ms tanpa dialog OS |
| `MockGallerySheet` | Grid Foto Produk | Tap salah satu foto | Menyalin aset resolusi tinggi ke cache & menampilkannya di form |
| `Form Pelanggan / Kasir` | Tombol `Icon Kontak` | Tap tombol kontak | Membuka `MockContactPickerSheet` tanpa minta permission kontak fisik |
| `MockContactPickerSheet` | Search bar / List kontak | Ketik nama / Tap kontak | Mengisi otomatis Nama & Nomor HP (format 08xxx) ke form |
| `Aktivasi Google Login` | Tombol `Masuk dengan Google` | Tap tombol | Membuka modal `MockGoogleAccountPicker` (Toko Berkah / Owner Demo) |
| `Aktivasi Lisensi Lite` | Form License Key | Masukkan key apa saja & Tap | Validasi hijau 300ms -> Status Lifetime Active -> Lanjut `/setup` |
| `Form Setup Toko` | Tombol `Mulai Menggunakan NUSA` | Tap simpan | Simpan data toko & PIN tanpa dialog permission OS Android |
| `Asisten AI (Chatbox)` | Banner `Unduh Model AI` | Tap tombol unduh | Progress bar 0%-100% tepat 1.8s (INT4 -> NPU -> Context 4K) -> Siap |
| `WhatsApp Gateway` | Layar Pairing QR / Code | Tap `⚡ Simulasi HP Terhubung` | QR berganti status badge hijau `Terhubung (Baterai 85%)` + load 3 chat dummy |
| `WhatsApp Outbox` | Input chat & Tombol Kirim | Ketik pesan & Kirim | Muncul status centang satu -> 200ms -> berubah centang dua biru |
| `Pengaturan Printer` | Tombol `Cari Printer` | Tap pindai | Langsung menemukan `RPP02N-Thermal-58mm` & `Zijiang-POS-80mm` |
| `Checkout / Kasir` | Pembayaran QRIS | Kartu QRIS | QR dinamis valid muncul + tombol floating `Simulasi Pelanggan Bayar` |
| `Checkout / Selesai` | Tombol `Cetak Struk` | Tap cetak | Membuka sheet `VirtualReceiptSheet` preview monokrom 58mm interaktif |

---

## Petunjuk untuk AI Video & Otomasi ADB
1. **Punch-in Zoom (1.3x–1.5x)**:
   - Pada layar awal Login/Aktivasi, punch-in ke floating pill Sandbox di header saat mendemonstrasikan fleksibilitas multi-varian.
   - Pada layar Checkout saat metode QRIS aktif, punch-in zoom ke area QR Code dan tombol *"Simulasi Pelanggan Bayar"*.
2. **Timing Transisi & Animasi**:
   - Transisi state switcher varian membutuhkan waktu ~300ms untuk me-reseed database lokal SQLite. Berikan jeda perekaman 400ms setelah tap *"Terapkan"*.
   - Simulasi unduh AI Model berjalan tepat 1.800ms (18 tick x 100ms), sangat pas untuk diisi voiceover tutorial penjelasan akselerasi NPU lokal.
   - Simulasi pesan WhatsApp memiliki jeda 200ms dari centang satu (abu-abu) ke centang dua (biru), sinkronkan dengan efek suara 'pop' pesan terkirim.
3. **Android Device Recording Hygiene**:
   - Selalu pastikan ADB Do Not Disturb aktif (`adb shell cmd notification set_zen_mode 1`).
   - Jangan pernah menyentuh galeri bawaan perangkat; selalu andalkan picker in-app yang telah terpasang.
