#!/usr/bin/env python3
"""
NUSA Kasir - Comprehensive Per-Variant Asset Harvester (198 Granular Targets)
=============================================================================
Script otomatis untuk memanen seluruh layar utama, formulir melayang (floating sheet),
dialog pop-up, kalkulator, dan interaksi mikro di 8 varian NUSA Kasir Creator Sandbox (com.nusa.dev).

Keunggulan Arsitektur:
- 100% Mandiri Per-Varian: Tiap varian memiliki pustaka visual utuh (24 aset per varian).
- Zero Theme Mismatch: Setiap tangkapan layar menggunakan tema warna asli industri, data produk riil, dan nota struk masing-masing.
- 9 Folder Terpisah: 00_global_auth + 8 direktori varian (01_kelontong s/d 08_servis).
- Zero-Corrupt Screen Capture Protocol: Menggunakan internal storage staging (/sdcard).
"""

import os
import sys
import time
import subprocess
from datetime import datetime

# Root output directory
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "content_library")

# Master Blueprint: 198 Granular Assets across 9 Directories
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
        "folder": "01_kelontong",
        "variant": "kelontong",
        "onboarding": False,
        "items": [
            ("01_pos_catalog_grid", "Katalog produk sembako, minyak, beras, rokok", [("route", "/kasir")]),
            ("02_category_filter_chips", "Filter kategori sembako sedang aktif", [("tap", 200, 280), ("wait", 0.4)]),
            ("03_barcode_scanner_active", "Layar scanner barcode aktif kamera belakang", [("tap", 980, 160), ("wait", 0.8), ("back",)]),
            ("04_cart_bottom_active", "Floating bar keranjang bawah terisi belanjaan", [("tap", 270, 840), ("tap", 810, 840), ("wait", 0.4)]),
            ("05_item_quantity_notes_sheet", "Modal sheet ubah quantity & catatan item", [("tap", 540, 2230), ("wait", 0.6), ("back",)]),
            ("06_grosir_tier_pricing_sheet", "Modal setting harga bertingkat grosir vs eceran", [("route", "/produk"), ("tap", 540, 800), ("wait", 0.6), ("back",)]),
            ("07_shelf_label_price_tag", "Pratinjau cetak label harga rak minimarket", [("route", "/produk"), ("tap", 850, 160), ("wait", 0.6), ("back",)]),
            ("08_kasbon_customer_sheet", "Pencatatan kasbon langganan dan jatuh tempo", [("route", "/piutang"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("09_debt_installments_history", "Riwayat pembayaran cicilan kasbon pelanggan", [("route", "/piutang"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("10_product_add_form_sheet", "Floating sheet formulir tambah sembako baru", [("route", "/produk"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("11_payment_methods_sheet", "Layar checkout pilihan cara bayar", [("route", "/kasir"), ("tap", 540, 2230), ("wait", 0.6)]),
            ("12_cash_fast_tender_keypad", "Pilihan bayar tunai dengan tombol uang pas", [("tap", 540, 680), ("wait", 0.4)]),
            ("13_qris_dynamic_display", "Tampilan kode QRIS dinamis siap scan", [("tap", 540, 880), ("wait", 0.5)]),
            ("14_receipt_thermal_preview", "Pratinjau struk thermal 58mm logo toko kelontong", [("tap", 540, 2020), ("wait", 0.8), ("back",), ("back",)]),
            ("15_closing_shift_summary", "Rekap tutup shift kasir & uang laci toko sembako", [("route", "/laporan"), ("tap", 540, 1200), ("wait", 0.6), ("back",)]),
            ("16_finance_cashflow_overview", "Buku kas toko sembako masuk vs keluar", [("route", "/keuangan"), ("wait", 0.5)]),
            ("17_finance_expense_sheet", "Modal formulir catat pengeluaran toko baru", [("route", "/keuangan"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("18_stock_inventory_list", "Daftar stok fisik sembako & alert menipis", [("route", "/stok"), ("wait", 0.5)]),
            ("19_stock_opname_audit_sheet", "Form audit stok opname gudang sembako", [("route", "/stok"), ("tap", 850, 160), ("wait", 0.5), ("back",)]),
            ("20_transactions_history_list", "Riwayat transaksi penjualan toko sembako", [("route", "/transaksi"), ("wait", 0.5)]),
            ("21_transaction_refund_dialog", "Modal proses retur barang rusak / refund nota", [("route", "/transaksi"), ("tap", 540, 600), ("tap", 850, 400), ("wait", 0.5), ("back",), ("back",)]),
            ("22_suppliers_restock_sheet", "Kontak agen distributor sembako & faktur PO", [("route", "/supplier"), ("wait", 0.5)]),
            ("23_settings_printer_setup", "Pengaturan printer Bluetooth thermal 58mm/80mm", [("route", "/pengaturan"), ("tap", 540, 800), ("wait", 0.6), ("back",)]),
            ("24_settings_lan_pc_connect", "Layar Sambungkan ke Komputer (Web POS kelontong)", [("route", "/lan-pos"), ("wait", 0.5)]),
        ]
    },
    {
        "folder": "02_fnb",
        "variant": "fnb",
        "onboarding": False,
        "items": [
            ("01_pos_fnb_menu_grid", "Katalog menu makanan, minuman, dan camilan kafe", [("route", "/kasir")]),
            ("02_table_management_grid", "Denah visual meja tamu (Dine-in)", [("route", "/meja"), ("wait", 0.5)]),
            ("03_table_occupancy_detail_sheet", "Detail pesanan aktif di meja tamu kafe", [("tap", 300, 600), ("wait", 0.5), ("back",)]),
            ("04_move_merge_table_dialog", "Modal aksi pindah atau gabung meja tamu", [("tap", 300, 600), ("tap", 850, 400), ("wait", 0.5), ("back",), ("back",)]),
            ("05_dine_in_vs_takeaway_toggle", "Pilihan makan di tempat vs bungkus", [("route", "/kasir"), ("wait", 0.4)]),
            ("06_product_modifier_topping_sheet", "Modal pilihan topping, level pedas, es", [("tap", 270, 840), ("wait", 0.5), ("back",)]),
            ("07_cart_fnb_order_active", "Bar pesanan meja kafe terisi makanan & minuman", [("tap", 270, 840), ("tap", 810, 840), ("wait", 0.4)]),
            ("08_kitchen_order_ticket_print", "Pratinjau tiket pesanan koki dapur/bar", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("09_kitchen_display_system_kds", "Layar Dapur Digital (KDS) monitor koki", [("route", "/kitchen-display"), ("wait", 0.6)]),
            ("10_recipe_bom_management", "Daftar Resep & Takaran Bahan Baku (BOM)", [("route", "/recipes"), ("wait", 0.5)]),
            ("11_recipe_ingredient_add_sheet", "Modal input takaran gram kopi & ml susu", [("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("12_split_bill_payment_modal", "Modal pisah tagihan bayar per orang", [("route", "/kasir"), ("tap", 540, 2230), ("tap", 540, 1400), ("wait", 0.5), ("back",)]),
            ("13_payment_methods_sheet", "Layar checkout kasir kafe/resto", [("route", "/kasir"), ("tap", 540, 2230), ("wait", 0.6)]),
            ("14_cash_fast_tender_keypad", "Pembayaran tunai kasir kafe & kembalian", [("tap", 540, 680), ("wait", 0.4)]),
            ("15_qris_dynamic_display", "Tampilan QRIS dinamis di meja kasir kafe", [("tap", 540, 880), ("wait", 0.5)]),
            ("16_receipt_thermal_preview", "Struk kasir kafe rincian nomor meja & servis", [("tap", 540, 2020), ("wait", 0.8), ("back",), ("back",)]),
            ("17_fnb_daily_closing_report", "Laporan omzet resto makanan vs minuman", [("route", "/laporan"), ("wait", 0.5)]),
            ("18_finance_cashflow_overview", "Buku kas harian resto masuk vs keluar", [("route", "/keuangan"), ("wait", 0.5)]),
            ("19_finance_expense_sheet", "Catat belanja bahan basah dapur & es batu", [("route", "/keuangan"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("20_stock_raw_materials_list", "Stok bahan baku mentah (biji kopi, cup, sirup)", [("route", "/stok"), ("wait", 0.5)]),
            ("21_transactions_history_list", "Riwayat transaksi meja kafe & arsip pesanan", [("route", "/transaksi"), ("wait", 0.5)]),
            ("22_attendance_staff_shift", "Presensi absensi staf barista, waiter, koki", [("route", "/presensi"), ("wait", 0.5)]),
            ("23_settings_printer_kitchen", "Pengaturan multi-printer kasir & dapur", [("route", "/pengaturan"), ("tap", 540, 800), ("wait", 0.6), ("back",)]),
            ("24_settings_lan_pc_connect", "Layar Sambungkan ke Komputer (Web POS & KDS PC)", [("route", "/lan-pos"), ("wait", 0.5)]),
        ]
    },
    {
        "folder": "03_laundry",
        "variant": "laundry",
        "onboarding": False,
        "items": [
            ("01_pos_services_laundry_grid", "Katalog layanan cuci komplit, kering, setrika", [("route", "/kasir")]),
            ("02_kiloan_vs_satuan_selector", "Pilihan hitung tarif per kilo vs per helai", [("wait", 0.4)]),
            ("03_weight_decimal_keypad_sheet", "Keypad input timbangan desimal (3.75 kg)", [("tap", 270, 840), ("wait", 0.5), ("back",)]),
            ("04_perfume_fragrance_selector", "Pilihan aroma parfum laundry pelanggan", [("tap", 270, 840), ("wait", 0.5), ("back",)]),
            ("05_rack_hanger_assignment_dialog", "Modal penetapan nomor rak & lemari baju A-04", [("tap", 540, 2230), ("tap", 540, 1100), ("wait", 0.5), ("back",), ("back",)]),
            ("06_cart_laundry_order_active", "Bar keranjang cucian pelanggan terisi kiloan", [("tap", 270, 840), ("tap", 810, 840), ("wait", 0.4)]),
            ("07_order_status_pipeline_sheet", "Status cucian (Diterima, Cuci, Setrika, Siap)", [("route", "/laundry_status"), ("wait", 0.5)]),
            ("08_laundry_tag_receipt_preview", "Struk tanda terima cucian dengan nomor kantong", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("09_whatsapp_ready_pickup_modal", "Modal kirim WA otomatis cucian siap diambil", [("route", "/laundry_status"), ("tap", 850, 600), ("wait", 0.5), ("back",)]),
            ("10_laundry_production_queue", "Antrean kerja cucian berdasarkan jam selesai", [("route", "/laundry_status"), ("wait", 0.5)]),
            ("11_payment_methods_sheet", "Layar checkout laundry (bisa DP di awal)", [("route", "/kasir"), ("tap", 540, 2230), ("wait", 0.6)]),
            ("12_cash_fast_tender_keypad", "Pembayaran tunai uang muka cucian & kembalian", [("tap", 540, 680), ("wait", 0.4)]),
            ("13_qris_dynamic_display", "QRIS dinamis di meja kasir laundry", [("tap", 540, 880), ("wait", 0.5)]),
            ("14_receipt_thermal_preview", "Struk thermal tanda terima cucian nomor kantong", [("tap", 540, 2020), ("wait", 0.8), ("back",), ("back",)]),
            ("15_laundry_revenue_report", "Rekapitulasi omzet kiloan vs satuan bulan ini", [("route", "/laporan"), ("wait", 0.5)]),
            ("16_finance_cashflow_overview", "Buku kas operasional laundry masuk vs keluar", [("route", "/keuangan"), ("wait", 0.5)]),
            ("17_finance_expense_sheet", "Catat belanja deterjen, softener, gas dryer", [("route", "/keuangan"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("18_stock_detergent_chemical", "Stok bahan kimia deterjen, softener, parfum", [("route", "/stok"), ("wait", 0.5)]),
            ("19_stock_opname_audit_sheet", "Audit stok bahan kimia & plastik packing", [("route", "/stok"), ("tap", 850, 160), ("wait", 0.5), ("back",)]),
            ("20_transactions_history_list", "Riwayat transaksi cucian pelanggan", [("route", "/transaksi"), ("wait", 0.5)]),
            ("21_customer_loyalty_sheet", "Kartu member cuci 10x gratis 1x cuci", [("route", "/pelanggan"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("22_attendance_staff_shift", "Presensi staf pencuci & operator setrika uap", [("route", "/presensi"), ("wait", 0.5)]),
            ("23_settings_printer_setup", "Pengaturan printer thermal nota laundry 58mm", [("route", "/pengaturan"), ("tap", 540, 800), ("wait", 0.6), ("back",)]),
            ("24_settings_lan_pc_connect", "Layar Sambungkan ke Komputer (Web POS laundry)", [("route", "/lan-pos"), ("wait", 0.5)]),
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
            ("06_cart_bengkel_order_active", "Bar keranjang servis dan suku cadang aktif", [("tap", 270, 840), ("tap", 810, 840), ("wait", 0.4)]),
            ("07_work_order_spk_preview", "Surat Perintah Kerja (SPK) untuk mekanik", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("08_bengkel_official_invoice", "Nota struk resmi bengkel lengkap garansi", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("09_mechanic_commission_summary", "Rekap upah bagi hasil komisi mekanik", [("route", "/laporan"), ("tap", 540, 1400), ("wait", 0.5), ("back",)]),
            ("10_sparepart_restock_alert", "Peringatan stok oli & kampas rem menipis", [("route", "/stok"), ("wait", 0.4)]),
            ("11_payment_methods_sheet", "Layar checkout kasir bengkel", [("route", "/kasir"), ("tap", 540, 2230), ("wait", 0.6)]),
            ("12_cash_fast_tender_keypad", "Pembayaran tunai ongkos servis & suku cadang", [("tap", 540, 680), ("wait", 0.4)]),
            ("13_qris_dynamic_display", "QRIS dinamis di meja kasir bengkel", [("tap", 540, 880), ("wait", 0.5)]),
            ("14_receipt_thermal_preview", "Struk thermal bengkel resmi plat nomor & montir", [("tap", 540, 2020), ("wait", 0.8), ("back",), ("back",)]),
            ("15_bengkel_monthly_sales_report", "Laporan laba bengkel: jasa vs margin part", [("route", "/laporan"), ("wait", 0.5)]),
            ("16_finance_cashflow_overview", "Buku kas operasional bengkel masuk vs keluar", [("route", "/keuangan"), ("wait", 0.5)]),
            ("17_finance_expense_sheet", "Catat belanja solar pembersih, majun, kompresor", [("route", "/keuangan"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("18_stock_sparepart_inventory", "Daftar stok suku cadang & oli mesin", [("route", "/stok"), ("wait", 0.5)]),
            ("19_stock_opname_audit_sheet", "Form audit stok opname sparepart di rak", [("route", "/stok"), ("tap", 850, 160), ("wait", 0.5), ("back",)]),
            ("20_transactions_history_list", "Riwayat servis kendaraan dan nota bengkel", [("route", "/transaksi"), ("wait", 0.5)]),
            ("21_suppliers_part_vendor_sheet", "Daftar agen sparepart motor & distributor oli", [("route", "/supplier"), ("wait", 0.5)]),
            ("22_attendance_mechanic_shift", "Presensi absensi mekanik dan montir", [("route", "/presensi"), ("wait", 0.5)]),
            ("23_settings_printer_setup", "Pengaturan printer thermal nota SPK bengkel", [("route", "/pengaturan"), ("tap", 540, 800), ("wait", 0.6), ("back",)]),
            ("24_settings_lan_pc_connect", "Layar Sambungkan ke Komputer (Web POS bengkel)", [("route", "/lan-pos"), ("wait", 0.5)]),
        ]
    },
    {
        "folder": "05_salon",
        "variant": "salon",
        "onboarding": False,
        "items": [
            ("01_pos_salon_services_grid", "Daftar menu potong rambut, pewarnaan, creambath", [("route", "/kasir")]),
            ("02_stylist_kapster_select_sheet", "Pilihan kapster / stylist yang melayani", [("tap", 270, 840), ("wait", 0.5), ("back",)]),
            ("03_treatment_package_bundling_sheet", "Paket bundling hemat perawatan rambut", [("wait", 0.4)]),
            ("04_stylist_commission_calculator", "Perhitungan persentase komisi bagi hasil", [("route", "/laporan/stylist"), ("wait", 0.5)]),
            ("05_customer_hair_notes_sheet", "Catatan model rambut langganan pelanggan", [("route", "/pelanggan"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("06_cart_salon_order_active", "Bar pesanan salon terisi jasa & produk retail", [("tap", 270, 840), ("tap", 810, 840), ("wait", 0.4)]),
            ("07_appointment_queue_list", "Daftar reservasi dan antrean walk-in salon", [("route", "/booking"), ("wait", 0.5)]),
            ("08_product_retail_upsell_sheet", "Penjualan vitamin rambut & pomade retail", [("route", "/kasir"), ("tap", 600, 280), ("wait", 0.4)]),
            ("09_salon_receipt_stylist_name", "Nota struk kasir salon mencantumkan nama stylist", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("10_stylist_daily_payout_report", "Rekap komisi harian seluruh terapis/stylist", [("route", "/laporan/stylist"), ("wait", 0.5)]),
            ("11_payment_methods_sheet", "Layar checkout kasir salon", [("route", "/kasir"), ("tap", 540, 2230), ("wait", 0.6)]),
            ("12_cash_fast_tender_keypad", "Bayar tunai kasir salon & input tips kapster", [("tap", 540, 680), ("wait", 0.4)]),
            ("13_qris_dynamic_display", "Tampilan QRIS dinamis meja resepsionis salon", [("tap", 540, 880), ("wait", 0.5)]),
            ("14_receipt_thermal_preview", "Pratinjau struk thermal estetik salon nama stylist", [("tap", 540, 2020), ("wait", 0.8), ("back",), ("back",)]),
            ("15_salon_performance_analytics", "Analisis layanan rambut paling diminati", [("route", "/laporan"), ("wait", 0.5)]),
            ("16_finance_cashflow_overview", "Buku kas salon arus kas masuk vs operasional", [("route", "/keuangan"), ("wait", 0.5)]),
            ("17_finance_expense_sheet", "Catat belanja shampoo, obat cat, vitamin rambut", [("route", "/keuangan"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("18_stock_beauty_products", "Stok produk perawatan & barang jualan retail", [("route", "/stok"), ("wait", 0.5)]),
            ("19_stock_opname_audit_sheet", "Form audit stok fisik botol obat rambut", [("route", "/stok"), ("tap", 850, 160), ("wait", 0.5), ("back",)]),
            ("20_transactions_history_list", "Riwayat transaksi perawatan salon", [("route", "/transaksi"), ("wait", 0.5)]),
            ("21_customer_membership_sheet", "Kartu member loyalitas & diskon treatment", [("route", "/pelanggan"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("22_attendance_stylist_shift", "Presensi absensi hair stylist dan terapis", [("route", "/presensi"), ("wait", 0.5)]),
            ("23_settings_printer_setup", "Pengaturan printer thermal Bluetooth 58mm salon", [("route", "/pengaturan"), ("tap", 540, 800), ("wait", 0.6), ("back",)]),
            ("24_settings_lan_pc_connect", "Layar Sambungkan ke Komputer (Web POS salon)", [("route", "/lan-pos"), ("wait", 0.5)]),
        ]
    },
    {
        "folder": "06_apotek",
        "variant": "apotek",
        "onboarding": False,
        "items": [
            ("01_pos_medicine_catalog_grid", "Katalog obat bebas, terbatas, keras (strip/botol)", [("route", "/kasir")]),
            ("02_prescription_doctor_intake_sheet", "Form resep dokter: SIP, pasien, usia, BB", [("route", "/resep"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("03_signa_dosage_rule_picker", "Pilihan aturan pakai cepat (signa 3x1)", [("route", "/resep"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("04_medicine_etiket_print_preview", "Pratinjau cetak etiket obat stiker 58mm", [("route", "/resep"), ("tap", 540, 600), ("tap", 850, 400), ("wait", 0.6), ("back",), ("back",)]),
            ("05_batch_number_expiry_sheet", "Pencatatan nomor batch pabrik & tgl expired", [("route", "/produk"), ("tap", 540, 700), ("wait", 0.5), ("back",)]),
            ("06_cart_apotek_order_active", "Bar keranjang apotek obat bebas & resep", [("tap", 270, 840), ("tap", 810, 840), ("wait", 0.4)]),
            ("07_expiry_date_alert_warning", "Daftar peringatan obat mendekati kadaluarsa", [("route", "/stok"), ("wait", 0.5)]),
            ("08_official_apograph_copy_receipt", "Salinan resep resmi apograph tanda tangan apoteker", [("route", "/resep"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("09_unit_conversion_calculator", "Konversi satuan obat: 1 box = 10 strip = 100 tab", [("route", "/produk"), ("tap", 540, 700), ("wait", 0.5), ("back",)]),
            ("10_controlled_medicine_report", "Laporan buku pengeluaran obat resep", [("route", "/laporan"), ("wait", 0.5)]),
            ("11_payment_methods_sheet", "Layar checkout kasir apotek", [("route", "/kasir"), ("tap", 540, 2230), ("wait", 0.6)]),
            ("12_cash_fast_tender_keypad", "Pembayaran tunai kasir apotek & kembalian", [("tap", 540, 680), ("wait", 0.4)]),
            ("13_qris_dynamic_display", "QRIS dinamis kasir apotek siap scan", [("tap", 540, 880), ("wait", 0.5)]),
            ("14_receipt_thermal_preview", "Nota struk resmi apotek nomor SIP & resep", [("tap", 540, 2020), ("wait", 0.8), ("back",), ("back",)]),
            ("15_apotek_daily_margin_report", "Laporan laba obat bebas vs obat resep", [("route", "/laporan"), ("wait", 0.5)]),
            ("16_finance_cashflow_overview", "Buku kas apotek penjualan vs belanja PBF", [("route", "/keuangan"), ("wait", 0.5)]),
            ("17_finance_expense_sheet", "Catat biaya operasional & perpanjangan SIPA", [("route", "/keuangan"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("18_stock_medicine_inventory", "Daftar stok obat gudang apotek & etalase", [("route", "/stok"), ("wait", 0.5)]),
            ("19_stock_opname_audit_sheet", "Form audit stok opname obat & nomor batch", [("route", "/stok"), ("tap", 850, 160), ("wait", 0.5), ("back",)]),
            ("20_transactions_history_list", "Riwayat transaksi penebusan resep apotek", [("route", "/transaksi"), ("wait", 0.5)]),
            ("21_supplier_pbf_purchase_order", "Surat pesanan obat ke distributor PBF", [("route", "/pembelian"), ("wait", 0.5)]),
            ("22_customer_drug_allergy_record", "Catatan riwayat alergi obat pasien", [("route", "/pelanggan"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("23_settings_printer_setup", "Pengaturan printer struk thermal & etiket obat", [("route", "/pengaturan"), ("tap", 540, 800), ("wait", 0.6), ("back",)]),
            ("24_settings_lan_pc_connect", "Layar Sambungkan ke Komputer (Web POS apoteker)", [("route", "/lan-pos"), ("wait", 0.5)]),
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
            ("06_cart_fotocopy_order_active", "Bar keranjang pesanan cetak & jilid aktif", [("tap", 270, 840), ("tap", 810, 840), ("wait", 0.4)]),
            ("07_pc_portal_file_queue_screen", "Antrean berkas PDF/Word kiriman pelanggan HP", [("route", "/print-portal"), ("wait", 0.6)]),
            ("08_pc_portal_download_detail_modal", "Modal detail berkas & spesifikasi cetak", [("tap", 540, 700), ("wait", 0.5), ("back",)]),
            ("09_fotocopy_job_ticket_receipt", "Struk tanda terima cetak dengan jam selesai", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("10_pc_portal_web_browser_view", "Tampilan desktop monitor operator PC localhost", [("route", "/print-portal"), ("wait", 0.5)]),
            ("11_payment_methods_sheet", "Layar checkout kasir percetakan/fotocopy", [("route", "/kasir"), ("tap", 540, 2230), ("wait", 0.6)]),
            ("12_cash_fast_tender_keypad", "Bayar tunai fotocopy & uang koin receh", [("tap", 540, 680), ("wait", 0.4)]),
            ("13_qris_dynamic_display", "QRIS dinamis counter percetakan siap scan", [("tap", 540, 880), ("wait", 0.5)]),
            ("14_receipt_thermal_preview", "Struk kasir fotocopy rincian jumlah lembar", [("tap", 540, 2020), ("wait", 0.8), ("back",), ("back",)]),
            ("15_fotocopy_daily_sales_recap", "Laporan omzet jasa mesin vs jualan kertas", [("route", "/laporan"), ("wait", 0.5)]),
            ("16_finance_cashflow_overview", "Buku kas operasional fotocopy masuk vs keluar", [("route", "/keuangan"), ("wait", 0.5)]),
            ("17_finance_expense_sheet", "Catat belanja toner, tinta, servis mesin fotocopy", [("route", "/keuangan"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("18_stock_paper_atk_inventory", "Stok kertas rim HVS (A4, F4, A3) & lakban", [("route", "/stok"), ("wait", 0.5)]),
            ("19_stock_opname_audit_sheet", "Form audit stok rim kertas & catatan waste", [("route", "/stok"), ("tap", 850, 160), ("wait", 0.5), ("back",)]),
            ("20_transactions_history_list", "Riwayat transaksi cetak dokumen & ATK", [("route", "/transaksi"), ("wait", 0.5)]),
            ("21_supplier_paper_distributor", "Daftar distributor kertas rim & agen toner", [("route", "/supplier"), ("wait", 0.5)]),
            ("22_attendance_operator_shift", "Presensi operator mesin fotocopy & desainer", [("route", "/presensi"), ("wait", 0.5)]),
            ("23_settings_printer_setup", "Pengaturan printer thermal Bluetooth 58mm/80mm", [("route", "/pengaturan"), ("tap", 540, 800), ("wait", 0.6), ("back",)]),
            ("24_settings_lan_pc_connect", "Layar Sambungkan ke Komputer (Portal File PC)", [("route", "/lan-pos"), ("wait", 0.5)]),
        ]
    },
    {
        "folder": "08_servis",
        "variant": "servis",
        "onboarding": False,
        "items": [
            ("01_pos_sparepart_device_grid", "Katalog suku cadang LCD, baterai, fleksibel", [("route", "/kasir")]),
            ("02_unit_intake_receipt_sheet", "Form tanda terima servis masuk & keluhan rusak", [("route", "/servis"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("03_screen_pattern_pin_draw_sheet", "Lembar gambar pola kunci layar & PIN HP", [("route", "/servis"), ("tap", 540, 600), ("wait", 0.5), ("back",)]),
            ("04_cost_estimate_down_payment_dialog", "Pencatatan estimasi biaya & uang muka DP", [("route", "/servis"), ("tap", 540, 600), ("tap", 850, 300), ("wait", 0.5), ("back",), ("back",)]),
            ("05_cart_servis_order_active", "Bar pesanan servis dan biaya jasa teknisi", [("tap", 270, 840), ("tap", 810, 840), ("wait", 0.4)]),
            ("06_intake_claim_receipt_preview", "Cetak nota tanda terima servis nomor tiket", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("07_repair_status_pipeline_sheet", "Status servis (Masuk, Dicek, Tunggu Part, Selesai)", [("route", "/servis"), ("wait", 0.5)]),
            ("08_whatsapp_service_done_notify_modal", "Modal WA otomatis: HP selesai diperbaiki", [("route", "/servis"), ("tap", 850, 600), ("wait", 0.5), ("back",)]),
            ("09_service_warranty_card_print", "Cetak kartu garansi servis resmi (30 hari)", [("route", "/transaksi"), ("tap", 540, 600), ("wait", 0.6), ("back",)]),
            ("10_technician_commission_payout", "Rekapitulasi komisi teknisi per unit HP", [("route", "/laporan"), ("tap", 540, 1400), ("wait", 0.5), ("back",)]),
            ("11_payment_methods_sheet", "Layar checkout pelunasan biaya servis", [("route", "/kasir"), ("tap", 540, 2230), ("wait", 0.6)]),
            ("12_cash_fast_tender_keypad", "Bayar tunai pelunasan servis & kembalian", [("tap", 540, 680), ("wait", 0.4)]),
            ("13_qris_dynamic_display", "QRIS dinamis counter servis siap scan", [("tap", 540, 880), ("wait", 0.5)]),
            ("14_receipt_thermal_preview", "Struk thermal bukti lunas servis & garansi", [("tap", 540, 2020), ("wait", 0.8), ("back",), ("back",)]),
            ("15_servis_monthly_revenue_report", "Laporan laba usaha servis: jasa vs sparepart", [("route", "/laporan"), ("wait", 0.5)]),
            ("16_finance_cashflow_overview", "Buku kas masuk servis vs operasional konter", [("route", "/keuangan"), ("wait", 0.5)]),
            ("17_finance_expense_sheet", "Catat belanja timah, pasta solder, lem LCD", [("route", "/keuangan"), ("tap", 920, 2120), ("wait", 0.6), ("back",)]),
            ("18_stock_sparepart_lcd_battery", "Stok komponen sparepart LCD & baterai original", [("route", "/stok"), ("wait", 0.5)]),
            ("19_stock_opname_audit_sheet", "Form audit stok komponen sparepart di laci", [("route", "/stok"), ("tap", 850, 160), ("wait", 0.5), ("back",)]),
            ("20_transactions_history_list", "Riwayat unit servis yang selesai & diambil", [("route", "/transaksi"), ("wait", 0.5)]),
            ("21_supplier_sparepart_distributor", "Buku kontak distributor sparepart HP", [("route", "/supplier"), ("wait", 0.5)]),
            ("22_attendance_technician_shift", "Presensi absensi teknisi perbaikan HP", [("route", "/presensi"), ("wait", 0.5)]),
            ("23_settings_printer_setup", "Pengaturan printer thermal nota tiket servis", [("route", "/pengaturan"), ("tap", 540, 800), ("wait", 0.6), ("back",)]),
            ("24_settings_lan_pc_connect", "Layar Sambungkan ke Komputer (Meja Teknisi PC)", [("route", "/lan-pos"), ("wait", 0.5)]),
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
        route_path = action[1]
        run_adb(f'shell am start -n com.nusa.dev/com.example.nusa_kasir.MainActivity -d "nusa://app{route_path}"')
        time.sleep(0.8)


def main():
    print("=" * 80)
    print("📸 NUSA KASIR - MASTER PER-VARIANT ASSET HARVESTER (198 GRANULAR TARGETS)")
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
    
    # 2. Iterasi seluruh 9 grup direktori
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
            
            if actions:
                for act in actions:
                    execute_action(act)
                time.sleep(0.4)
            
            # Capture screenshot
            if capture_clean_screenshot(dest):
                total_captured += 1
            
            time.sleep(0.2)
            
    # 3. Matikan Do Not Disturb
    run_adb("shell cmd notification set_zen_mode 0")
    
    elapsed = time.time() - start_time
    print("\n" + "=" * 80)
    print(f"🎉 SUKSES! Berhasil memanen {total_captured} aset visual dari {len(HARVEST_PLAN)} direktori.")
    print(f"⏱️ Waktu pengerjaan: {elapsed:.1f} detik ({elapsed/60:.1f} menit).")
    print(f"📁 Aset tersimpan rapi di: {OUTPUT_DIR}")
    print("=" * 80)


if __name__ == "__main__":
    main()
