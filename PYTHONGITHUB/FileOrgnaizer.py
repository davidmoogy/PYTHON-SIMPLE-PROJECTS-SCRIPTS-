import os
import shutil

# Define the directory to organize
source_dir = 'path/to/your/directory'

# Define subfolder names for different file types
folders = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar'],
}

# Create subfolders if they don't exist
def create_folders():
    for folder in folders.keys():
        folder_path = os.path.join(source_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Move files to their corresponding folders
def organize_files():
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, extensions in folders.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(source_dir, folder)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"Moved: {filename} -> {folder}")
                    moved = True
                    break
            if not moved:
                print(f"Unsorted file: {filename}")

if __name__ == "__main__":
    create_folders()
    organize_files()
    print("File organization complete.")
