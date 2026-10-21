'''
2. create a Python program using while True where the user gets 3 options:
        1. Add a number to the list.
        2. Update an existing number in the list.
        3. Delete a number from the list.
'''

numbers = []

while True:
    print("\n1. Add")
    print("2. Update")
    print("3. Delete")
    print("4. Display List")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter number to add: "))
        numbers.append(num)
        print("Number added successfully!")

    elif choice == 2:
        old_num = int(input("Enter number to update: "))

        if old_num in numbers:
            new_num = int(input("Enter new number: "))
            index = numbers.index(old_num)
            numbers[index] = new_num
            print("Number updated successfully!")
        else:
            print("Number not found!")

    elif choice == 3:
        num = int(input("Enter number to delete: "))

        if num in numbers:
            numbers.remove(num)
            print("Number deleted successfully!")
        else:
            print("Number not found!")

    elif choice == 4:
        print("Your list:", numbers)

    elif choice == 5:
        print("Program stopped.")
        break

    else:
        print("Invalid choice! Please try again.")