from goprocam import GoProCamera, constants

# Define GoPro IPs (replace with actual IPs)
gopro_ips = ["10.5.5.9", "10.5.5.10"]

gopros = [GoProCamera.GoPro(ip=ip) for ip in gopro_ips]

# Example: Start Recording on All GoPros
for gopro in gopros:
    gopro.shoot_video()

print("All GoPros are recording!")
