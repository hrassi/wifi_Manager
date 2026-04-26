from wifi_connect import wifi_loop
from machine import WDT
import time

wdt = WDT(timeout=30000)  # 30 seconds


MyNetwork = "Rassi Net3"
MyPassword = "Holyshit"


# ───── 1. WAIT FOR WIFI AT STARTUP OPTIONAL ─────
print("[System] Connecting to WiFi...")
while not wifi_loop(MyNetwork, MyPassword):
    time.sleep_ms(500)
print("[System] WiFi connected!")



while True:
    wifi_loop(MyNetwork, MyPassword)

    # Your system runs freely here (MQTT, sensors, UI, etc.)
    wdt.feed()           # reset watchdog timer
    time.sleep_ms(100)