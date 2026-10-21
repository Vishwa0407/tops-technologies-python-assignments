my_set = set()

while True:
    print("\n--- SET CRUD MENU ---")
    print("1. Add Item")
    print("2. Display Set")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        my_set.add(item)
        print("Item added successfully!")

    elif choice == 2:
        print("Your Set:", my_set)

    elif choice == 3:
        old_item = input("Enter item to update: ")

        if old_item in my_set:
            new_item = input("Enter new item: ")

            my_set.remove(old_item)
            my_set.add(new_item)

            print("Item updated successfully!")
        else:
            print("Item not found!")

    elif choice == 4:
        item = input("Enter item to delete: ")

        if item in my_set:
            my_set.remove(item)
            print("Item deleted successfully!")
        else:
            print("Item not found!")

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
