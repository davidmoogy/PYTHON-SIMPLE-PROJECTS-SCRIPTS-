import os
import shutil
import datetime

def create_backup(source_dirs, backup_dir):
    """
    Creates a backup of specified directories.
    
    :param source_dirs: List of directories to backup
    :param backup_dir: Directory where backups will be stored
    """
    # Get current date and time for timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f"backup_{timestamp}.zip"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    # Create a backup ZIP file
    with shutil.ZipFile(backup_path, 'w') as backup_zip:
        for folder in source_dirs:
            # Walk through the directory and add files to the ZIP file
            for root, dirs, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Add file to the ZIP archive with relative path
                    backup_zip.write(file_path, os.path.relpath(file_path, start=folder))
    
    print(f"Backup created successfully: {backup_path}")

def main():
    # Define the directories to backup
    source_dirs = [
        '/path/to/your/first_directory',   # Replace with the actual path
        '/path/to/your/second_directory',  # Replace with the actual path
    ]
    
    # Define the backup directory
    backup_dir = '/path/to/your/backup_directory'  # Replace with the actual path
    
    # Create the backup
    create_backup(source_dirs, backup_dir)

if __name__ == "__main__":
    main()
