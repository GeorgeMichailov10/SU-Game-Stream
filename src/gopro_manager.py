from open_gopro import WirelessGoPro
import numpy as np
import cv2
import asyncio
import threading
import time
from typing import List, Optional
import os
import dotenv

dotenv.load_dotenv()

class GoProManager:
    def __init__(self, ip_addresses):
        self.ip_addresses = ip_addresses
        self.cameras = [cv2.VideoCapture(0)]
        self.active_camera_index = 0
        self.last_frame_buffers = [None]
        self.active_stream_frame_buffer = None


    def start_streams(self):
        pass

    def stop_streams(self):
        pass

    def switch_camera(self, index: int):
        pass

    
        
