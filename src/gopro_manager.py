from open_gopro import WirelessGoPro
import numpy as np
import asyncio

class GoProManager:
    def __init__(self, ip_addresses):
        self.ip_addresses = ip_addresses
        self.cameras = [WirelessGoPro(ip_address) for ip_address in self.ip_addresses]
        self.active_camera_index = 0

    def connect_camera(self):
        self.camera.open()
        print(f"Connected to camera {self.camera.identifier}")

    def read_default_frame(self):
        frame = self.cameras[self.active_camera_index].read_frame()  # Assuming this returns a NumPy array
        if frame is None:
            # Return a black frame if no frame is available
            return np.zeros((720, 1280, 3), dtype=np.uint8)
        return frame