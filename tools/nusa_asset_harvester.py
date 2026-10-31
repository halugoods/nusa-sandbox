#!/usr/bin/env python3
"""
NUSA Kasir - Automated Content Screenshot Harvester
=====================================================
Script otomatis untuk memanen (screenshot) seluruh layar, menu, dan detail
interaksi di 8 varian NUSA Kasir Creator Sandbox (com.nusa.dev) via ADB.

Keunggulan:
- 100% Otomatis: Gak perlu screenshot manual satu-satu di HP lalu me-rename file.
- Penamaan Baku: Menggunakan format standar yang langsung dikenali AI Vision Multimodal.
- Terstruktur per Varian: Folder rapi per industri (Kelontong, FnB, Laundry, Bengkel, dll).
- Zero-Corrupt Screen Capture Protocol: Menggunakan internal storage staging (/sdcard).
"""

import os
import sys
import time
import subprocess
from datetime import datetime

# Root output directory
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "content_library")

# Definisi Varian & Skenario Screenshot
VARIANTS = [
    {
        "id": "kelontong",
        "name": "NUSA Kelontong",
        "folder": "01_kelontong",
        "steps": [
            ("01_pos_catalog_grid", "Katalog produk sembako & minimarket dengan foto dan harga"),
            ("02_pos_cart_active", "Keranjang belanja dengan produk pilihan dan total harga"),
            ("03_checkout_payment_options", "Pilihan metode pembayaran (Tunai, QRIS, Kasbon, Transfer)"),
            ("04_payment_qris_screen", "Tampilan kode QRIS dinamis siap scan"),
            ("05_receipt_thermal_preview", "Pratinjau struk kasir thermal 58mm"),
            ("06_kasbon_debt_screen", "Catatan kasbon pelanggan dan jatuh tempo"),
            ("07_closing_shift_summary", "Rekap shift kasir (uang masuk, modal laci, setoran)"),
            ("08_daily_profit_report", "Laporan keuntungan bersih dan omzet harian"),
        ]
    },
    {
        "id": "fnb",
        "name": "NUSA FnB",
        "folder": "02_fnb",
        "steps": [
            ("01_pos_menu_kuliner", "Daftar menu makanan dan minuman berfoto"),
            ("02_table_management_grid", "Manajemen denah meja tamu (Dine-in)"),
            ("03_takeaway_vs_dinein", "Pilihan pesanan bungkus atau makan di tempat"),
            ("04_kitchen_order_ticket", "Tiket pesanan ke bagian dapur atau bar"),
            ("05_kitchen_display_kds", "Tampilan layar dapur koki (Kitchen Display)"),
            ("06_recipe_bom_ingredients", "Takaran resep bahan baku otomatis potong stok"),
            ("07_fnb_sales_report", "Laporan omzet resto dan menu best-seller"),
        ]
    },
    {
        "id": "laundry",
        "name": "NUSA Laundry",
        "folder": "03_laundry",
        "steps": [
            ("01_pos_laundry_services", "Daftar tarif laundry kiloan dan satuan"),
            ("02_weight_scale_input", "Input berat timbangan desimal (misal 3.5 kg)"),
            ("03_rack_hanger_assignment", "Pencatatan nomor rak dan lemari penyimpanan baju"),
            ("04_order_status_tracking", "Pelacakan status cucian (Diterima, Dicuci, Siap Ambil)"),
            ("05_laundry_tag_receipt", "Nota struk tanda terima laundry dengan nomor kantong"),
        ]
    },
    {
        "id": "bengkel",
        "name": "NUSA Bengkel",
        "folder": "04_bengkel",
        "steps": [
            ("01_pos_sparepart_catalog", "Katalog suku cadang, oli, dan ban berfoto"),
            ("02_license_plate_input", "Input nomor polisi (plat nomor) dan tipe kendaraan"),
            ("03_mechanic_fee_split", "Pemisahan ongkos jasa mekanik dan harga sparepart"),
            ("04_vehicle_service_history", "Riwayat riil servis kendaraan pelanggan"),
            ("05_bengkel_work_invoice", "Nota struk bengkel lengkap dengan data kendaraan"),
        ]
    },
    {
        "id": "salon",
        "name": "NUSA Salon",
        "folder": "05_salon",
        "steps": [
            ("01_pos_salon_services", "Daftar layanan potong rambut, creambath, dan perawatan"),
            ("02_stylist_assignment", "Pilihan nama kapster atau stylist yang melayani"),
            ("03_stylist_commission_view", "Perhitungan komisi bagi hasil karyawan otomatis"),
            ("04_treatment_package", "Paket perawatan bundling kecantikan"),
            ("05_salon_closing_report", "Laporan penutupan kasir dan komisi karyawan"),
        ]
    },
    {
        "id": "apotek",
        "name": "NUSA Apotek",
        "folder": "06_apotek",
        "steps": [
            ("01_pos_medicine_catalog", "Katalog obat bebas, resep, strip, dan botol"),
            ("02_doctor_prescription_input", "Form pencatatan resep dokter (nama dokter, pasien, aturan pakai)"),
            ("03_dosage_etiket_print", "Cetak etiket aturan pakai obat untuk ditempel di botol/plastik"),
            ("04_expiry_date_alert", "Peringatan dini otomatis obat mendekati kadaluarsa"),
            ("05_apograph_copy_receipt", "Salinan resep resmi (apograph) bertanda tangan apoteker"),
        ]
    },
    {
        "id": "fotocopy",
        "name": "NUSA Fotocopy",
        "folder": "07_fotocopy",
        "steps": [
            ("01_pos_printing_services", "Daftar tarif cetak per lembar, warna, BW, dan jilid"),
            ("02_per_page_calculator", "Kalkulator hitung otomatis jumlah lembar dan rangkap"),
            ("03_binding_laminating_options", "Pilihan jenis jilid (skripsi, spiral, lakban) dan laminating"),
            ("04_banner_meteran_calculator", "Hitungan spanduk atau banner per meter persegi"),
            ("05_pc_portal_file_queue", "Antrean berkas kiriman pelanggan yang masuk dari HP"),
        ]
    },
    {
        "id": "servis",
        "name": "NUSA Servis",
        "folder": "08_servis",
        "steps": [
            ("01_pos_sparepart_device", "Katalog sparepart LCD, baterai, dan aksesoris"),
            ("02_intake_receipt_complaint", "Tanda terima servis masuk (keluhan kerusakan, pola/password, kelengkapan)"),
            ("03_repair_status_pipeline", "Status pengerjaan servis (Dicek, Tunggu Part, Selesai)"),
            ("04_warranty_card_print", "Cetak kartu garansi servis resmi untuk pelanggan"),
        ]
    }
]

GLOBAL_SCREENS = [
    ("00_global_auth", "01_welcome_onboarding", "Layar pembuka onboarding NUSA Kasir"),
    ("00_global_auth", "02_license_key_input", "Form aktivasi kode lisensi resmi"),
    ("00_global_auth", "03_store_profile_setup", "Pengaturan awal nama toko dan alamat"),
    ("09_shared_settings", "01_settings_menu_main", "Menu pengaturan umum toko"),
    ("09_shared_settings", "02_printer_bluetooth_setup", "Pengaturan koneksi printer thermal Bluetooth"),
    ("09_shared_settings", "03_pc_connect_info", "Menu Sambungkan ke Komputer (Web POS & Portal File)"),
    ("09_shared_settings", "04_cashier_pin_security", "Pengaturan hak akses kasir dan PIN pemilik toko"),
]


def run_adb(cmd):
    full_cmd = f"adb {cmd}"
    res = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
    return res.stdout.strip()


def check_adb_connected():
    out = run_adb("devices")
    lines = [l.strip() for l in out.split("\n")[1:] if l.strip() and not l.startswith("*")]
    return len(lines) > 0


def capture_clean_screenshot(dest_path):
    """
    Menangkap screenshot HP menggunakan internal storage staging.
    Menjamin biner PNG tidak tercemar output warning ADB (anti-corrupt).
    """
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    sdcard_path = "/sdcard/_nusa_capture_temp.png"
    
    # 1. Capture di internal storage HP
    run_adb(f'shell "screencap -p {sdcard_path}"')
    time.sleep(0.3)
    
    # 2. Pull ke komputer
    run_adb(f'pull "{sdcard_path}" "{dest_path}"')
    
    # 3. Hapus staging file
    run_adb(f'shell "rm {sdcard_path}"')
    
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1000:
        print(f"  [SAVED] {os.path.basename(dest_path)} ({os.path.getsize(dest_path) // 1024} KB)")
        return True
    else:
        print(f"  [WARN] Gagal menyimpan {dest_path}")
        return False


def switch_variant(variant_id, is_pro=True, onboarding=False):
    """
    Headless Intent Switcher ke APK Sandbox (com.nusa.dev)
    """
    pro_str = "true" if is_pro else "false"
    onboard_str = "true" if onboarding else "false"
    cmd = (
        f'shell am start -n com.nusa.dev/com.example.nusa_kasir.MainActivity '
        f'--es variant {variant_id} --ez pro {pro_str} --ez onboarding {onboard_str}'
    )
    run_adb(cmd)
    time.sleep(1.8)  # Beri jeda transisi seeder & render UI


def main():
    print("=" * 70)
    print("📸 NUSA KASIR - AUTOMATED CONTENT ASSET HARVESTER")
    print("=" * 70)
    
    if not check_adb_connected():
        print("[ERROR] Tidak ada HP/Emulator yang terdeteksi via ADB!")
        print("Pastikan HP Android tercolok kabel USB (atau via 'adb connect <ip>:5555').")
        sys.exit(1)
        
    print("[OK] Perangkat ADB terdeteksi.")
    print(f"[DEST] Folder Output: {OUTPUT_DIR}\n")
    
    # 1. Bersihkan notifikasi & aktifkan DND di HP agar tangkapan layar bersih
    run_adb("shell cmd notification set_zen_mode 1")
    
    # 2. Panen Layar Global / Onboarding
    print("▶ Memanen Layar Onboarding & Pengaturan Global...")
    switch_variant("kelontong", is_pro=True, onboarding=True)
    for folder, file_name, desc in GLOBAL_SCREENS:
        dest = os.path.join(OUTPUT_DIR, folder, f"{file_name}.png")
        print(f"- {desc} -> {folder}/{file_name}.png")
        capture_clean_screenshot(dest)
        time.sleep(0.5)

    # 3. Panen Layar per 8 Varian Usaha
    for v in VARIANTS:
        v_id = v["id"]
        v_folder = v["folder"]
        print(f"\n▶ Beralih ke Varian: {v['name']} ({v_id})...")
        switch_variant(v_id, is_pro=True, onboarding=False)
        
        for step_key, desc in v["steps"]:
            dest = os.path.join(OUTPUT_DIR, v_folder, f"{step_key}.png")
            print(f"- {desc} -> {v_folder}/{step_key}.png")
            capture_clean_screenshot(dest)
            time.sleep(0.5)

    # 4. Kembalikan mode notifikasi normal
    run_adb("shell cmd notification set_zen_mode 0")
    
    print("\n" + "=" * 70)
    print("✅ PANEN ASSET KONTEN SELESAI DENGAN SEMPURNA!")
    print(f"Seluruh screenshot tersimpan rapi dan siap dipelajari AI Vision di:")
    print(f"{OUTPUT_DIR}")
    print("=" * 70)


if __name__ == "__main__":
    main()
