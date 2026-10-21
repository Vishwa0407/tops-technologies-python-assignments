# 4. Given a dictionary called food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}, use the keys(), values(), and items() methods to print: a) all food items, b) all quantities, and c) each item with its quantity.

food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}

# Print all food items
print("Food items:", food_order.keys())

# Print all quantities
print("Quantities:", food_order.values())

# Print each item with its quantity
print("Items with quantities:")
for item, quantity in food_order.items():
    print(item, ":", quantity)