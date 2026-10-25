# NUSA Creator Sandbox ADB Automation Playbook

Dokumen ini berisi urutan koordinat tap ADB, input teks, dan keycodes untuk mengotomatisasi skenario perekaman video layar HP di **NUSA Kasir Creator Sandbox (`v2.3.0+171`)**.

---

## 📐 Resolusi & Konversi Koordinat

Script mengasumsikan resolusi standar HP 19.5:9 atau 20:9 (misal: `1080 x 2400` atau `1080 x 2340`).
Gunakan persentase lebar (`%W`) dan tinggi (`%H`) untuk menghitung piksel:
`X = Round(W * %W)`, `Y = Round(H * %H)`.

Contoh kalkulator ADB:
```bash
# Untuk layar 1080 x 2400:
# Tap 50% W, 92% H -> X=540, Y=2208
adb shell input tap 540 2208
```

---

## 🎬 Skenario 1: Beralih Varian dari Onboarding / Layar Awal

### Metode A: Headless Switcher Seketika via ADB Intent (Disarankan 0-Klik)
```bash
# Langsung switch varian dan mode tanpa perlu menyentuh menu:
adb shell am start -n com.nusa.dev/com.example.nusa_kasir.MainActivity --es variant fnb --ez pro true --ez onboarding false
```

### Metode B: Melalui Modal Control Center (5x Tap Logo NUSA)
Jika berada di `ActivationScreen`:
1. **Tap Logo NUSA 5x Cepat**:
   * Koordinat: `50% W, 10% H`
   * Perintah: `for i in {1..5}; do adb shell input tap 540 240; sleep 0.1; done`
   * Efek: Haptic feedback getar dan membuka modal sheet **NUSA Creator Studio Control Center**.
2. **Pilih Mode Operasional**:
   * Mode Pro: `30% W, 32% H`
   * Mode Lite: `70% W, 32% H`
3. **Pilih Varian Usaha (Grid 4x2)**:
   * Kelontong: `20% W, 42% H`
   * F&B (Resto/Kafe): `40% W, 42% H`
   * Laundry: `60% W, 42% H`
   * Bengkel: `80% W, 42% H`
   * Salon: `20% W, 52% H`
   * Apotek: `40% W, 52% H`
   * Fotocopy: `60% W, 52% H`
   * Servis: `80% W, 52% H`
4. **Pilih Jalur Aksi Eksekusi**:
   * **Opsi A: Mulai dari Awal (Onboarding)**:
     * Koordinat: `50% W, 88% H`
     * Efek: Reset auth/lisensi, isi data seed, tetap di layar onboarding untuk rekam tutorial awal.
   * **Opsi B: Langsung Masuk Kasir (POS)**:
     * Koordinat: `50% W, 94% H`
     * Efek: Auto-login Owner, langsung masuk terminal kasir POS.

---

## 🎬 Skenario 2: Onboarding Google Sign-In (Jalur Pro)

1. **Tap Tombol "Masuk dengan Google"**:
   * Koordinat: `50% W, 72% H`
   * Efek: Membuka In-App Mock Google Account Picker.
2. **Pilih Akun "Toko Berkah"**:
   * Koordinat: `50% W, 55% H`
   * Efek: Shimmer loading 400ms -> langsung masuk ke form profil toko / dashboard.

---

## 🎬 Skenario 3: Onboarding Lisensi (Jalur Lite)

1. **Tap Field Input Lisensi**:
   * Koordinat: `50% W, 62% H`
2. **Input Dummy Lisensi**:
   * Perintah: `adb shell input text "NUSA-PRO-2026"`
3. **Tap Tombol "Aktivasi Lisensi"**:
   * Koordinat: `50% W, 70% H`
   * Efek: Animasi sukses hijau 300ms -> langsung aktif permanen.

---

## 🎬 Skenario 4: Transaksi Kasir & Mock QRIS Bayar

1. **Pilih Produk 1 (Card Pertama di Grid)**:
   * Koordinat: `25% W, 35% H`
2. **Pilih Produk 2 (Card Kedua di Grid)**:
   * Koordinat: `75% W, 35% H`
3. **Tap Tombol "Bayar" (Floating Bottom Bar)**:
   * Koordinat: `50% W, 93% H`
   * Efek: Membuka Layar Checkout Pembayaran.
4. **Pilih Metode "QRIS"**:
   * Koordinat: `50% W, 38% H`
   * Efek: Muncul QRIS ShopeePay/NUSA valid secara visual + Tombol Floating *"Simulasi Pelanggan Bayar"*.
5. **Tap Tombol "Simulasi Pelanggan Bayar"**:
   * Koordinat: `50% W, 84% H`
   * Efek: Audio ding kasir -> modal notifikasi pembayaran lunas -> navigasi ke layar struk sukses.
6. **Cetak Struk Virtual**:
   * Koordinat: `50% W, 92% H`
   * Efek: Membuka preview struk virtual termal 58mm yang dapat di-scroll.

---

## 🎬 Skenario 5: Secret Gesture Switcher (Jika di dalam POS / Dashboard)

1. **Navigasi ke Pengaturan**:
   * Tap tab Pengaturan: `80% W, 96% H`
2. **Scroll ke Bawah & Tap "Tentang Aplikasi"**:
   * Koordinat: `50% W, 75% H`
3. **Trigger Secret 5x Tap pada "Kebijakan Privasi"**:
   * Koordinat: `50% W, 82% H`
   * Jalankan rentetan 5 tap cepat dalam 1 detik:
     ```bash
     for i in 1 2 3 4 5; do adb shell input tap 540 1968; sleep 0.15; done
     ```
   * Efek: Haptic feedback -> Bottom Sheet **NUSA Creator Studio Control Center** terbuka.
