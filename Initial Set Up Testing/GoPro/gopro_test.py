import cv2

# RTMP stream URL (replace with your actual RTMP URL)
rtmp_url = "rtmp://192.168.1.100:1935/live/test>"

# Open a connection to the RTMP stream
cap = cv2.VideoCapture(rtmp_url)

if not cap.isOpened():
    print("Error: Unable to open the RTMP stream.")
    exit()

print("RTMP stream opened successfully. Press 'q' to quit.")

# Continuously grab frames and display them
while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Unable to grab a frame from the stream.")
        break

    # Display the frame in a CV2 window
    cv2.imshow("GoPro Stream", frame)

    # Press 'q' to quit the stream viewer
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()