import os

# Directory paths
USER = os.getenv('USER')
ROOT_DIR = f'/Users/{USER}/Downloads/'
IMAGE_DIR = f'/Users/{USER}/Downloads/images/'
DOCUMENTS_DIR = f'/Users/{USER}/Downloads/documents/'
OTHERS_DIR = f'/Users/{USER}/Downloads/others/'
SOFTWARE_DIR = f'/Users/{USER}/Downloads/softwares/'

# File types
DOC_TYPES = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
IMG_TYPES = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
SOFTWARE_TYPES = ('.exe', '.pkg', '.dmg')
