#!/usr/bin/env python3
"""
NUSA Kasir Creator Studio Director Engine
Universal, zero-latency ADB automation with dynamic (%W, %H) responsive scaling.
Auto-calibrated for Samsung Galaxy Z Flip 3 (1080x2640) with dynamic fallback for emulators.
"""

import json
import os
import re
import subprocess
import sys
import time

MATRIX_FILE = os.path.join(os.path.dirname(__file__), "action_matrix.json")

class NusaDirector:
    def __init__(self, device_serial: str = None):
        self.device_serial = device_serial
        self.width = 1080
        self.height = 2640
        self.is_z_flip_3 = False
        self.matrix = self._load_matrix()
        self._detect_device()

    def _load_matrix(self) -> dict:
        if os.path.exists(MATRIX_FILE):
            with open(MATRIX_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _adb_cmd(self, *args) -> str:
        cmd = ["adb"]
        if self.device_serial:
            cmd.extend(["-s", self.device_serial])
        cmd.extend(args)
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return res.stdout.strip()
        except subprocess.CalledProcessError as e:
            return e.stdout.strip() if e.stdout else ""

    def _detect_device(self):
        # 1. Check connected devices
        devices_out = self._adb_cmd("devices")
        lines = [line.split()[0] for line in devices_out.splitlines()[1:] if "device" in line]
        if not lines:
            print("[WARN] No ADB device detected. Running in mock/dry-run mode (1080x2640).")
            return

        if not self.device_serial and lines:
            self.device_serial = lines[0]
            print(f"[DIRECTOR] Connected to ADB device: {self.device_serial}")

        # 2. Get screen size
        size_out = self._adb_cmd("shell", "wm", "size")
        match = re.search(r"(\d+)x(\d+)", size_out)
        if match:
            self.width = int(match.group(1))
            self.height = int(match.group(2))
            print(f"[DIRECTOR] Detected Screen Resolution: {self.width}x{self.height}")

            # Check if Z Flip 3 (1080x2640)
            if self.width == 1080 and self.height == 2640:
                self.is_z_flip_3 = True
                print("[DIRECTOR] Samsung Galaxy Z Flip 3 calibrated preset active.")
            elif self.height / self.width > 2.2:
                print("[DIRECTOR] Ultra-tall aspect ratio detected (22:9). Calibrating layout.")

    def resolve_coords(self, target) -> tuple[int, int]:
        """Resolves target key (e.g. 'pos_screen.product_item_r1_c1') or (x_pct, y_pct) to pixel (x, y)."""
        if isinstance(target, (list, tuple)) and len(target) == 2:
            x_pct, y_pct = float(target[0]), float(target[1])
            return int(self.width * x_pct), int(self.height * y_pct)

        if isinstance(target, str):
            coords_dict = self.matrix.get("normalized_coordinates", {})
            parts = target.split(".")
            val = coords_dict
            for p in parts:
                if isinstance(val, dict):
                    val = val.get(p)
            if isinstance(val, dict) and "x" in val and "y" in val:
                return int(self.width * float(val["x"])), int(self.height * float(val["y"]))

        raise ValueError(f"Target '{target}' not found in action matrix or invalid format.")

    def tap(self, target, delay_after: float = 0.3):
        x, y = self.resolve_coords(target)
        print(f"[TAP] -> ({x}, {y}) [{target}]")
        self._adb_cmd("shell", "input", "tap", str(x), str(y))
        if delay_after > 0:
            time.sleep(delay_after)

    def double_tap(self, target, delay_between: float = 0.12, delay_after: float = 0.3):
        x, y = self.resolve_coords(target)
        print(f"[DOUBLE TAP] -> ({x}, {y})")
        self._adb_cmd("shell", "input", "tap", str(x), str(y))
        time.sleep(delay_between)
        self._adb_cmd("shell", "input", "tap", str(x), str(y))
        if delay_after > 0:
            time.sleep(delay_after)

    def swipe(self, from_target, to_target, duration_ms: int = 350, delay_after: float = 0.3):
        x1, y1 = self.resolve_coords(from_target)
        x2, y2 = self.resolve_coords(to_target)
        print(f"[SWIPE] -> ({x1}, {y1}) to ({x2}, {y2}) in {duration_ms}ms")
        self._adb_cmd("shell", "input", "swipe", str(x1), str(y1), str(x2), str(y2), str(duration_ms))
        if delay_after > 0:
            time.sleep(delay_after)

    def type_text(self, text: str, delay_after: float = 0.3):
        safe_text = text.replace(" ", "%s")
        print(f"[TYPE] -> '{text}'")
        self._adb_cmd("shell", "input", "text", safe_text)
        if delay_after > 0:
            time.sleep(delay_after)

    def key(self, keycode: int, delay_after: float = 0.2):
        self._adb_cmd("shell", "input", "keyevent", str(keycode))
        if delay_after > 0:
            time.sleep(delay_after)

    def cheat(self, action: str, variant: str = None, pro: bool = True):
        """Dispatches silent background cheat intent directly to Flutter without debug UI."""
        cmd_args = ["shell", "am", "start", "-n", "com.nusa.kelontong/com.example.nusa_kasir.MainActivity"]
        cmd_args.extend(["--es", "action", action.upper()])
        if variant:
            cmd_args.extend(["--es", "variant", variant])
        if pro is not None:
            cmd_args.extend(["--ez", "pro", "true" if pro else "false"])

        print(f"[CHEAT] Dispatching silent action '{action}' (variant={variant}, pro={pro})")
        self._adb_cmd(*cmd_args)
        time.sleep(0.5)

    def wait(self, seconds: float):
        """Pacing pause matching voiceover word-boundary synchronization."""
        print(f"[PACING] Holding frame for {seconds:.2f}s...")
        time.sleep(seconds)


if __name__ == "__main__":
    director = NusaDirector()
    print("NusaDirector initialized successfully. Ready for dynamic screen choreography.")
