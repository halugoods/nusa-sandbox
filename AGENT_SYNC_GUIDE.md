# NUSA Kasir Sandbox: Panduan Koordinasi Antar-Agen AI (Multi-Session Sync)

Dokumen ini adalah SOP dan panduan teknis bagi **AI Agent** yang bekerja di sesi paralel (misalnya agen pembuat video, agen QA/test automation, atau agen dokumentasi) untuk mempelajari dan memanfaatkan NUSA Kasir Creator Sandbox.

---

## 1. Konsep Utama

Repository ini (`halugoods/nusa-sandbox`) bertindak sebagai **Single Source of Truth** untuk artefak rilis APK Sandbox dan metadata UI terkini. 

* **APK Rilis**: Tersedia di GitHub Releases tag `v2.3.0+171` (`nusa-sandbox.apk` — 1 APK tunggal mencakup seluruh 8 varian & 2 mode operasional).
* **Metadata UI**: File [`UI_CHANGELOG_STUDIO.md`](UI_CHANGELOG_STUDIO.md) berisi daftar lengkap layar, widget key, dan persentase koordinat tap.
* **Perintah Otomasi**: File [`PLAYBOOK_SANDBOX.md`](PLAYBOOK_SANDBOX.md) berisi skenario tap ADB presisi.

---

## 2. Cara Agent Mengambil Update Terkini (Pull & Inspect)

Jika Anda adalah agen yang baru saja memulai sesi atau menerima tugas membuat video untuk varian tertentu:

```bash
# 1. Clone atau pull repository ini
git clone https://github.com/halugoods/nusa-sandbox.git
cd nusa-sandbox
git pull origin main

# 2. Periksa versi terbaru dan UI changelog
cat UI_CHANGELOG_STUDIO.md | head -n 40
```

---

## 3. Menghubungkan Device / Emulator untuk Recording

1. Pastikan ADB terhubung:
   ```bash
   adb devices
   ```
2. Unduh dan install APK Sandbox:
   ```bash
   gh release download v2.3.0+171 -p "nusa-sandbox.apk" -R halugoods/nusa-sandbox
   adb install -r nusa-sandbox.apk
   ```
3. Buka atau beralih varian seketika via ADB Intent:
   ```bash
   # Opsi A: Buka standar
   adb shell monkey -p com.nusa.dev -c android.intent.category.LAUNCHER 1

   # Opsi B (Disarankan untuk Agen): Headless Switcher ke varian spesifik
   # Format: --es variant <kelontong|fnb|laundry|bengkel|salon|apotek|fotocopy|servis> --ez pro <true|false> --ez onboarding <true|false>
   adb shell am start -n com.nusa.dev/com.example.nusa_kasir.MainActivity --es variant fnb --ez pro true --ez onboarding false
   ```
   *(Catatan: Sandbox menggunakan isolated package ID `com.nusa.dev` sehingga dapat berdampingan dengan 8 aplikasi NUSA produksi).*

---

## 4. SOP Rekaman Layar Tanpa Kebocoran Privasi (Zero Leak Protocol)

Sesuai aturan di `.agents/memories/` dan `AGENTS.md`:
* **Jangan gunakan `adb exec-out screencap -p > file.png`** di Windows PowerShell (bisa mencemari binary header PNG pada device multi-display).
* **Selalu gunakan protokol internal storage**:
  ```bash
  adb shell "screencap -p /sdcard/screen.png"
  adb pull /sdcard/screen.png ./screen.png
  adb shell "rm /sdcard/screen.png"
  ```
* **Sebelum merekam video**:
  ```bash
  # Aktifkan Do Not Disturb (DND)
  adb shell cmd notification set_zen_mode 1
  ```

---

## 5. Hubungan dengan 8 Repo Produksi NUSA

Repository ini selalu mengikuti nomor versi produksi NUSA Kasir:
* **Versi Major**: `2.3.0`
* **Build Number**: Terkini `+171`
* **Varian Terkait**:
  1. `halugoods/nusa-kelontong`
  2. `halugoods/nusa-fnb`
  3. `halugoods/nusa-laundry`
  4. `halugoods/nusa-bengkel`
  5. `halugoods/nusa-salon`
  6. `halugoods/nusa-apotek`
  7. `halugoods/nusa-fotocopy`
  8. `halugoods/nusa-servis`

Setiap kali ada fitur baru yang di-merge ke 8 varian di atas, APK Sandbox di repo ini akan di-rebuild dan tag baru akan dirilis secara sinkron.
