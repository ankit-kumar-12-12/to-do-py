import tkinter as tk
from tkinter import messagebox

# File to store tasks
TASKS_FILE = "tasks.txt"

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create a listbox to display tasks
task_list = tk.Listbox(window, width=50, height=10)
task_list.pack(pady=20)

# Function to add a new task
def add_task():
    task = entry_task.get().strip()
    if task:  # Check if a task was entered
        task_list.insert(tk.END, task)
        save_tasks()
        entry_task.delete(0, tk.END)  # Clear the entry field
    else:
        tk.messagebox.showwarning("Warning", "Please enter a task")

# Function to delete the selected task
def delete_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:  # Check if a task is selected
        task_list.delete(selected_task_index)
        save_tasks()

# Function to save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        tasks = task_list.get(0, tk.END)
        file.write("\n".join(tasks))

# Function to load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            for task in file:
                task_list.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

# Create entry for new tasks and buttons
entry_task = tk.Entry(window, width=40)
entry_task.pack()

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=10)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

# Load tasks when the application starts
load_tasks()

# Run the main loop
window.mainloop()
