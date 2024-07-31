# File Segregator Script

This script helps organize files in the Downloads directory by segregating them into respective subdirectories based on their file types.

## Prerequisites

- Python 3.x
- macOS (This script is designed for a macOS environment)

## Installation

1. **Clone the repository to your local machine:**

    ```sh
    git clone https://github.com/Someone-who-loves-coding/File-Segregator.git
    ```

2. **Navigate to the cloned directory:**

    ```sh
    cd File-Segregator
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### 1. Makemydir.py

This script creates a directory with the current date within the 'Downloads' directory and changes the working directory to it.

To run the script, execute the following command:

    ```sh
    python makemydir.py
    ```

### 2. Segregator-Script.py

This script segregates files in the 'Downloads' directory into respective subdirectories based on their file types.

Before running the script, ensure that the `makemydir.py` script has been executed to create the necessary directory structure.

To run the script, execute the following command:

    ```sh
    python segregator-script.py
    ```

## Settings

The `Setting.py` file contains directory paths and file types used by the `Segregator-Script.py` script. Modify these settings as needed.

Example `Setting.py` file:

    ```python
    DOWNLOADS_DIR = "/Users/YourUsername/Downloads"
    FILE_TYPES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mov", ".avi"],
        # Add more file types as needed
    }
    ```

Modify the paths and file types as per your requirements.
