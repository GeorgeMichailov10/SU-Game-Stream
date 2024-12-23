from open_gopro import WirelessGoPro
import numpy as np
import asyncio

class GoProManager:
    def __init__(self, ip_addresses):
        self.ip_addresses = ip_addresses
        self.cameras = [WirelessGoPro(ip_address) for ip_address in self.ip_addresses]
        self.active_camera_index = 0