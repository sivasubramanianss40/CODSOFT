import tkinter as tk
from tkinter import messagebox, ttk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Style configuration
        style = ttk.Style()
        style.configure("TFrame", background="#e0e0e0")
        style.configure("TLabel", background="#e0e0e0", font=("Helvetica", 10))
        style.configure("TButton", font=("Helvetica", 10, "bold"))
        style.configure("TCheckbutton", background="#e0e0e0", font=("Helvetica", 10))
        style.configure("TSpinbox", font=("Helvetica", 10))

        # Main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Initialize variables
        self.length = tk.IntVar(value=12)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)

        # Create GUI components
        ttk.Label(main_frame, text="Password Length:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.length_spinbox = ttk.Spinbox(main_frame, from_=6, to=32, textvariable=self.length, width=5)
        self.length_spinbox.grid(row=0, column=1, pady=5)

        self.uppercase_check = ttk.Checkbutton(main_frame, text="Include Uppercase Letters", variable=self.include_uppercase)
        self.uppercase_check.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=5)
        self.digits_check = ttk.Checkbutton(main_frame, text="Include Digits", variable=self.include_digits)
        self.digits_check.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=5)
        self.special_check = ttk.Checkbutton(main_frame, text="Include Special Characters", variable=self.include_special)
        self.special_check.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.password_entry = ttk.Entry(main_frame, width=40, font=("Helvetica", 10))
        self.password_entry.grid(row=4, column=0, columnspan=2, pady=10)

        self.generate_button = ttk.Button(main_frame, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.length.get()
        include_uppercase = self.include_uppercase.get()
        include_digits = self.include_digits.get()
        include_special = self.include_special.get()

        if length < 6 or length > 32:
            messagebox.showerror("Error", "Password length must be between 6 and 32")
            return

        characters = string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_special:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "No character types selected!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
