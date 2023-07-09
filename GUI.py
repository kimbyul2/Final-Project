import tkinter as tk
import pandas as pd

class Student:
    def __init__(self, id, department, phone_number):
        self.id = id
        self.department = department
        self.phone_number = phone_number

def save_data():
    data = []
    for student in arr:
        data.append({
            'Student ID': student.id,
            'Department': student.department,
            'Phone Number': student.phone_number
        })
    df = pd.DataFrame(data)
    df.to_excel('student_data.xlsx', index=False)

def add_student():
    id = int(entry_id.get())
    department = entry_department.get()
    phone_number = entry_phone.get()
    arr.append(Student(id, department, phone_number))
    entry_id.delete(0, tk.END)
    entry_department.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    save_data()

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
    department = entry_department.get()
    phone_number = entry_phone.get()
    position = int(entry_position.get())
    if position >= 0 and position <= len(arr):
        arr.insert(position, Student(id, department, phone_number))
        result_text.set("Student ID inserted")
    else:
        result_text.set("Invalid position")
    entry_id.delete(0, tk.END)
    entry_department.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_position.delete(0, tk.END)

def search_student():
    id = int(entry_id.get())
    found = False
    for j in range(len(arr)):
        if arr[j].id == id:
            result_text.set(f"Student ID found at position {j}")
            found = True
            break
    if not found:
        result_text.set("Student ID not found")
    entry_id.delete(0, tk.END)

def update_student():
    id = int(entry_id.get())
    new_id = int(entry_new_id.get())
    found = False
    for j in range(len(arr)):
        if arr[j].id == id:
            arr[j].id = new_id
            result_text.set("Student ID updated")
            found = True
            break
    if not found:
        result_text.set("Student ID not found")
    entry_id.delete(0, tk.END)
    entry_new_id.delete(0, tk.END)

def display_students():
    result_text.set("Student IDs:\n" + "\n".join(f"ID: {student.id}, Department: {student.department}, Phone: {student.phone_number}" for student in arr))

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

label_phone = tk.Label(root, text="Phone Number:")
label_phone.grid(row=2, column=0, padx=5, pady=5)

entry_phone = tk.Entry(root)
entry_phone.grid(row=2, column=1, padx=5, pady=5)

label_position = tk.Label(root, text="Position:")
label_position.grid(row=3, column=0, padx=5, pady=5)

entry_position = tk.Entry(root)
entry_position.grid(row=3, column=1, padx=5, pady=5)

label_new_id = tk.Label(root, text="New ID:")
label_new_id.grid(row=4, column=0, padx=5, pady=5)

entry_new_id = tk.Entry(root)
entry_new_id.grid(row=4, column=1, padx=5, pady=5)

button_add = tk.Button(root, text="Add Student ID", command=add_student)
button_add.grid(row=5, column=0, padx=5, pady=5)

button_delete = tk.Button(root, text="Delete Student ID", command=delete_student)
button_delete.grid(row=5, column=1, padx=5, pady=5)

button_insert = tk.Button(root, text="Insert Student ID", command=insert_student)
button_insert.grid(row=6, column=0, padx=5, pady=5)

button_search = tk.Button(root, text="Search Student ID", command=search_student)
button_search.grid(row=6, column=1, padx=5, pady=5)

button_update = tk.Button(root, text="Update Student ID", command=update_student)
button_update.grid(row=7, column=0, padx=5, pady=5)

button_display = tk.Button(root, text="Display Student IDs", command=display_students)
button_display.grid(row=7, column=1, padx=5, pady=5)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

button_exit = tk.Button(root, text="Exit", command=root.destroy)
button_exit.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

arr = []

root.mainloop()
