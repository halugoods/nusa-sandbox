#!/usr/bin/env python3
"""
NUSA Kasir - Comprehensive Content Screenshot Harvester (136 Granular Targets)
================================================================================
Script otomatis untuk memanen seluruh layar utama, formulir melayang (floating sheet),
dialog pop-up, kalkulator, dan interaksi mikro di 8 varian NUSA Kasir Creator Sandbox (com.nusa.dev).

Keunggulan:
- 136 Target Aset Visual Terkurasi (Bukan cuma menu utama, tapi sampai detail floating sheet & modal).
- Folderisasi Rapi: 12 direktori terpisah (Auth, 8 Varian, Shared POS Flow, Shared Settings, Shared Operations).
- Penamaan Baku Standar Industri: Langsung siap dikonsumsi AI Vision Multimodal untuk pemetaan konten.
- Zero-Corrupt Screen Capture Protocol: Menggunakan internal storage staging (/sdcard).
"""

import os
import sys
import time
import subprocess
from datetime import datetime

# Root output directory
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "content_library")

# Master Blueprint: 126 Granular Assets
HARVEST_PLAN = [
    {
        "folder": "00_global_auth",
        "variant": "kelontong",
        "onboarding": True,
        "items": [
            ("auth_01_welcome_onboarding", "Layar pembuka selamat datang & pilihan masuk", None),
            ("auth_02_google_sign_in_sheet", "Modal sheet pilihan akun Google Sign-In", [("tap", 540, 1720), ("wait", 0.6), ("back",)]),
            ("auth_03_license_key_input", "Form input aktivasi lisensi key lifetime", [("tap", 540, 1850), ("wait", 0.5)]),
            ("auth_04_activation_success_anim", "Modal dialog sukses aktivasi permanen", [("type", "NUSA-PRO-2026"), ("tap", 540, 1680), ("wait", 0.8), ("back",)]),
            ("auth_05_store_profile_setup", "Form input identitas toko dan alamat", None),
            ("auth_06_variant_picker_sheet", "Sheet pilihan 8 varian industri usaha", [("tap_logo_5x",), ("wait", 0.6), ("back",)]),
        ]
    },
    {
        "folder": "09_shared_pos_flow",
        "variant": "kelontong",
        "onboarding": False,
        "items": [
            ("pos_01_catalog_empty_cart", "Katalog grid produk saat keranjang masih kosong", [("route", "/kasir")]),
            ("pos_02_category_filter_chips", "Filter kategori produk sedang aktif", [("tap", 200, 280), ("wait", 0.4)]),
            ("pos_03_cart_bar_bottom_active", "Floating bar keranjang bawah terisi belanjaan", [("tap", 270, 840), ("tap", 810, 840), ("wait", 0.4)]),
            ("pos_04_item_detail_modifier_sheet", "Modal sheet ubah quantity & catatan item", [("tap", 540, 2230), ("wait", 0.6), ("back",)]),
            ("pos_05_global_discount_sheet", "Modal input diskon belanja / kode promo", [("tap", 900, 280), ("wait", 0.5), ("back",)]),
            ("pos_06_customer_picker_sheet", "Sheet pemilihan nama pelanggan langganan", [("tap", 120, 280), ("wait", 0.5), ("back",)]),
            ("pos_07_payment_methods_sheet", "Layar checkout pilihan metode pembayaran", [("tap", 540, 2230), ("wait", 0.6)]),
            ("pos_08_cash_fast_tender_keypad", "Pilihan bayar tunai dengan tombol uang pas", [("tap", 540, 680), ("wait", 0.4)]),
            ("pos_09_qris_dynamic_display", "Tampilan kode QRIS dinamis siap scan", [("tap", 540, 880), ("wait", 0.5)]),
            ("pos_10_receipt_thermal_preview", "Pratinjau struk kasir thermal 58mm", [("tap", 540, 2020), ("wait", 0.8), ("back",), ("back",)]),
        ]
    },
    {
        "folder": "01_kelontong",
        "variant": "kelontong",
        "onboarding": False,
        "items": [
            ("01_pos_grid_kelontong", "Katalog produk sembako, minyak, beras, rokok", [("route", "/kasir")]),
            ("02_grosir_tier_pricing_sheet", "Modal setting harga bertingkat eceran vs grosir", [("route", "/produk"), ("tap", 540, 800), ("wait", 0.6), ("back",)]),
            ("03_barcode_scanner_active", "Layar scanner barcode aktif kamera belakang", [("route", "/kasir"), ("tap", 980, 160), ("wait", 0.8), ("back",)]),
            ("04_product_add_floating_sheet", "Floating sheet formulir tambah produk baru", [("route", "/produk"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("05_product_edit_stock_sheet", "Modal penyesuaian stok opname gudang", [("route", "/stok"), ("tap", 540, 700), ("wait", 0.5), ("back",)]),
            ("06_shelf_label_print_preview", "Pratinjau cetak label harga rak minimarket", [("route", "/produk"), ("tap", 850, 160), ("wait", 0.6), ("back",)]),
            ("07_kasbon_debt_customer_sheet", "Pencatatan kasbon langganan dan jatuh tempo", [("route", "/piutang"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("08_debt_installments_history", "Riwayat pembayaran cicilan kasbon pelanggan", [("route", "/piutang"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("09_closing_shift_summary", "Rekap tutup shift kasir & uang laci", [("route", "/laporan"), ("tap", 540, 1200), ("wait", 0.6), ("back",)]),
            ("10_daily_profit_loss_report", "Laporan laba bersih & omzet harian toko", [("route", "/laporan"), ("wait", 0.5)]),
            ("11_best_seller_product_ranking", "Peringkat produk sembako paling laris", [("route", "/laporan"), ("swipe_up",), ("wait", 0.5)]),
            ("12_bulk_excel_import_sheet", "Modal upload ribuan produk via file Excel", [("route", "/produk"), ("tap", 750, 160), ("wait", 0.5), ("back",)]),
            ("13_stock_low_alert_banner", "Peringatan stok menipis belanja ulang", [("route", "/stok"), ("wait", 0.4)]),
            ("14_receipt_with_store_logo", "Struk kasir dengan foto logo toko sembako", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
        ]
    },
    {
        "folder": "02_fnb",
        "variant": "fnb",
        "onboarding": False,
        "items": [
            ("01_pos_grid_fnb_menu", "Katalog menu makanan, minuman, dan kopi", [("route", "/kasir")]),
            ("02_table_management_grid", "Denah visual meja makan (Dine-in)", [("route", "/meja"), ("wait", 0.5)]),
            ("03_table_occupancy_detail_sheet", "Detail pesanan aktif di meja tamu", [("tap", 300, 600), ("wait", 0.5), ("back",)]),
            ("04_move_merge_table_dialog", "Modal pindah atau gabung meja pelanggan", [("tap", 300, 600), ("tap", 850, 400), ("wait", 0.5), ("back",), ("back",)]),
            ("05_dine_in_vs_takeaway_toggle", "Pilihan makan di tempat vs bawa pulang", [("route", "/kasir"), ("wait", 0.4)]),
            ("06_product_modifier_topping_sheet", "Modal pilihan topping, level pedas, es", [("tap", 270, 840), ("wait", 0.5), ("back",)]),
            ("07_kitchen_order_ticket_print", "Pratinjau tiket pesanan koki dapur/bar", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("08_kitchen_display_system_kds", "Layar Dapur Digital (KDS) monitor koki", [("route", "/kitchen-display"), ("wait", 0.6)]),
            ("09_recipe_bom_management", "Daftar Resep & Takaran Bahan Baku (BOM)", [("route", "/recipes"), ("wait", 0.5)]),
            ("10_recipe_ingredient_add_sheet", "Modal input takaran gram kopi & ml susu", [("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("11_split_bill_payment_modal", "Modal pisah tagihan bayar per orang", [("route", "/checkout"), ("tap", 540, 1400), ("wait", 0.5), ("back",)]),
            ("12_fnb_daily_closing_report", "Laporan omzet resto makanan vs minuman", [("route", "/laporan"), ("wait", 0.5)]),
        ]
    },
    {
        "folder": "03_laundry",
        "variant": "laundry",
        "onboarding": False,
        "items": [
            ("01_pos_services_laundry", "Katalog layanan cuci komplit, kering, setrika", [("route", "/kasir")]),
            ("02_kiloan_vs_satuan_selector", "Pilihan hitung tarif per kilo vs per helai", [("wait", 0.4)]),
            ("03_weight_decimal_keypad_sheet", "Keypad input timbangan desimal (3.75 kg)", [("tap", 270, 840), ("wait", 0.5), ("back",)]),
            ("04_rack_hanger_assignment_dialog", "Modal penetapan nomor rak & lemari baju", [("tap", 540, 2230), ("tap", 540, 1100), ("wait", 0.5), ("back",), ("back",)]),
            ("05_perfume_fragrance_selector", "Pilihan aroma parfum laundry pelanggan", [("tap", 270, 840), ("wait", 0.5), ("back",)]),
            ("06_order_status_pipeline_sheet", "Status cucian (Diterima, Cuci, Setrika, Siap)", [("route", "/laundry_status"), ("wait", 0.5)]),
            ("07_laundry_tag_receipt_preview", "Struk tanda terima cucian dengan nomor kantong", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("08_whatsapp_ready_pickup_modal", "Modal kirim WA otomatis cucian siap diambil", [("route", "/laundry_status"), ("tap", 850, 600), ("wait", 0.5), ("back",)]),
            ("09_laundry_production_queue", "Antrean kerja cucian berdasarkan jam selesai", [("route", "/laundry_status"), ("wait", 0.5)]),
            ("10_laundry_revenue_report", "Rekapitulasi omzet kiloan vs satuan bulan ini", [("route", "/laporan"), ("wait", 0.5)]),
        ]
    },
    {
        "folder": "04_bengkel",
        "variant": "bengkel",
        "onboarding": False,
        "items": [
            ("01_pos_sparepart_oil_grid", "Katalog oli mesin, kampas rem, busi, ban", [("route", "/kasir")]),
            ("02_vehicle_intake_form_sheet", "Form input plat nomor polisi & kilometer KM", [("tap", 120, 280), ("wait", 0.5), ("back",)]),
            ("03_mechanic_assignment_sheet", "Pilihan montir yang mengerjakan servis", [("tap", 270, 840), ("wait", 0.5), ("back",)]),
            ("04_service_fee_sparepart_split", "Pemisahan ongkos jasa vs harga suku cadang", [("route", "/checkout"), ("wait", 0.5), ("back",)]),
            ("05_vehicle_service_history_sheet", "Riwayat servis kendaraan berdasarkan plat nomor", [("route", "/pelanggan"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("06_work_order_spk_preview", "Surat Perintah Kerja (SPK) untuk mekanik", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("07_bengkel_official_invoice", "Nota struk resmi bengkel lengkap garansi", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("08_mechanic_commission_summary", "Rekap upah bagi hasil komisi mekanik", [("route", "/laporan"), ("tap", 540, 1400), ("wait", 0.5), ("back",)]),
            ("09_sparepart_restock_alert", "Peringatan stok oli & kampas rem menipis", [("route", "/stok"), ("wait", 0.4)]),
            ("10_bengkel_monthly_sales_report", "Laporan laba bengkel: jasa vs margin part", [("route", "/laporan"), ("wait", 0.5)]),
        ]
    },
    {
        "folder": "05_salon",
        "variant": "salon",
        "onboarding": False,
        "items": [
            ("01_pos_salon_services_grid", "Daftar menu haircut, creambath, pewarnaan", [("route", "/kasir")]),
            ("02_stylist_kapster_select_sheet", "Pilihan kapster / stylist yang melayani", [("tap", 270, 840), ("wait", 0.5), ("back",)]),
            ("03_treatment_package_bundling_sheet", "Paket perawatan kecantikan bundling hemat", [("wait", 0.4)]),
            ("04_stylist_commission_calculator", "Perhitungan persentase komisi bagi hasil", [("route", "/laporan/stylist"), ("wait", 0.5)]),
            ("05_customer_hair_notes_sheet", "Catatan model rambut langganan pelanggan", [("route", "/pelanggan"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("06_salon_receipt_with_stylist_name", "Nota struk kasir dengan nama hair stylist", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("07_stylist_daily_payout_report", "Rekap komisi harian seluruh terapis/stylist", [("route", "/laporan/stylist"), ("wait", 0.5)]),
            ("08_appointment_queue_list", "Daftar reservasi dan antrean walk-in salon", [("route", "/booking"), ("wait", 0.5)]),
            ("09_product_retail_upsell_sheet", "Penjualan vitamin rambut & pomade retail", [("route", "/kasir"), ("tap", 600, 280), ("wait", 0.4)]),
            ("10_salon_performance_analytics", "Analisis layanan rambut paling diminati", [("route", "/laporan"), ("wait", 0.5)]),
        ]
    },
    {
        "folder": "06_apotek",
        "variant": "apotek",
        "onboarding": False,
        "items": [
            ("01_pos_medicine_catalog_grid", "Katalog obat bebas, resep, strip, botol", [("route", "/kasir")]),
            ("02_prescription_doctor_intake_sheet", "Form resep dokter: SIP, pasien, usia, BB", [("route", "/resep"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("03_signa_dosage_rule_picker", "Pilihan aturan pakai cepat (signa 3x1)", [("route", "/resep"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("04_medicine_etiket_print_preview", "Pratinjau cetak etiket obat stiker 58mm", [("route", "/resep"), ("tap", 540, 600), ("tap", 850, 400), ("wait", 0.6), ("back",), ("back",)]),
            ("05_batch_number_expiry_sheet", "Pencatatan nomor batch pabrik & tgl expired", [("route", "/produk"), ("tap", 540, 700), ("wait", 0.5), ("back",)]),
            ("06_expiry_date_alert_warning_list", "Daftar peringatan obat mendekati kadaluarsa", [("route", "/stok"), ("wait", 0.5)]),
            ("07_official_apograph_copy_receipt", "Salinan resep resmi bertanda tangan apoteker", [("route", "/resep"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("08_unit_conversion_calculator_sheet", "Konversi satuan obat: 1 box = 10 strip", [("route", "/produk"), ("tap", 540, 700), ("wait", 0.5), ("back",)]),
            ("09_controlled_medicine_report", "Laporan buku pengeluaran obat resep", [("route", "/laporan"), ("wait", 0.5)]),
            ("10_apotek_daily_margin_report", "Laporan laba obat bebas vs obat resep", [("route", "/laporan"), ("wait", 0.5)]),
            ("11_supplier_pbf_purchase_order", "Surat pesanan obat ke distributor PBF", [("route", "/pembelian"), ("wait", 0.5)]),
            ("12_customer_drug_allergy_record", "Catatan riwayat alergi obat pelanggan", [("route", "/pelanggan"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
        ]
    },
    {
        "folder": "07_fotocopy",
        "variant": "fotocopy",
        "onboarding": False,
        "items": [
            ("01_pos_print_copy_services_grid", "Tarif fotocopy, print warna, jilid, ATK", [("route", "/kasir")]),
            ("02_per_page_pricing_calculator", "Kalkulator hitung otomatis jumlah lembar", [("tap", 270, 840), ("wait", 0.5), ("back",)]),
            ("03_color_mode_paper_selector", "Pilihan mode warna: Hitam Putih vs Warna", [("wait", 0.4)]),
            ("04_binding_laminating_options_sheet", "Pilihan jilid lakban, spiral, hardcover", [("tap", 810, 840), ("wait", 0.5), ("back",)]),
            ("05_banner_meteran_calculator_dialog", "Hitung spanduk/banner per meter persegi", [("tap", 270, 1100), ("wait", 0.5), ("back",)]),
            ("06_pc_portal_file_queue_screen", "Antrean file kiriman pelanggan dari HP", [("route", "/print-portal"), ("wait", 0.6)]),
            ("07_pc_portal_download_detail_modal", "Modal detail berkas & spesifikasi cetak", [("tap", 540, 700), ("wait", 0.5), ("back",)]),
            ("08_fotocopy_job_ticket_receipt", "Struk tanda terima cetak dengan jam selesai", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("09_atk_retail_item_catalog", "Katalog penjualan kertas rim & alat tulis", [("route", "/kasir"), ("tap", 400, 280), ("wait", 0.4)]),
            ("10_pc_portal_web_browser_view", "Tampilan desktop monitor operator PC", [("route", "/print-portal"), ("wait", 0.5)]),
            ("11_production_paper_waste_log", "Catatan kertas rusak / gagal cetak", [("route", "/stok"), ("wait", 0.4)]),
            ("12_fotocopy_daily_sales_recap", "Laporan omzet jasa mesin vs jualan kertas", [("route", "/laporan"), ("wait", 0.5)]),
        ]
    },
    {
        "folder": "08_servis",
        "variant": "servis",
        "onboarding": False,
        "items": [
            ("01_pos_sparepart_device_grid", "Katalog LCD, baterai original, konektor", [("route", "/kasir")]),
            ("02_unit_intake_receipt_complaint_sheet", "Form tanda terima unit servis & keluhan", [("route", "/servis"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("03_screen_pattern_pin_draw_sheet", "Lembar gambar pola kunci layar & PIN HP", [("route", "/servis"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("04_cost_estimate_down_payment_dialog", "Pencatatan estimasi biaya & uang muka DP", [("route", "/servis"), ("tap", 540, 600), ("tap", 850, 300), ("wait", 0.5), ("back",), ("back",)]),
            ("05_intake_claim_receipt_preview", "Cetak nota tanda terima servis resmi", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("06_repair_status_pipeline_sheet", "Status servis: Masuk, Dicek, Tunggu Part", [("route", "/servis"), ("wait", 0.5)]),
            ("07_whatsapp_service_done_notify_modal", "Modal WA otomatis: HP selesai diperbaiki", [("route", "/servis"), ("tap", 850, 600), ("wait", 0.5), ("back",)]),
            ("08_service_warranty_card_print", "Cetak kartu garansi servis resmi (30 hari)", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("09_technician_commission_payout", "Rekapitulasi komisi teknisi per unit HP", [("route", "/laporan"), ("tap", 540, 1400), ("wait", 0.5), ("back",)]),
            ("10_servis_monthly_revenue_report", "Laporan laba usaha servis: jasa vs sparepart", [("route", "/laporan"), ("wait", 0.5)]),
        ]
    },
    {
        "folder": "10_shared_settings",
        "variant": "kelontong",
        "onboarding": False,
        "items": [
            ("set_01_settings_menu_main", "Menu utama pengaturan NUSA Kasir", [("route", "/pengaturan")]),
            ("set_02_store_data_edit_form", "Form pengaturan nama toko, WA, upload logo", [("tap", 540, 400), ("wait", 0.5), ("back",)]),
            ("set_03_receipt_footer_tax_sheet", "Setting footer struk toko & PPN", [("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("set_04_printer_bluetooth_scanner_sheet", "Sheet pencarian printer Bluetooth thermal", [("tap", 540, 800), ("wait", 0.6), ("back",)]),
            ("set_05_printer_paper_width_selector", "Pilihan lebar kertas 58mm vs 80mm", [("tap", 540, 800), ("wait", 0.5), ("back",)]),
            ("set_06_lan_pc_connect_screen", "Layar Sambungkan ke Komputer (Web POS)", [("route", "/lan-pos"), ("wait", 0.5)]),
            ("set_07_lan_pairing_pin_modal", "Modal tampilan PIN pairing 4-digit komputer", [("tap", 540, 1200), ("wait", 0.5), ("back",)]),
            ("set_08_employee_list_roles", "Daftar staf karyawan kasir & jabatan", [("route", "/karyawan"), ("wait", 0.5)]),
            ("set_09_employee_add_pin_access_sheet", "Modal tambah kasir, PIN, kunci laba", [("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("set_10_backup_restore_sheet", "Modal simpan berkas cadangan data .nus1", [("route", "/pengaturan"), ("tap", 540, 1400), ("wait", 0.5), ("back",)]),
            ("set_11_creator_studio_control_sheet", "Modal Creator Studio Control 5x tap logo", [("tap_logo_5x",), ("wait", 0.6), ("back",)]),
            ("set_12_about_license_version_info", "Info versi aplikasi & lisensi lifetime", [("route", "/pengaturan"), ("swipe_up",), ("wait", 0.4)]),
        ]
    },
    {
        "folder": "11_shared_operations",
        "variant": "kelontong",
        "onboarding": False,
        "items": [
            ("op_01_shift_cash_drawer_open", "Modal buka kasir & input uang modal awal laci", [("route", "/kasir"), ("tap", 120, 160), ("wait", 0.6), ("back",)]),
            ("op_02_finance_cashflow_overview", "Buku kas & ringkasan arus kas masuk vs keluar", [("route", "/keuangan"), ("wait", 0.5)]),
            ("op_03_finance_expense_record_sheet", "Modal formulir catat pengeluaran toko baru", [("route", "/keuangan"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("op_04_stock_opname_audit_screen", "Layar audit stok opname fisik barang gudang", [("route", "/stok"), ("tap", 850, 160), ("wait", 0.5)]),
            ("op_05_stock_adjustment_confirm_dialog", "Dialog konfirmasi selisih stok fisik vs sistem", [("tap", 540, 700), ("wait", 0.5), ("back",), ("back",)]),
            ("op_06_transactions_history_list", "Daftar riwayat transaksi & filter tanggal", [("route", "/transaksi"), ("wait", 0.5)]),
            ("op_07_transaction_detail_receipt_view", "Detail nota transaksi & tombol cetak ulang struk", [("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("op_08_transaction_refund_return_dialog", "Modal proses retur barang / refund nota", [("tap", 540, 600), ("tap", 850, 400), ("wait", 0.5), ("back",), ("back",)]),
            ("op_09_suppliers_vendor_list", "Daftar kontak pemasok & distributor kulakan", [("route", "/supplier"), ("wait", 0.5)]),
            ("op_10_supplier_add_vendor_sheet", "Modal formulir tambah pemasok / vendor baru", [("route", "/supplier"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("op_11_purchase_order_restock_screen", "Form purchase order / faktur kulakan masuk", [("route", "/pembelian"), ("wait", 0.5)]),
            ("op_12_attendance_clockin_screen", "Layar absensi kehadiran staf & jam kerja", [("route", "/presensi"), ("wait", 0.5)]),
            ("op_13_promo_design_studio_editor", "Studio pembuat flyer & poster diskon promosi", [("route", "/desain_promosi"), ("wait", 0.6)]),
            ("op_14_id_card_member_studio", "Studio cetak ID card staf & kartu member QR", [("route", "/id_card_studio"), ("wait", 0.6)]),
            ("op_15_online_orders_dashboard", "Dashboard kelola pesanan toko online masuk", [("route", "/pesanan_online"), ("wait", 0.5)]),
            ("op_16_online_storefront_preview", "Pratinjau etalase belanja online pembeli", [("route", "/toko"), ("wait", 0.5)]),
            ("op_17_ai_business_consultant_chat", "Layar konsultasi pintar Asisten AI Toko NUSA", [("route", "/ai_chat"), ("wait", 0.5)]),
            ("op_18_multibranch_outlet_manager", "Pengelolaan multi-cabang outlet & pantau stok", [("route", "/cabang"), ("wait", 0.5)]),
        ]
    }
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
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    sdcard_path = "/sdcard/_nusa_capture_temp.png"
    
    run_adb(f'shell "screencap -p {sdcard_path}"')
    time.sleep(0.25)
    run_adb(f'pull "{sdcard_path}" "{dest_path}"')
    run_adb(f'shell "rm {sdcard_path}"')
    
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1000:
        print(f"    [OK] {os.path.basename(dest_path)} ({os.path.getsize(dest_path) // 1024} KB)")
        return True
    else:
        print(f"    [WARN] Gagal menyimpan {dest_path}")
        return False


def switch_variant(variant_id, is_pro=True, onboarding=False):
    pro_str = "true" if is_pro else "false"
    onboard_str = "true" if onboarding else "false"
    cmd = (
        f'shell am start -n com.nusa.dev/com.example.nusa_kasir.MainActivity '
        f'--es variant {variant_id} --ez pro {pro_str} --ez onboarding {onboard_str}'
    )
    run_adb(cmd)
    time.sleep(1.8)


def execute_action(action):
    act_type = action[0]
    if act_type == "tap":
        run_adb(f"shell input tap {action[1]} {action[2]}")
    elif act_type == "type":
        run_adb(f'shell input text "{action[1]}"')
    elif act_type == "wait":
        time.sleep(action[1])
    elif act_type == "back":
        run_adb("shell input keyevent 4")
        time.sleep(0.3)
    elif act_type == "swipe_up":
        run_adb("shell input swipe 540 1800 540 600 300")
        time.sleep(0.4)
    elif act_type == "tap_logo_5x":
        for _ in range(5):
            run_adb("shell input tap 540 240")
            time.sleep(0.08)
    elif act_type == "route":
        # Deep link route jika didukung atau fallback ke navigasi
        route_path = action[1]
        run_adb(f'shell am start -n com.nusa.dev/com.example.nusa_kasir.MainActivity -d "nusa://app{route_path}"')
        time.sleep(0.8)


def main():
    print("=" * 80)
    print("📸 NUSA KASIR - MASTER ASSET HARVESTER (108 GRANULAR INTERACTION TARGETS)")
    print("=" * 80)
    
    if not check_adb_connected():
        print("[ERROR] Tidak ada HP/Emulator yang terdeteksi via ADB!")
        print("Pastikan HP Android terhubung via USB atau WiFi ('adb connect <ip>:5555').")
        sys.exit(1)
        
    print("[OK] Perangkat ADB terdeteksi aktif.")
    print(f"[DEST] Folder Output: {OUTPUT_DIR}\n")
    
    # 1. Aktifkan Do Not Disturb (DND)
    run_adb("shell cmd notification set_zen_mode 1")
    
    total_captured = 0
    start_time = time.time()
    
    # 2. Iterasi seluruh 11 grup direktori
    for group in HARVEST_PLAN:
        folder = group["folder"]
        variant = group["variant"]
        onboarding = group.get("onboarding", False)
        items = group["items"]
        
        print(f"\n📂 [{folder.upper()}] Menginisialisasi varian '{variant}' (Onboarding: {onboarding})...")
        switch_variant(variant, is_pro=True, onboarding=onboarding)
        
        for file_name, desc, actions in items:
            dest = os.path.join(OUTPUT_DIR, folder, f"{file_name}.png")
            print(f"  • {desc} -> {file_name}.png")
            
            # Jalankan aksi interaksi jika ada
            if actions:
                for act in actions:
                    execute_action(act)
                    time.sleep(0.2)
                    
            # Tangkap screenshot
            if capture_clean_screenshot(dest):
                total_captured += 1
                
            time.sleep(0.3)
            
    # 3. Kembalikan notifikasi HP
    run_adb("shell cmd notification set_zen_mode 0")
    
    elapsed = int(time.time() - start_time)
    print("\n" + "=" * 80)
    print(f"🎉 SUKSES! Berhasil memanen {total_captured} Aset Layar & Interaksi Mikro dalam {elapsed} detik.")
    print(f"📁 Seluruh file tersimpan rapi dan siap dipelajari AI Vision di:")
    print(f"   {OUTPUT_DIR}")
    print("=" * 80)


if __name__ == "__main__":
    main()
