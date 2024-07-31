import os
import shutil
from settings import ROOT_DIR, DATE_DIR, IMAGE_DIR, DOCUMENTS_DIR, OTHERS_DIR, SOFTWARE_DIR
from settings import IMAGE_EXTENSIONS, DOCUMENT_EXTENSIONS, SOFTWARE_EXTENSIONS

# Function to create directory if not exists
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Function to move file to respective directory
def move_file(file, src_dir, dest_dir):
    src_path = os.path.join(src_dir, file)
    dest_path = os.path.join(dest_dir, file)
    shutil.move(src_path, dest_path)

# Ensure the date directory exists
if not os.path.exists(DATE_DIR):
    os.makedirs(DATE_DIR)

# Iterate through the files in the Downloads directory
for file in os.listdir(ROOT_DIR):
    file_path = os.path.join(ROOT_DIR, file)
    
    # Skip if it's a directory
    if os.path.isdir(file_path):
        continue
    
    # Check file extension and move to respective directory inside the date folder
    _, file_extension = os.path.splitext(file)
    
    if file_extension.lower() in IMAGE_EXTENSIONS:
        create_directory(IMAGE_DIR)
        move_file(file, ROOT_DIR, IMAGE_DIR)
    elif file_extension.lower() in DOCUMENT_EXTENSIONS:
        create_directory(DOCUMENTS_DIR)
        move_file(file, ROOT_DIR, DOCUMENTS_DIR)
    elif file_extension.lower() in SOFTWARE_EXTENSIONS:
        create_directory(SOFTWARE_DIR)
        move_file(file, ROOT_DIR, SOFTWARE_DIR)
    else:
        create_directory(OTHERS_DIR)
        move_file(file, ROOT_DIR, OTHERS_DIR)

print("Files have been segregated successfully.")
