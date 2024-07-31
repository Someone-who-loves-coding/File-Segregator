Sure! Here is the content for the `README.md` file:

```markdown
# File Segregator Script

This script helps organize files in the Downloads directory by segregating them into respective subdirectories based on their file types.

## Prerequisites

- Python 3.x
- Windows (This script is designed for Windows environment)
```

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Someone-who-loves-coding/File-Segregator.git
```

2. Navigate to the cloned directory:

```bash
cd File-Segregator
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Setup Task Scheduler

This script sets up a Task Scheduler entry to automatically run the file segregation script at system startup.

To set up the Task Scheduler entry, run the following command with administrative privileges:

```bash
python setup_task.py
```

To remove the Task Scheduler entry, run:

```bash
python setup_task.py remove
```

### 2. Monitor Downloads Folder

The `monitor_downloads.py` script monitors the Downloads folder and triggers the file segregation script whenever a new file is downloaded.

This script will be automatically started at system startup after setting up the Task Scheduler entry. You do not need to run it manually.

### 3. Directory Creation and File Segregation

The `makemydir.py` script creates a directory with the current date within the 'Downloads' directory and segregates files into respective subdirectories based on their file types.

This script is automatically called by `monitor_downloads.py` when a new file is detected.

## Scripts

### setup_task.py

This script sets up and removes the Task Scheduler entry to run `monitor_downloads.py` at system startup.

### monitor_downloads.py

This script monitors the Downloads directory for new files and runs `makemydir.py` to segregate them.

### makemydir.py

This script creates a directory with the current date within the 'Downloads' directory and segregates files into respective subdirectories based on their file types.

## Settings

No additional settings are required. The script automatically detects the Downloads directory and segregates files based on their extensions.

### Additional Notes

- Ensure you run `setup_task.py` with administrative privileges to create the Task Scheduler entry.
- The script will automatically handle starting at system startup, monitoring the Downloads folder, and segregating files without any manual intervention from the user.
- Make sure the scripts are all located in the same directory for proper execution.
