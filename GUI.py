import tkinter as tk
import pandas as pd
import os

class Student:
    def __init__(self, id, name, department, phone_number, email):
        self.id = id
        self.name = name
        self.department = department
        self.phone_number = phone_number
        self.email = email

def save_data():
    data = []
    for student in arr:
        data.append({
            'Student ID': student.id,
            'Name' : student.name,
            'Department': student.department,
            'Phone Number': student.phone_number,
            'Email': student.email
        })
    df = pd.DataFrame(data)
    df.to_excel('student_data.xlsx', index=False)

def update_excel_file():
    if os.path.exists('student_data.xlsx'):
        os.remove('student_data.xlsx')
    save_data()

def load_data():
    global arr
    if os.path.exists('student_data.xlsx'):
        df = pd.read_excel('student_data.xlsx')
        for index, row in df.iterrows():
            id = row['Student ID']
            name = row['Name']
            department = row['Department']
            phone_number = row['Phone Number']
            email = row['Email']
            arr.append(Student(id, name, department, phone_number, email))

def add_student():
    id = entry_id.get()
    name = entry_name.get()
    department = entry_department.get()
    phone_number = entry_phone.get()
    email_id = entry_email_id.get()
    email_domain = email_var.get()
    
    if not id or not name or not department or not phone_number or not email_id or not email_domain:
        status_label.config(text="Please enter all student information.", fg="red")
        return
    
    if email_domain == "select email":
        status_label.config(text="Email domain must be selected.", fg="red")
        return
    
    if email_domain == "Direct input":
        email_domain = entry_email_domain.get()
    
    email = f"{email_id}@{email_domain}"
    
    arr.append(Student(id, name, department, phone_number, email))
    
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_department.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email_id.delete(0, tk.END)
    email_var.set("select email")
    email_dropdown.configure(state=tk.NORMAL)
    
    save_data()
    status_label.config(text="Student ID added successfully", fg="green")


def delete_student():
    id = entry_id.get()
    
    if not id:
        status_label.config(text="Please enter your student ID.", fg="red")
        return
    
    found = False
    for j in range(len(arr)):
        if arr[j].id == id:
            del arr[j]
            found = True
            break
    
    entry_id.delete(0, tk.END)
    
    if found:
        status_label.config(text="Student ID deleted successfully", fg="green")
        update_excel_file()
    else:
        status_label.config(text="Student ID not found", fg="red")


def search_student():
    search_query = entry_id.get()
    search_query = entry_name.get()
    found_students = []
    
    if not search_query:
        status_label.config(text="Please enter your student ID or name.", fg="red")
        return

    for student in arr:
        if str(student.id) == search_query or student.name.lower() == search_query.lower():
            found_students.append(student)
    
    if found_students:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        
        for student in found_students:
            result_text.insert(tk.END, f"Student ID: {student.id}\n")
            result_text.insert(tk.END, f"Name: {student.name}\n")
            result_text.insert(tk.END, f"Department: {student.department}\n")
            result_text.insert(tk.END, f"Phone Number: {student.phone_number}\n")
            result_text.insert(tk.END, f"Email: {student.email}\n")
            result_text.insert(tk.END, "-" * 30 + "\n")
        
        result_text.config(state=tk.DISABLED)
        status_label.config(text="Your search results have been displayed.", fg="green")
    else:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.config(state=tk.DISABLED)
        status_label.config(text="No results were found for your search.", fg="red")
    
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)

def update_student():
    id = entry_id.get()
    
    if not id:
        status_label.config(text="Please enter your student ID.", fg="red")
        return
    
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
        result_text.insert(tk.END, f"ID: {student.id}, Name: {student.name}, Department: {student.department}, Phone: {student.phone_number}, Email: {student.email}\n")
    result_text.config(state=tk.DISABLED)

def select_email_domain(event):
    selected_domain = email_var.get()
    if selected_domain == "Direct input":
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
    if selected_domain != "Direct input":
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

    label_name = tk.Label(root, text="Name:")
    label_name.grid(row=0, column=2, padx=5, pady=5)

    entry_name = tk.Entry(root)
    entry_name.grid(row=0, column=3, padx=5, pady=5)

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
    email_var.set("select email")
    email_domain_options = [
        "select email",
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
        "Direct input"
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

    result_text = tk.Text(root, height=25, width=100)
    result_text.grid(row=0, column=4, rowspan=9, padx=10, pady=5)

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
