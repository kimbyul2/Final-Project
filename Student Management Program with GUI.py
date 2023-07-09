import tkinter as tk

class Student:
    def __init__(self, id):
        self.id = id

def add_student():
    id = int(entry_id.get())
    arr.append(Student(id))



root = tk.Tk()
root.title("Student ID Manager")

label_id = tk.Label(root, text="Student ID:")
label_id.grid(row=0, column=0, padx=5, pady=5)

entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=5, pady=5)

label_department = tk.Label(root, text="Department:")
label_department.grid(row=1, column=0, padx=5, pady=5)

entry_department = tk.Entry(root)
entry_department.grid(row=1, column=1, padx=5, pady=5)

label_new_id = tk.Label(root, text="New ID:")
label_new_id.grid(row=2, column=0, padx=5, pady=5)

entry_new_id = tk.Entry(root)
entry_new_id.grid(row=2, column=1, padx=5, pady=5)

button_add = tk.Button(root, text="Add Student ID", command=add_student)
button_add.grid(row=3, column=0, padx=5, pady=5)


arr = []

root.mainloop()
