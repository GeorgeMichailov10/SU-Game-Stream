from open_gopro import WirelessGoPro
import numpy as np
import cv2
import asyncio
import threading
import time
from typing import List
import os
import dotenv
# from ball_tracking import BallTracker
import sys
import signal

dotenv.load_dotenv()

class GoProManager:
    def __init__(self, ip_addresses):
        # self.ip_addresses = ip_addresses
        self.cameras = [cv2.VideoCapture(0)]
        self.camera_locks = [threading.Lock() for _ in self.cameras]
        self.active_camera_index = 0
        self.last_frame_buffers: List[np.ndarray] = [None] * len(self.cameras)
        self.active_stream_frame_buffer: np.ndarray = None
        # self.ball_tracker = BallTracker()
        self.active_stream_lock = threading.Lock()
        self.last_frame_lock = threading.Lock()
        self.continue_stream = True


    def start_processes(self):
        self.stream_webcam_thread = threading.Thread(target=self.stream_webcam)
        self.display_last_frame_buffer_thread = threading.Thread(target=self.display_last_frame_buffer)
        # self.forward_active_stream_frame_buffer_thread = threading.Thread(target=self.forward_active_stream_frame_buffer)
        # self.active_camera_controller_thread = threading.Thread(target=self.active_camera_controller)

        self.stream_webcam_thread.start()
        self.display_last_frame_buffer_thread.start()
        # self.forward_active_stream_frame_buffer_thread.start()
        # self.active_camera_controller_thread.start()

    # Thread 1: Accept video feed from webcam and store every x frames of active camera
    # in last_frame_buffers and active_stream_frame_buffer.
    def stream_webcam(self):
        count = 0
        while self.continue_stream:
            ret, frame = self.cameras[self.active_camera_index].read()
            if ret:
                cv2.imshow("Active Stream Buffer", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.stop()

                with self.active_stream_lock:
                    self.active_stream_frame_buffer = frame
                if count % 5 == 0:
                    with self.last_frame_lock:
                        self.last_frame_buffers[self.active_camera_index] = frame
                count += 1

    def display_last_frame_buffer(self):
        while self.continue_stream:
            with self.last_frame_lock:
                last_frame = self.last_frame_buffers[self.active_camera_index]
            if last_frame is not None:
                # Display the last frame buffer
                cv2.imshow("Last Frame Buffer", last_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop()
            time.sleep(0.1)

    # Thread 2: Forward active_stream_frame_buffer to ball_tracker.
    def forward_active_stream_frame_buffer(self):
        while self.continue_stream:
            pass

    # Thread 3: Control active camera.
    def active_camera_controller(self):
        while True:
            pass

    def kill_stream_controller(self):
        print("Stopping all streams...")
        self.continue_stream = False
        for camera in self.cameras:
            camera.release()
        self.stream_webcam_thread.join()
        cv2.destroyAllWindows()
        print("All resources released.")

    
        