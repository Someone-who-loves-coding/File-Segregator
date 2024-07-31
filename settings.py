import os
import platform
from datetime import datetime

# Determine the current operating system
current_os = platform.system()

# Get the username based on the operating system
if current_os == "Windows":
    USER = os.getenv('USERNAME')
else:  # Assume a Unix-like system (Linux, macOS, etc.)
    USER = os.getenv('USER')

# Define the root directory (Downloads)
ROOT_DIR = os.path.join(os.path.expanduser('~'), 'Downloads')

# Define the date directory
DATE_DIR = os.path.join(ROOT_DIR, datetime.now().strftime('%Y-%m-%d'))

# Define subdirectory paths within the date folder
IMAGE_DIR = os.path.join(DATE_DIR, 'images')
DOCUMENTS_DIR = os.path.join(DATE_DIR, 'documents')
OTHERS_DIR = os.path.join(DATE_DIR, 'others')
SOFTWARE_DIR = os.path.join(DATE_DIR, 'softwares')

# Define file type extensions
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
DOCUMENT_EXTENSIONS = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt']
SOFTWARE_EXTENSIONS = ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm']
