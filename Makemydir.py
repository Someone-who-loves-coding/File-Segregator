import os
import datetime
import settings

def makemydir():
    """
    Create a directory with the current date within the 'Downloads' directory and change the working directory to it.

    Returns:
    - str: The path of the newly created directory.
    """
    try:
        # Get the current date
        current_date = str(datetime.date.today())
        
        # Set the directory name and change the directory to 'Downloads'
        dir_name = os.path.join(settings.ROOT_DIR, current_date)
        os.chdir(settings.ROOT_DIR)
        
        # Create the directory if it doesn't exist
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print(f"Directory '{dir_name}' created successfully.")
        else:
            print(f"Directory '{dir_name}' already exists.")
        
        # Change the working directory to the newly created directory
        os.chdir(dir_name)
        
        return os.getcwd()  # Return the path of the newly created directory
    
    except Exception as e:
        print(f"An error occurred while creating the directory: {e}")

# Example usage:
if __name__ == "__main__":
    new_dir = makemydir()
    print(f"Current working directory: {new_dir}")
