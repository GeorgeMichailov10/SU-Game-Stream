import subprocess
import platform
import cv2
from OpenGoPro import WirelessGoPro

# List of static IPs for the GoPros
gopro_ips = ["10.5.5.100", "10.5.5.101"]  # Replace with your GoPro IPs

# Function to check if a GoPro is reachable
def is_reachable(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    try:
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Initialize GoPro instances using the OpenGoPro SDK
gopros = []
for ip in gopro_ips:
    if is_reachable(ip):
        try:
            print(f"Connecting to GoPro at {ip}...")
            gopro = WirelessGoPro(ip)  # Create a GoPro instance using the OpenGoPro SDK
            gopro.connect()  # Establish a connection
            gopros.append((ip, gopro))
            print(f"Connected to GoPro at {ip}.")
        except Exception as e:
            print(f"Failed to connect to GoPro at {ip}: {e}")
    else:
        print(f"GoPro at {ip} is not reachable. Skipping...")

# Function to start recording on all reachable GoPros
def start_recording():
    for ip, gopro in gopros:
        try:
            print(f"Starting recording on GoPro ({ip})...")
            gopro.command("start")  # Send the start command
            print(f"GoPro ({ip}) is now recording!")
        except Exception as e:
            print(f"Failed to start recording on GoPro ({ip}): {e}")

# Function to display live preview from each GoPro
def live_preview():
    for ip, gopro in gopros:
        try:
            print(f"Accessing live preview for GoPro ({ip})...")
            stream_url = f"http://{ip}:8080/live"  # Replace with actual stream URL if different
            cap = cv2.VideoCapture(stream_url)

            while True:
                ret, frame = cap.read()
                if not ret:
                    print(f"Failed to retrieve frame from GoPro ({ip}).")
                    break
                
                cv2.imshow(f"GoPro {ip} Live Feed", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"Error accessing live preview for GoPro ({ip}): {e}")

# Main function
if __name__ == "__main__":
    if not gopros:
        print("No reachable GoPros. Exiting...")
        exit(1)
    
    print("Starting recording on all reachable GoPros...")
    start_recording()

    print("Displaying live previews...")
    live_preview()
