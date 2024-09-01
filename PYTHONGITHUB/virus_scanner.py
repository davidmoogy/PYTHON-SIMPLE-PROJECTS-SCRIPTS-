import os
import hashlib

# Define known malicious file hashes (example hashes)
MALICIOUS_HASHES = {
    "e99a18c428cb38d5f260853678922e03",  # Example MD5 hash
    "5baa61e4c9b93f3f0682250b6cf8331b"   # Example MD5 hash
}

def calculate_file_hash(file_path):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except IOError:
        return None
    return hash_md5.hexdigest()

def scan_directory(directory):
    """Scan all files in the specified directory and its subdirectories."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)
            if file_hash and file_hash in MALICIOUS_HASHES:
                print(f"Malicious file detected: {file_path}")

def main():
    """Main function to start the scan."""
    # Get directory path from user
    path_to_scan = input("Enter the path to scan (e.g., C:\\\\, D:\\\\myfolder): ").strip()
    
    if not os.path.isdir(path_to_scan):
        print(f"Error: The path '{path_to_scan}' is not a valid directory.")
        return

    print("Starting the scan...")
    scan_directory(path_to_scan)
    print("Scan complete.")

if __name__ == "__main__":
    main()
