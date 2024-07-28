import tkinter as tk
from tkinter import ttk

# Function to evaluate the expression in the entry widget
def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to append a character to the entry widget
def append_to_entry(character):
    entry.insert(tk.END, character)

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Stylish Calculator")
root.geometry("350x450")
root.resizable(0, 0)
root.configure(bg='#ffffff')

# Create an entry widget for input and output
entry = ttk.Entry(root, font=("Arial", 24), justify=tk.RIGHT)
entry.pack(pady=20, padx=10, fill=tk.X)

# Define style
style = ttk.Style()
style.configure('TButton', font=("Arial", 18), padding=10)
style.configure('TEntry', font=("Arial", 24))

# Create a frame to hold the buttons
button_frame = ttk.Frame(root, padding=10)
button_frame.pack()

# Define button labels and their respective row and column positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4)
]

# Create and place buttons in the frame
for (text, row, col, *span) in buttons:
    colspan = span[0] if span else 1
    if text == '=':
        button = ttk.Button(button_frame, text=text, style='TButton', command=evaluate_expression)
    elif text == 'C':
        button = ttk.Button(button_frame, text=text, style='TButton', command=clear_entry)
    else:
        button = ttk.Button(button_frame, text=text, style='TButton', command=lambda t=text: append_to_entry(t))
    button.grid(row=row, column=col, columnspan=colspan, sticky='nsew', padx=5, pady=5)

# Adjust column and row weights for equal sizing
for i in range(4):
    button_frame.columnconfigure(i, weight=1)
for i in range(5):
    button_frame.rowconfigure(i, weight=1)

# Start the main event loop
root.mainloop()
