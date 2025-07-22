import shutil

# Source path (USB drive)
source_path = r"E:\Arushree HD.mpg"

# Destination path (D drive)
destination_path = r"D:\Arushree HD.mpg"

try:
    shutil.copy2(source_path, destination_path)
    print("File transferred successfully! 🌈")
except Exception as e:
    print("Error while transferring file:", e)
