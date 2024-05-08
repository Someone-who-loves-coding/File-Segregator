import os
import Makemydir
import Segregator_Script
import settings

if __name__ == "__main__":
    new_dir = Makemydir.makemydir()
    print(f"Current working directory: {new_dir}")

    root_dir = os.path.join(settings.ROOT_DIR, new_dir)
    files = Segregator_Script.get_non_hidden_files_except_current_file(root_dir)
    Segregator_Script.move_files(files, root_dir)
