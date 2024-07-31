import os
from datetime import datetime
import platform
import subprocess

# Determine the current operating system
current_os = platform.system()

# Get the username based on the operating system
if current_os == "Windows":
    USER = os.getenv('USERNAME')
else:  # Assume a Unix-like system (Linux, macOS, etc.)
    USER = os.getenv('USER')

# Define the root directory (Downloads)
ROOT_DIR = os.path.join(os.path.expanduser('~'), 'Downloads')

# Create a date folder within the Downloads directory
today_date = datetime.now().strftime('%Y-%m-%d')
DATE_DIR = os.path.join(ROOT_DIR, today_date)
if not os.path.exists(DATE_DIR):
    os.makedirs(DATE_DIR)

print(f"Date directory created: {DATE_DIR}")

# Call the segregator-script.py
subprocess.run(["python", "Segregator_Script.py"])
