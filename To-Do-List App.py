from tkinter import *
from tkinter import messagebox as m_box
from tkinter import ttk
import time

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry('800x500+300+150')

        self.setup_ui()

    def setup_ui(self):
        self.label = Label(self.root, text='To - Do - List - App', font='Arial 25 bold', bd=10, bg='#00215e', fg='white')
        self.label.pack(side='top', fill=X)

        self.frame_left = Frame(self.root, bd=10, bg='black')
        self.frame_left.pack(side='left', fill=Y)

        self.label2 = Label(self.frame_left, text='Add Tasks', font='Arial 15 bold', bd=10, bg='blue', fg='white')
        self.label2.pack(side='top', fill=X)

        self.text = Text(self.frame_left, bd=5, height=2, width=30, font='Arial 10 bold')
        self.text.pack(side='top', pady=(10, 0))

        self.add_button = Button(self.frame_left, text='Add', font='Arial 12 bold', width=8, bd=5, bg='blue', fg='black', command=self.add_task)
        self.add_button.pack(side='top', pady=(10, 0))

        self.delete_button = Button(self.frame_left, text='Delete', font='Arial 12 bold', width=8, bd=5, bg='blue', fg='black', command=self.delete_task)
        self.delete_button.pack(side='top', pady=(10, 0))

        self.delete_all_button = Button(self.frame_left, text='Delete All', font='Arial 12 bold', width=8, bd=5, bg='blue', fg='black', command=self.delete_all_tasks)
        self.delete_all_button.pack(side='top', pady=(10, 0))

        self.frame_right = Frame(self.root, bd=10, bg='blue')
        self.frame_right.pack(side='left', expand=True, fill=BOTH)

        self.label3 = Label(self.frame_right, text='Your Tasks ', font='Arial 15 bold', bd=10, bg='blue', fg='white')
        self.label3.pack(side='top', fill=X)

        self.task_listbox = Listbox(self.frame_right, bd=10, font='Arial 15 italic bold', selectmode=SINGLE)
        self.task_listbox.pack(side='left', expand=True, fill=BOTH, pady=(10, 0))

        self.scrollbar = Scrollbar(self.frame_right, orient=VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # Bind double click event to set reminder
        self.task_listbox.bind('<Double-1>', self.set_reminder)

        # Load existing tasks from file
        self.load_tasks()

    def add_task(self):
        content = self.text.get(1.0, END).strip()
        
        if content:
            self.task_listbox.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content + '\n')
            self.text.delete(1.0, END)
        else:
            m_box.showerror('Error', 'Please enter a task.')

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_index)
            confirm = m_box.askyesno('Confirm Deletion', f'Are you sure you want to delete "{selected_task}"?')
            if confirm:
                self.task_listbox.delete(selected_index)
                self.save_tasks()
        except IndexError:
            m_box.showerror('Error', 'Please select a task to delete.')

    def delete_all_tasks(self):
        if self.task_listbox.size() == 0:
            m_box.showwarning('No Tasks', 'There are no tasks to delete.')
        else:
            confirm = m_box.askyesno('Confirm Deletion', 'Are you sure you want to delete all tasks?')
            if confirm:
                self.task_listbox.delete(0, END)  # Clear the Listbox
                with open('data.txt', 'w') as file:
                    file.truncate(0)  # Clear the data file

    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    self.task_listbox.insert(END, line.strip())
        except FileNotFoundError:
            m_box.showwarning('File Not Found', 'No previous tasks found.')

    def save_tasks(self):
        with open('data.txt', 'w') as file:
            tasks = self.task_listbox.get(0, END)
            for task in tasks:
                file.write(task + '\n')

    def set_reminder(self, event):
        try:
            selected_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_index)
            m_box.showinfo('Reminder Set', f'Reminder set for: {selected_task}')
            self.root.after(60000, lambda: self.reminder_notification(selected_task))  # Reminder after 1 minute (60000 milliseconds)
        except IndexError:
            pass

    def reminder_notification(self, task):
        m_box.showinfo('Reminder', f"Don't forget to complete: {task}")

def main():
    root = Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    