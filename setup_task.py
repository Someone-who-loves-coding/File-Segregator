import os
import subprocess
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def create_task_scheduler_entry():
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    monitor_script_path = os.path.join(script_dir, 'monitor_downloads.py')
    python_executable = sys.executable

    # Task Scheduler command
    task_name = "MonitorDownloadsFolder"
    create_task_command = f'''
    schtasks /create /f /tn "{task_name}" /tr "{python_executable} {monitor_script_path}" /sc onlogon /rl highest
    '''
    print("Creating Task Scheduler entry...")
    subprocess.run(create_task_command, shell=True)

def remove_task_scheduler_entry():
    task_name = "MonitorDownloadsFolder"
    remove_task_command = f'schtasks /delete /tn "{task_name}" /f'
    print("Removing Task Scheduler entry...")
    subprocess.run(remove_task_command, shell=True)

if __name__ == "__main__":
    if not is_admin():
        print("This script requires administrative privileges.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        if len(sys.argv) > 1 and sys.argv[1] == "remove":
            remove_task_scheduler_entry()
        else:
            create_task_scheduler_entry()
