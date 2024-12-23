# Project Plan

### GoProManager

#### Responsibilities

- Connect to the GoPros using the static IPs in the .env file.
- Thread 1: Accept the video feeds from each connected GoPro and store every x frames in a buffer to act as the last frame. (Due to high fps and accuracy needs, it doesn't make sense to store every frame.)
- Thread 2: Forward along the video feed from the selected GoPro to the VideoPublisher class.
- Async Function 1: Wait for a signal from BallTracker class and then pass the last frame buffer from each GoPro to the BallTracker class.
- Async Function 2: When given an index from the Algorithm class, switch the active camera to the GoPro at the given index.

#### Attributes

- active_camera_index: int
- cameras: list[GoPro]
- last_frame_buffers: list[np.ndarray]
- active_stream_frame_buffer: np.ndarray

#### Methods

- start_streams(): void
- stop_streams(): void
- async switch_camera(index: int): void:
- async pass_latest_frame_buffer_to_ball_tracker(): void
-

### BallTracker

#### Responsibilities

- Open and start yolov7 upon initialization.
- Signal the GoProManager to pass the last frame buffer.
- Calculate the bounding box of the ball in the frame.
- Call the async algorithm function with the bounding boxes to calculate the position of the ball and if necessary, send a message to GoProManager to switch cameras.

#### Attributes

- yolov7_model: YOLOv7
- last_frames_buffer: list[np.ndarray]
- ball_bounding_boxes: list[list[int]]
- previous_ball_positions: list[list[int]]

#### Methods

- signal_next_batch(): void
- calculate_ball_positions(): list[list[int]]

### Algorithm

#### Responsibilities

- Determine the best camera to switch to based on the ball's position.
- Send the index of the best camera to the GoProManager if different from the current camera.
- Store multiple algorithms to switch between depending on choice of user.

#### Attributes
