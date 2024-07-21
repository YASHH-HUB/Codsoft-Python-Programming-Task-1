import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced To-Do List")
        self.tasks = []
        self.create_gui()

    def create_gui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Task list frame
        list_frame = tk.Frame(main_frame, bg='#ffffff', bd=2, relief=tk.SUNKEN)
        list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.task_listbox = tk.Listbox(list_frame, width=50, height=15, font=("Helvetica", 12),
                                       selectbackground='#a6a6a6', selectforeground='#ffffff')
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Entry frame
        entry_frame = tk.Frame(main_frame, bg='#f0f0f0')
        entry_frame.pack(pady=10, fill=tk.X)

        self.task_entry = tk.Entry(entry_frame, width=40, font=("Helvetica", 12))
        self.task_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

        add_button = tk.Button(entry_frame, text="Add Task", command=self.add_task,
                               bg='#4CAF50', fg='white', font=("Helvetica", 10, "bold"))
        add_button.pack(side=tk.LEFT, padx=5)

        # Button frame
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(pady=10)

        update_button = tk.Button(button_frame, text="Update Task", command=self.update_task,
                                  bg='#2196F3', fg='white', font=("Helvetica", 10, "bold"))
        update_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task,
                                  bg='#f44336', fg='white', font=("Helvetica", 10, "bold"))
        delete_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            current_task = self.tasks[selected_index]
            new_task = simpledialog.askstring("Update Task", "Edit the task:",
                                              initialvalue=current_task)
            if new_task and new_task.strip() != current_task:
                self.tasks[selected_index] = new_task.strip()
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{task}'?"):
                del self.tasks[selected_index]
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{index}. {task}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    todo_app = TodoApp(root)
    root.mainloop()