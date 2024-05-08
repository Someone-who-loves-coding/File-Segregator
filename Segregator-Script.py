import os
from shutil import move

def get_non_hidden_files_except_current_file(root_dir):
    """
    Get a list of non-hidden files in the specified directory, excluding the current file.

    Args:
    - root_dir (str): The directory path to search for files.

    Returns:
    - list: A list of non-hidden file names.

    """
    current_file = os.path.basename(__file__)
    return [f for f in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, f)) and not f.startswith('.') and not f == current_file]

def move_files(files, root_dir):
    """
    Move files to respective directories based on their file types.

    Args:
    - files (list): List of file names to be moved.
    - root_dir (str): The root directory where the files are located.

    """
    user = os.getenv('USER')
    image_dir = os.path.join(root_dir, 'images')
    documents_dir = os.path.join(root_dir, 'documents')
    others_dir = os.path.join(root_dir, 'others')
    software_dir = os.path.join(root_dir, 'softwares')

    doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
    img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
    software_types = ('.exe', '.pkg', '.dmg')

    for file in files:
        # Determine file type and move accordingly
        if file.endswith(doc_types):
            dest_dir = documents_dir
        elif file.endswith(img_types):
            dest_dir = image_dir
        elif file.endswith(software_types):
            dest_dir = software_dir
        else:
            dest_dir = others_dir
        
        # Move file to destination directory
        source_path = os.path.join(root_dir, file)
        dest_path = os.path.join(dest_dir, file)
        move(source_path, dest_path)
        print(f'File {file} moved to {dest_dir}')

if __name__ == "__main__":
    user = os.getenv('USER')
    root_dir = f'/Users/{user}/Downloads'
    files = get_non_hidden_files_except_current_file(root_dir)
    move_files(files, root_dir)
