import tkinter as tk
import pandas as pd

class Student:
    def __init__(self, id, department, phone_number, email):
        self.id = id
        self.department = department
        self.phone_number = phone_number
        self.email = email

def save_data():
    data = []
    for student in arr:
        data.append({
            'Student ID': student.id,
            'Department': student.department,
            'Phone Number': student.phone_number,
            'Email': student.email
        })
    df = pd.DataFrame(data)
    df.to_excel('student_data.xlsx', index=False)

def load_data():
    try:
        df = pd.read_excel('student_data.xlsx')
        for _, row in df.iterrows():
            id = row['Student ID']
            department = row['Department']
            phone_number = row['Phone Number']
            email = row['Email']
            arr.append(Student(id, department, phone_number, email))
    except pd.errors.EmptyDataError:
        pass

def add_student():
    id = int(entry_id.get())
    department = entry_department.get()
    phone_number = entry_phone.get()
    email_id = entry_email_id.get()
    email_domain = email_var.get()
    if email_domain == "직접입력":
        email_domain = entry_email_domain.get()
    email = f"{email_id}@{email_domain}"
    arr.append(Student(id, department, phone_number, email))
    entry_id.delete(0, tk.END)
    entry_department.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email_id.delete(0, tk.END)
    email_var.set("이메일선택")
    email_dropdown.configure(state=tk.NORMAL)
    save_data()

def delete_student():
    id = int(entry_id.get())
    found = False
    for j in range(len(arr)):
        if arr[j].id == id:
            del arr[j]
            found = True
            break
    entry_id.delete(0, tk.END)
    if found:
        status_label.config(text="Student ID deleted successfully", fg="green")
    else:
        status_label.config(text="Student ID not found", fg="red")


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
    found = False
    for j in range(len(arr)):
        if arr[j].id == id:
            result_text.set("Student ID updated")
            found = True
            break
    if not found:
        result_text.set("Student ID not found")
    entry_id.delete(0, tk.END)

def display_students():
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Student IDs:\n")
    for student in arr:
        result_text.insert(tk.END, f"ID: {student.id}, Department: {student.department}, Phone: {student.phone_number}, Email: {student.email}\n")
    result_text.config(state=tk.DISABLED)

def select_email_domain(event):
    selected_domain = email_var.get()
    if selected_domain == "직접입력":
        if not hasattr(root, 'entry_email_domain'):
            global entry_email_domain
            entry_email_domain = tk.Entry(root)
            entry_email_domain.grid(row=4, column=3, padx=5, pady=5, sticky='w')
    else:
        if hasattr(root, 'entry_email_domain'):
            entry_email_domain.grid_forget()
            entry_email_domain.delete(0, tk.END)
    if entry_email_id['state'] == tk.NORMAL:
        entry_email_id.focus_set()
    if selected_domain != "직접입력":
        entry_email_domain.configure(state=tk.DISABLED)
    else:
        entry_email_domain.configure(state=tk.NORMAL)

def main():
    load_data()
    root.mainloop()

if __name__ == "__main__":
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

    label_email = tk.Label(root, text="Email:")
    label_email.grid(row=3, column=0, padx=5, pady=5)

    entry_email_id = tk.Entry(root)
    entry_email_id.grid(row=3, column=1, padx=5, pady=5)

    entry_email_domain = tk.Entry(root)
    entry_email_domain.grid(row=3, column=4, padx=5, pady=5)
    entry_email_domain.configure(state=tk.DISABLED)

    email_var = tk.StringVar(root)
    email_var.set("이메일선택")
    email_domain_options = [
        "이메일선택",
        "naver.com",
        "hanmail.net",
        "hotmail.com",
        "nate.com",
        "hufs.ac.kr",
        "yahoo.co.kr",
        "daum.com",
        "paran.com",
        "hanafos.com",
        "empal.com",
        "gmail.com",
        "korea.com",
        "hanmir.com",
        "직접입력"
    ]
    email_dropdown = tk.OptionMenu(root, email_var, *email_domain_options, command=select_email_domain)
    email_dropdown.grid(row=3, column=3, padx=5, pady=5)

    label_at = tk.Label(root, text="@")
    label_at.grid(row=3, column=2, padx=5, pady=5)

    button_add = tk.Button(root, text="Add Student ID", command=add_student)
    button_add.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

    button_delete = tk.Button(root, text="Delete Student ID", command=delete_student)
    button_delete.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

    button_search = tk.Button(root, text="Search Student ID", command=search_student)
    button_search.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

    button_update = tk.Button(root, text="Update Student ID", command=update_student)
    button_update.grid(row=8, column=0, columnspan=4, padx=5, pady=5)

    button_display = tk.Button(root, text="Display Student IDs", command=display_students)
    button_display.grid(row=9, column=0, columnspan=4, padx=5, pady=5)

    result_text = tk.Text(root, height=25, width=50)
    result_text.grid(row=0, column=4, rowspan=9, padx=12, pady=5)

    status_label = tk.Label(root, text="", fg="red")
    status_label.grid(row=9, column=4, columnspan=4, padx=5, pady=5)

    scrollbar = tk.Scrollbar(root)
    scrollbar.grid(row=0, column=5, rowspan=9, padx=0, pady=5, sticky="ns")
    result_text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=result_text.yview)

    button_exit = tk.Button(root, text="Exit", command=root.destroy)
    button_exit.grid(row=10, column=0, columnspan=4, padx=5, pady=5)

    arr = []

    root.protocol("WM_DELETE_WINDOW", save_data)
    main()
