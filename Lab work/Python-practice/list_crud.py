my_list = []

while True:
    print("\n--- LIST CRUD MENU ---")
    print("1. Add Item")
    print("2. Display List")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        my_list.append(item)
        print("Item added successfully!")

    elif choice == 2:
        print("Your List : ",my_list)

    elif choice == 3:
        old_item = input("Enter item to update: ")

        if old_item in my_list:
            new_item = input("Enter new item: ")
            index = my_list.index(old_item)
            my_list[index] = new_item
            print("Item updated successfully!")
        else:
            print("Item not found!")

    elif choice == 4:
        item = input("Enter item to delete: ")

        if item in my_list:
            my_list.remove(item)
            print("Item deleted successfully!")
        else:
            print("Item not found!")

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")