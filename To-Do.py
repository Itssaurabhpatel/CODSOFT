import tkinter as tk
from tkinter import messagebox

tasks = []

def display_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        entry.delete(0, tk.END)
        display_tasks()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def update_task():
    try:
        selected_task_index = listbox.curselection()[0]
        new_task = entry.get()
        if new_task:
            tasks[selected_task_index] = new_task
            entry.delete(0, tk.END)
            display_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a new task.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks.pop(selected_task_index)
        display_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Update Task", command=update_task)
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

display_tasks()

root.mainloop()
    
