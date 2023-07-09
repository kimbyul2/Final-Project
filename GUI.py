import tkinter as tk

class Student:
    def __init__(self, id):
        self.id = id

def add_student():
    id = int(entry_id.get())
    arr.append(Student(id))

def delete_student():
    id = int(entry_id.get())
    found = False
    for j in range(len(arr)):
        if arr[j].id == id:
            del arr[j]
            found = True
            break
    if found:
        result_text.set("Student ID deleted")
    else:
        result_text.set("Student ID not found")
    entry_id.delete(0, tk.END)

def insert_student():
    id = int(entry_id.get())
    position = int(entry_position.get())
    if position >= 0 and position <= len(arr):
        arr.insert(position, Student(id))
        result_text.set("Student ID inserted")
    else:
        result_text.set("Invalid position")
    entry_id.delete(0, tk.END)
    entry_position.delete(0, tk.END)



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

button_delete = tk.Button(root, text="Delete Student ID", command=delete_student)
button_delete.grid(row=3, column=1, padx=5, pady=5)

button_insert = tk.Button(root, text="Insert Student ID", command=insert_student)
button_insert.grid(row=4, column=0, padx=5, pady=5)

arr = []

root.mainloop()

