# NUSA Kasir Creator Sandbox & Studio Hub (v2.3.1+172)

[![Release](https://img.shields.io/badge/Release-v2.3.1%2B172-blue.svg)](https://github.com/halugoods/nusa-sandbox/releases/tag/v2.3.1%2B172)
[![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Flutter%203.x-green.svg)]()
[![Engine](https://img.shields.io/badge/Engine-1%20APK%20for%2016%20States-orange.svg)]()
[![Brand](https://img.shields.io/badge/Slogan-Cara%20Cerdas%20Kelola%20Usaha-emerald.svg)]()

> **NUSA Kasir Creator Sandbox** adalah repositori pusat panduan, aset, dan lingkungan aplikasi kasir Android **NUSA Kasir** yang dirancang khusus untuk **AI Creator Agent, demonstrasi publik, dan otomasi pembuatan konten video / grafis berkualitas studio**.
> 
> **1 APK Saja Untuk Seluruh Kebutuhan**: Cukup gunakan 1 file APK (`nusa-sandbox.apk`) untuk mencakup seluruh **8 Varian Usaha** dan **2 Mode Operasional (Pro & Lite)** dengan tampilan **100% Like-Production** (bebas watermark simulasi), **Zero Privacy Leak** (tanpa dialog OS Android untuk galeri atau kontak fisik), serta **Deterministic Flow**.

---

## 🧭 Peta Navigasi & Panduan Utama (Central Agent Guides)

Setiap AI Creator Agent yang bertugas diwajibkan membaca dan memahami dokumen panduan di repositori ini sebelum mengeksekusi tugas:

1. 📖 **[`CREATOR_AGENT_DIRECTOR_PLAYBOOK.md`](CREATOR_AGENT_DIRECTOR_PLAYBOOK.md)**:
   - Prinsip kerja natural manusiawi (*Natural Pacing*, anti-rushed, jeda render 1.5–2.5s).
   - Protokol layar lipat Samsung Galaxy Z Flip 3 (`display-id 4630947232161729154`).
   - Panduan Silent Cheat Codes ADB.
2. 📸 **[`ASSET_LIBRARY_PLAYBOOK.md`](ASSET_LIBRARY_PLAYBOOK.md)**:
   - Cetak biru pustaka tangkapan layar 9 direktori di `assets/content_library/` (00_global_auth sampai 08_servis).
   - Checklist layar-layar fungsional nyata yang wajib dipetakan untuk automasi CLI.
3. ✍️ **[`ANTISLOP_COPYWRITING_GUIDELINES.md`](ANTISLOP_COPYWRITING_GUIDELINES.md)**:
   - Standar copywriting pedagang UMKM Indonesia.
   - Larangan istilah teknis pemrogram (SQLite, Cloudflare, API, Backend).
   - Kamus padanan bahasa pedagang yang hidup, membumi, dan solutif.

---

## 🧠 Pustaka Skill Marketing & Kreatif Terpasang (`skills/`)

Repositori ini memuat skill pemasaran dan copywriting berstandar industri yang dapat langsung dipelajari dan diaktifkan oleh AI Agent:

- **[`skills/copywriting/`](skills/copywriting/)**: Framework penulisan headline, hook 3 detik awal, formulasi penawaran, dan panggilan aksi (CTA).
- **[`skills/ad-creative/`](skills/ad-creative/)**: Konsep kreatif materi iklan, struktur carousel slide, komposisi visual, dan penataan sudut pandang (*angle*).
- **[`skills/marketing-psychology/`](skills/marketing-psychology/)**: Prinsip psikologi konversi (*loss aversion*, bukti sosial, kenyamanan operasional pedagang).
- **[`skills/nusa-creator-cognitive/`](skills/nusa-creator-cognitive/)**: Kecerdasan kognitif kreatif NUSA Kasir, riset tren visual real-time via `@agent-reach`, dan filter anti-slop.
- **[`skills/content-strategy/`](skills/content-strategy/)** & **[`skills/social/`](skills/social/)**: Strategi pilar konten, ritme posting, dan distribusi media sosial.
- **[`skills/nusa-pc-connect-studio/`](skills/nusa-pc-connect-studio/)**: Panduan demonstrasi dan pembuatan konten fitur *"Sambungkan ke Komputer"* (LAN POS PC).

---

## 🎛️ Silent Cheat Codes (Headless ADB Control)

Gunakan perintah intent senyap ini untuk mengarahkan aplikasi di balik layar tanpa memunculkan menu debug pada rekaman video:

```bash
# Package Resmi: com.nusa.kelontong

# 1. Langsung masuk kasir Mode Pro (dengan katalog dummy lengkap)
adb shell am start -n com.nusa.kelontong/com.example.nusa_kasir.MainActivity --es action AUTH_PRO

# 2. Langsung masuk kasir Mode Lite (100% offline, 0 biaya cloud)
adb shell am start -n com.nusa.kelontong/com.example.nusa_kasir.MainActivity --es action AUTH_LITE

# 3. Buka layar Onboarding / Selamat Datang toko baru
adb shell am start -n com.nusa.kelontong/com.example.nusa_kasir.MainActivity --es action ONBOARDING

# 4. Ganti Varian Usaha seketika (< 1 detik)
# Pilihan varian: kelontong, fnb, laundry, bengkel, salon, apotek, fotocopy, servis
adb shell am start -n com.nusa.kelontong/com.example.nusa_kasir.MainActivity --es variant nusa-{variant} --ez pro true
```

---

## 🏷️ Matriks Lisensi Resmi: Lite vs Pro

| Fitur / Kemampuan | NUSA Kasir Lite | NUSA Kasir Pro |
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

## 📦 Unduhan APK Sandbox Tunggal

Rilis build resmi untuk versi **`v2.3.1+172`**:
* **[nusa-sandbox.apk (Single Unified 16-in-1 APK)](https://github.com/halugoods/nusa-sandbox/releases/download/v2.3.1%2B172/nusa-sandbox.apk)** (209.8 MB)
  * Mencakup **seluruh 8 Varian Usaha** x **2 Mode (Pro & Lite)**.
  * Dilengkapi **57 foto produk katalog baru beresolusi tinggi (Flow MCP)**.
  * Mendukung **Asisten NUSA AI Offline** pada mode Lite & Pro.
