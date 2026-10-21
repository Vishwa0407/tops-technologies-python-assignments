# 2. Create a loop that goes through the following list: ['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Burger King'], and breaks the loop when it finds 'Burger King', printing 'Found Burger King, stopping search.'

foods = ['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Burger King']

for food in foods:
    if food == "Burger King":
        print("Found Burger King, stopping search")
        break
    print(food)