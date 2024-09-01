import tkinter as tk
from tkinter import messagebox
import json
import os

class PasswordManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("400x400")
        self.root.configure(bg='#2E2E2E')
        
        self.data_file = "passwords.json"
        self.load_data()

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Password Manager", font=("Helvetica", 16, "bold"), fg="#FFFFFF", bg="#2E2E2E")
        self.title_label.pack(pady=20)

        # Create a frame for the input fields and buttons
        self.input_frame = tk.Frame(self.root, bg="#2E2E2E")
        self.input_frame.pack(pady=10, padx=20, fill=tk.X)

        # Website Name
        self.website_label = tk.Label(self.input_frame, text="Website:", font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E")
        self.website_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.website_entry = tk.Entry(self.input_frame, font=("Helvetica", 12))
        self.website_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

        # Username
        self.username_label = tk.Label(self.input_frame, text="Username:", font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E")
        self.username_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.username_entry = tk.Entry(self.input_frame, font=("Helvetica", 12))
        self.username_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

        # Password
        self.password_label = tk.Label(self.input_frame, text="Password:", font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E")
        self.password_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.password_entry = tk.Entry(self.input_frame, show='*', font=("Helvetica", 12))
        self.password_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

        # Add Button
        self.add_button = tk.Button(self.root, text="Add Password", command=self.add_password, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="#FFFFFF")
        self.add_button.pack(pady=5)

        # View Button
        self.view_button = tk.Button(self.root, text="View Passwords", command=self.view_passwords, font=("Helvetica", 12, "bold"), bg="#2196F3", fg="#FFFFFF")
        self.view_button.pack(pady=5)

        # Delete Button
        self.delete_button = tk.Button(self.root, text="Delete Password", command=self.delete_password, font=("Helvetica", 12, "bold"), bg="#F44336", fg="#FFFFFF")
        self.delete_button.pack(pady=5)

    def add_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not website or not username or not password:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return

        self.passwords[website] = {"username": username, "password": password}
        self.save_data()
        messagebox.showinfo("Success", f"Password for {website} added successfully!")

    def view_passwords(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Passwords")
        view_window.geometry("300x300")
        view_window.configure(bg='#2E2E2E')

        for i, (website, data) in enumerate(self.passwords.items()):
            tk.Label(view_window, text=f"Website: {website}", font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E").pack(pady=5)
            tk.Label(view_window, text=f"Username: {data['username']}", font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E").pack(pady=5)
            tk.Label(view_window, text=f"Password: {data['password']}", font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E").pack(pady=5)

    def delete_password(self):
        website = self.website_entry.get()

        if website in self.passwords:
            del self.passwords[website]
            self.save_data()
            messagebox.showinfo("Success", f"Password for {website} deleted successfully!")
        else:
            messagebox.showwarning("Not Found", "No password found for this website")

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                self.passwords = json.load(file)
        else:
            self.passwords = {}

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.passwords, file)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()
