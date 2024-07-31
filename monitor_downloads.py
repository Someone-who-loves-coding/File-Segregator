import time
import os
import signal
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DownloadsHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Check if a file has been created
        if not event.is_directory:
            print(f"File created: {event.src_path}")
            # Run the makemydir.py script
            subprocess.run(["python", "makemydir.py"])

def signal_handler(sig, frame):
    print('Shutdown signal received. Stopping the observer...')
    observer.stop()

if __name__ == "__main__":
    # Define the Downloads directory to watch
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    event_handler = DownloadsHandler()
    observer = Observer()
    observer.schedule(event_handler, downloads_path, recursive=False)

    # Start the observer
    observer.start()
    print(f"Monitoring {downloads_path} for new files...")

    # Register the signal handler
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print('Observer stopped.')
