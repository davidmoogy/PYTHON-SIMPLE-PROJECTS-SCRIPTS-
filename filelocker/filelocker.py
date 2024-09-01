import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import shutil

class FileLockerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Locker")
        self.root.geometry("400x300")
        
        # Load and display the logo
        self.logo_image = Image.open("logo.png")
        self.logo_image = self.logo_image.resize((100, 100), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(root, image=self.logo)
        self.logo_label.pack(pady=10)

        # Create and pack widgets
        self.lock_button = tk.Button(root, text="Lock File", command=self.lock_file)
        self.lock_button.pack(pady=10)

        self.unlock_button = tk.Button(root, text="Unlock File", command=self.unlock_file)
        self.unlock_button.pack(pady=10)

        self.locked_files_dir = "locked_files"
        if not os.path.exists(self.locked_files_dir):
            os.makedirs(self.locked_files_dir)

    def lock_file(self):
        file_path = filedialog.askopenfilename(title="Select a file to lock")
        if file_path:
            file_name = os.path.basename(file_path)
            locked_file_path = os.path.join(self.locked_files_dir, file_name)
            try:
                shutil.move(file_path, locked_file_path)
                messagebox.showinfo("Success", f"File '{file_name}' locked successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to lock file: {e}")

    def unlock_file(self):
        file_name = filedialog.askopenfilename(initialdir=self.locked_files_dir, title="Select a file to unlock")
        if file_name:
            file_name = os.path.basename(file_name)
            locked_file_path = os.path.join(self.locked_files_dir, file_name)
            original_file_path = filedialog.asksaveasfilename(defaultextension=".*", title="Save unlocked file as")
            if original_file_path:
                try:
                    shutil.move(locked_file_path, original_file_path)
                    messagebox.showinfo("Success", f"File '{file_name}' unlocked successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to unlock file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileLockerApp(root)
    root.mainloop()
