import time
import network  # Assuming this is the library being used for WiFi control

class WiFiManager:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def connect(self):
        print(f'Connecting to {self.ssid}...')
        self.wlan.connect(self.ssid, self.password)
        # Retry until connected
        start_time = time.time()
        while not self.wlan.isconnected():
            if time.time() - start_time > 10:  # Timeout after 10 seconds
                print('Connection timed out.')
                return False
            time.sleep(1)  # Wait before trying again
        print('Connected successfully!')
        return True

    def check_connection(self):
        if not self.wlan.isconnected():
            print('WiFi disconnected! Trying to reconnect...')
            self.connect()
        else:
            print('WiFi is connected. Status: ', self.wlan.ifconfig())

    def auto_reconnect(self):
        while True:
            self.check_connection()
            time.sleep(5)  # Check connection status every 5 seconds

# Example usage:
# wifi_manager = WiFiManager('Your_SSID', 'Your_Password')
# wifi_manager.auto_reconnect()