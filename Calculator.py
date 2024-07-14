import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def on_button_click(event):
    button_text = event.widget.cget("text")
    
    if button_text == "=":
        try:
            expression = entry.get()
            # Evaluate the expression and display the result
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            entry.delete(0, tk.END)
        except SyntaxError:
            messagebox.showerror("Error", "Enter a valid calculation")
            entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
            entry.delete(0, tk.END)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Function to create buttons with improved UI
def create_button(parent, text, row, col, rowspan=1, colspan=1, bg_color="#4A90E2", fg_color="white"):
    button = tk.Button(parent, text=text, font=("Arial", 16), bg=bg_color, fg=fg_color, borderwidth=0, padx=20, pady=20)
    button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew", padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)

# Creating main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500+710+60")
root.configure(bg="#1C3A6D")

# Creating entry widget for input
entry = tk.Entry(root, font=("Arial", 24), bg="#7BAFD4", fg="black", bd=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Defining button layout and colors
buttons = [
    ("7", 1, 0, "#4A90E2"), ("8", 1, 1, "#4A90E2"), ("9", 1, 2, "#4A90E2"), ("/", 1, 3, "#FF9500"),
    ("4", 2, 0, "#4A90E2"), ("5", 2, 1, "#4A90E2"), ("6", 2, 2, "#4A90E2"), ("*", 2, 3, "#FF9500"),
    ("1", 3, 0, "#4A90E2"), ("2", 3, 1, "#4A90E2"), ("3", 3, 2, "#4A90E2"), ("-", 3, 3, "#FF9500"),
    ("C", 4, 0, "#FF3B30"), ("0", 4, 1, "#4A90E2"), ("=", 4, 2, "#34C759"), ("+", 4, 3, "#FF9500"),
]

# Creating buttons with improved UI
for (text, row, col, color) in buttons:
    create_button(root, text, row, col, bg_color=color)

# Configuring row and column weights for responsive design
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Running the main event loop
root.mainloop()
