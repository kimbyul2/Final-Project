class Student:
    def __init__(self, id):
        self.id = id

arr = []

while True:
    print("1. Add Student ID")
    print("2. Delete Student ID")
    print("3. Insert Student ID at a given position or index")
    print("4. Search Student ID")
    print("5. Update Student ID")
    print("6. Display Student IDs")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

   

    if choice == 6:  # Display Student IDs
        print("Student IDs:")
        for student in arr:
            print(student.id)

    elif choice == 7:  # Exit
        print("The programming is over.")
        break

    else:
        print("Invalid option. Please choose a valid option.")