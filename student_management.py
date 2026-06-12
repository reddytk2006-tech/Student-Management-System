students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        students[roll] = name
        print("Student Added Successfully!")

    elif choice == "2":
        for roll, name in students.items():
            print(roll, "-", name)

    elif choice == "3":
        roll = input("Enter Roll Number: ")
        if roll in students:
            print("Student Name:", students[roll])
        else:
            print("Student Not Found")

    elif choice == "4":
        break

    else:
        print("Invalid Choice")
