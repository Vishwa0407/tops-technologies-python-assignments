student = {}

while True:
    print("\n1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for i in range(3):
            key = input("Enter key: ")
            value = input("Enter value: ")
            student[key] = value

        print("All 3 records added successfully!")

    elif choice == 2:
        print(student)

    elif choice == 3:
        key = input("Enter key to update: ")

        if key in student:
            student[key] = input("Enter new value: ")
            print("Updated successfully!")
        else:
            print("Key not found!")

    elif choice == 4:
        key = input("Enter key to delete: ")

        if key in student:
            del student[key]
            print("Deleted successfully!")
        else:
            print("Key not found!")

    elif choice == 5:
        print("Program exited.")
        break

    else:
        print("Invalid choice!")