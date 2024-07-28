import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a password
def generate_password():
    length = entry.get()
    if not length.isdigit():
        messagebox.showerror("Invalid input", "Please enter a valid number for the password length.")
        return

    length = int(length)

    if length < 1:
        messagebox.showerror("Invalid length", "Password length must be greater than 0.")
        return

    # Define character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for i in range(length))

    # Display the generated password
    result_label.config(text=f"Generated Password: {password}")

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Create an entry widget to input the password length
tk.Label(root, text="Enter Password Length:").pack(pady=10)
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display the generated password
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()
