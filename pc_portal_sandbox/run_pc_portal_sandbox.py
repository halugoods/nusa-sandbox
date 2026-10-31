#!/usr/bin/env python3
"""
NUSA PC Portal & Web POS Sandbox Server (Halu Goods Studio)
============================================================
Tool serbaguna untuk Agent Editor Konten & Creator Studio dalam mendemokan
fitur "Sambungkan ke Komputer" (Web POS & Portal File Fotocopy/Percetakan).

Fitur:
1. Auto-ADB Bridge: Jika HP Android tercolok, otomatis jalankan `adb forward tcp:8080 tcp:8080`.
2. Standalone Fallback Microserver: Jika HP tidak tercolok atau ingin preview instan di PC,
   server ini menyajikan Web POS dan Portal File lengkap dengan mock data dan unduh berkas asli.
3. Zero-dependency: Berjalan murni menggunakan Python standard library (http.server).
"""

import http.server
import socketserver
import os
import sys
import json
import subprocess
import webbrowser
import urllib.parse
from datetime import datetime

PORT = 8080
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = CUR_DIR if os.path.exists(os.path.join(CUR_DIR, 'portal_file_sandbox.html')) else os.path.join(CUR_DIR, '..', 'assets')

# Dummy Minimal Valid PDF bytes
MINIMAL_PDF_BYTES = bytes([
    0x25, 0x50, 0x44, 0x46, 0x2d, 0x31, 0x2e, 0x34, 0x0a, 0x31, 0x20, 0x30, 0x20, 0x6f, 0x62, 0x6a,
    0x3c, 0x3c, 0x2f, 0x54, 0x79, 0x70, 0x65, 0x2f, 0x43, 0x61, 0x74, 0x61, 0x6c, 0x6f, 0x67, 0x2f,
    0x50, 0x61, 0x67, 0x65, 0x73, 0x20, 0x32, 0x20, 0x30, 0x20, 0x52, 0x3e, 0x3e, 0x65, 0x6e, 0x64,
    0x6f, 0x62, 0x6a, 0x0a, 0x32, 0x20, 0x30, 0x20, 0x6f, 0x62, 0x6a, 0x3c, 0x3c, 0x2f, 0x54, 0x79,
    0x70, 0x65, 0x2f, 0x50, 0x61, 0x67, 0x65, 0x73, 0x2f, 0x4b, 0x69, 0x64, 0x73, 0x5b, 0x33, 0x20,
    0x30, 0x20, 0x52, 0x5d, 0x2f, 0x43, 0x6f, 0x75, 0x6e, 0x74, 0x20, 0x31, 0x3e, 0x3e, 0x65, 0x6e,
    0x64, 0x6f, 0x62, 0x6a, 0x0a, 0x33, 0x20, 0x30, 0x20, 0x6f, 0x62, 0x6a, 0x3c, 0x3c, 0x2f, 0x54,
    0x79, 0x70, 0x65, 0x2f, 0x50, 0x61, 0x67, 0x65, 0x2f, 0x4d, 0x65, 0x64, 0x69, 0x61, 0x42, 0x6f,
    0x78, 0x5b, 0x30, 0x20, 0x30, 0x20, 0x35, 0x39, 0x35, 0x20, 0x38, 0x34, 0x32, 0x5d, 0x2f, 0x50,
    0x61, 0x72, 0x65, 0x6e, 0x74, 0x20, 0x32, 0x20, 0x30, 0x20, 0x52, 0x2f, 0x52, 0x65, 0x73, 0x6f,
    0x75, 0x72, 0x63, 0x65, 0x73, 0x3c, 0x3c, 0x3e, 0x3e, 0x3e, 0x3e, 0x65, 0x6e, 0x64, 0x6f, 0x62,
    0x6a, 0x0a, 0x78, 0x72, 0x65, 0x66, 0x0a, 0x30, 0x20, 0x34, 0x0a, 0x30, 0x30, 0x30, 0x30, 0x30,
    0x30, 0x30, 0x30, 0x30, 0x30, 0x20, 0x36, 0x35, 0x35, 0x33, 0x35, 0x20, 0x66, 0x20, 0x0a, 0x30,
    0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x39, 0x20, 0x30, 0x30, 0x30, 0x30, 0x30, 0x20,
    0x6e, 0x20, 0x0a, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x35, 0x32, 0x20, 0x30, 0x30,
    0x30, 0x30, 0x30, 0x20, 0x6e, 0x20, 0x0a, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30,
    0x32, 0x20, 0x30, 0x30, 0x30, 0x30, 0x30, 0x20, 0x6e, 0x20, 0x0a, 0x74, 0x72, 0x61, 0x69, 0x6c,
    0x65, 0x72, 0x3c, 0x3c, 0x2f, 0x53, 0x69, 0x7a, 0x65, 0x20, 0x34, 0x2f, 0x52, 0x6f, 0x6f, 0x74,
    0x20, 0x31, 0x20, 0x30, 0x20, 0x52, 0x3e, 0x3e, 0x0a, 0x73, 0x74, 0x61, 0x72, 0x74, 0x78, 0x72,
    0x65, 0x66, 0x0a, 0x31, 0x37, 0x38, 0x0a, 0x25, 0x25, 0x45, 0x4f, 0x46
])

# Mock Print Orders
MOCK_PRINT_ORDERS = [
    {
        "id": 1,
        "customerName": "Budi Santoso",
        "customerPhone": "081234567890",
        "serviceType": "Jilid Hardcover Skripsi",
        "pages": 140,
        "copies": 3,
        "paperSize": "A4",
        "widthCm": 0,
        "lengthCm": 0,
        "total": 135000,
        "status": "Selesai",
        "estimateReady": "Besok 14:00",
        "notes": "Cover biru tua tinta emas | Skripsi_Budi_Santoso_Bab_1-5.pdf",
        "createdAt": datetime.now().isoformat(),
        "files": [
            {
                "name": "Skripsi_Budi_Santoso_Bab_1-5.pdf",
                "fileName": "demo_skripsi_budi.pdf",
                "size": 2450000,
                "category": "Jilid Hardcover",
                "copies": 3,
                "color": "Hitam Putih",
                "paper": "A4",
                "finishing": "Hardcover Tinta Emas",
                "note": "Cover biru tua tinta emas"
            }
        ]
    },
    {
        "id": 2,
        "customerName": "Siti Nurhaliza",
        "customerPhone": "081388990011",
        "serviceType": "Print Warna Laser",
        "pages": 1,
        "copies": 50,
        "paperSize": "A4",
        "widthCm": 0,
        "lengthCm": 0,
        "total": 75000,
        "status": "Diproses",
        "estimateReady": "Hari ini 16:00",
        "notes": "Kertas Art Paper 150gr untuk brosur promo | Brosur_Promo_Toko_Siti.pdf",
        "createdAt": datetime.now().isoformat(),
        "files": [
            {
                "name": "Brosur_Promo_Toko_Siti.pdf",
                "fileName": "demo_brosur_promo.pdf",
                "size": 1820000,
                "category": "Print Warna Laser",
                "copies": 50,
                "color": "Warna",
                "paper": "A4",
                "finishing": "Art Paper 150gr",
                "note": "Cetak resolusi tinggi untuk pameran"
            }
        ]
    },
    {
        "id": 3,
        "customerName": "Pak RT Joko",
        "customerPhone": "085712345678",
        "serviceType": "Fotocopy B/W",
        "pages": 2,
        "copies": 100,
        "paperSize": "F4",
        "widthCm": 0,
        "lengthCm": 0,
        "total": 60000,
        "status": "Menunggu",
        "estimateReady": "1 Jam Selesai",
        "notes": "Surat edaran iuran warga RW 05 | Surat_Edaran_Iuran_RW05.pdf",
        "createdAt": datetime.now().isoformat(),
        "files": [
            {
                "name": "Surat_Edaran_Iuran_RW05.pdf",
                "fileName": "demo_surat_edaran.pdf",
                "size": 450000,
                "category": "Fotocopy B/W",
                "copies": 100,
                "color": "Hitam Putih",
                "paper": "F4",
                "finishing": "Stapler Kiri Atas",
                "note": "Bolak-balik rangkap 100 lembar"
            }
        ]
    },
    {
        "id": 4,
        "customerName": "Hendra Wijaya",
        "customerPhone": "082111223344",
        "serviceType": "Laminating Panas",
        "pages": 2,
        "copies": 1,
        "paperSize": "A4",
        "widthCm": 0,
        "lengthCm": 0,
        "total": 10000,
        "status": "Diambil",
        "notes": "Ijazah & Transkrip nilai asli | Ijazah_Transkrip_Asli.pdf",
        "createdAt": datetime.now().isoformat(),
        "files": [
            {
                "name": "Ijazah_Transkrip_Asli.pdf",
                "fileName": "demo_ijazah_transkrip.pdf",
                "size": 3210000,
                "category": "Laminating Panas",
                "copies": 1,
                "color": "Warna",
                "paper": "A4",
                "finishing": "Laminating Tebal 100 micron",
                "note": "Hati-hati jangan sampai terlipat"
            }
        ]
    }
]

# Mock Products for Standalone Web POS
MOCK_PRODUCTS = [
    {"id": 1, "name": "Fotocopy B/W (Hitam Putih)", "price": 300, "category": "Fotocopy", "stock": 9999, "barcode": "FC01"},
    {"id": 2, "name": "Print Warna Laser A4", "price": 1500, "category": "Print", "stock": 9999, "barcode": "PR01"},
    {"id": 3, "name": "Print Hitam Putih A4", "price": 500, "category": "Print", "stock": 9999, "barcode": "PR02"},
    {"id": 4, "name": "Jilid Hardcover Skripsi Tinta Emas", "price": 35000, "category": "Jilid", "stock": 50, "barcode": "JL01"},
    {"id": 5, "name": "Jilid Spiral Kawat A4", "price": 15000, "category": "Jilid", "stock": 100, "barcode": "JL02"},
    {"id": 6, "name": "Jilid Lakban Biasa", "price": 5000, "category": "Jilid", "stock": 200, "barcode": "JL03"},
    {"id": 7, "name": "Laminating Panas A4", "price": 5000, "category": "Laminating", "stock": 500, "barcode": "LM01"},
    {"id": 8, "name": "Kertas HVS A4 75gr (1 Rim)", "price": 48000, "category": "ATK", "stock": 85, "barcode": "ATK01"},
    {"id": 9, "name": "Kertas HVS F4 75gr (1 Rim)", "price": 52000, "category": "ATK", "stock": 60, "barcode": "ATK02"},
    {"id": 10, "name": "Map Folio Dokumen", "price": 2500, "category": "ATK", "stock": 250, "barcode": "ATK03"},
]

class SandboxHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # 1. Routes to HTML pages
        if path in ['/', '/pos', '/index.html']:
            html_file = os.path.join(ASSETS_DIR, 'web_pos_sandbox.html')
            if os.path.exists(html_file):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                with open(html_file, 'rb') as f:
                    self.wfile.write(f.read())
                return

        if path in ['/portal-file', '/files', '/operator', '/operator-cetak', '/antrean-cetak']:
            html_file = os.path.join(ASSETS_DIR, 'portal_file_sandbox.html')
            if os.path.exists(html_file):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                with open(html_file, 'rb') as f:
                    self.wfile.write(f.read())
                return

        # 2. Mock APIs
        if path in ['/api/print-order/files', '/api/print-orders']:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True, 'orders': MOCK_PRINT_ORDERS}).encode('utf-8'))
            return

        if path == '/api/print-order/download':
            file_name = query.get('file', ['dokumen.pdf'])[0]
            orig_name = query.get('name', [file_name])[0]
            self.send_response(200)
            self.send_header('Content-Type', 'application/pdf')
            if query.get('download', ['0'])[0] == '1':
                self.send_header('Content-Disposition', f'attachment; filename="{orig_name}"')
            else:
                self.send_header('Content-Disposition', f'inline; filename="{orig_name}"')
            self.end_headers()
            self.wfile.write(MINIMAL_PDF_BYTES)
            return

        if path == '/api/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'ok': True,
                'appName': 'NUSA Kasir Studio Sandbox',
                'brandName': 'Digital Copy & Print',
                'variant': 'nusa-fotocopy',
                'isLite': False,
                'port': PORT,
                'serverUrl': f'http://127.0.0.1:{PORT}',
                'authorizedClientsCount': 1
            }).encode('utf-8'))
            return

        if path == '/api/session':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'ok': True,
                'token': 'sandbox-session-pc-100',
                'isAuthorized': True,
                'qrSvg': '<svg xmlns="http://www.w3.org/2000/svg" width="160" height="160"><rect width="100%" height="100%" fill="#fff"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="14" fill="#333">QR SANDBOX</text></svg>',
                'isLite': False
            }).encode('utf-8'))
            return

        if path == '/api/auth/poll':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True, 'isAuthorized': True}).encode('utf-8'))
            return

        if path == '/api/products':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True, 'products': MOCK_PRODUCTS}).encode('utf-8'))
            return

        if path == '/api/categories':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            cats = list(set(p['category'] for p in MOCK_PRODUCTS))
            self.send_response(200)
            self.wfile.write(json.dumps({'ok': True, 'categories': cats}).encode('utf-8'))
            return

        if path == '/api/sync/version':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True, 'version': 100, 'timestamp': int(datetime.now().timestamp() * 1000)}).encode('utf-8'))
            return

        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(length).decode('utf-8') if length > 0 else '{}'
        try:
            payload = json.loads(body)
        except Exception:
            payload = {}

        if path == '/api/print-order/status':
            order_id = payload.get('id')
            status = payload.get('status')
            for o in MOCK_PRINT_ORDERS:
                if o['id'] == order_id:
                    o['status'] = status
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True, 'id': order_id, 'status': status}).encode('utf-8'))
            return

        if path == '/api/auth/pin':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True, 'message': 'Otorisasi Berhasil! Komputer terhubung.'}).encode('utf-8'))
            return

        if path == '/api/checkout':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'ok': True,
                'transactionId': 9999,
                'invoiceNumber': 'INV/20261028/001',
                'change': payload.get('cashPaid', 0) - payload.get('total', 0)
            }).encode('utf-8'))
            return

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'ok': True}).encode('utf-8'))


def check_adb_and_forward():
    try:
        res = subprocess.run(['adb', 'devices'], capture_output=True, text=True, timeout=3)
        lines = [line.strip() for line in res.stdout.strip().split('\n')[1:] if line.strip() and not line.startswith('*')]
        if lines:
            print(f"[ADB] Ditemukan {len(lines)} perangkat terhubung.")
            test_res = subprocess.run(['adb', 'shell', 'netstat -tuln 2>/dev/null | grep 8080'], capture_output=True, text=True, timeout=2)
            if '8080' in test_res.stdout:
                subprocess.run(['adb', 'forward', f'tcp:{PORT}', f'tcp:{PORT}'], check=False)
                print(f"[ADB] Port forwarding aktif: tcp:{PORT} -> tcp:{PORT}")
                return True
            else:
                print("[ADB] NUSA Kasir LAN Server di HP belum menyala. Berjalan dalam Mode Standalone Sandbox.")
                return False
        else:
            print("[ADB] Tidak ada perangkat fisik/emulator terdeteksi. Menggunakan Mode Standalone Sandbox.")
            return False
    except Exception as e:
        print(f"[ADB] Warning ({e}). Berjalan dalam Mode Standalone Sandbox.")
        return False


def main():
    has_device = check_adb_and_forward()
    print("=" * 60)
    print(" [NUSA PC PORTAL & WEB POS STUDIO SANDBOX SERVER] ")
    print("=" * 60)
    print(f">> Antrean File Fotocopy : http://localhost:{PORT}/portal-file")
    print(f">> Web POS Layar Penuh   : http://localhost:{PORT}/pos")
    print("=" * 60)

    # Buka browser otomatis
    portal_url = f"http://localhost:{PORT}/portal-file"
    print(f"Membuka browser otomatis ke: {portal_url}")
    webbrowser.open(portal_url)

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), SandboxHandler) as httpd:
        print("Server berjalan. Tekan Ctrl+C untuk berhenti.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer dihentikan.")


if __name__ == '__main__':
    main()
