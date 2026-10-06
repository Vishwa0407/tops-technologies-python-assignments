# 3. Build a Zomato-style bill calculator: take the price of a food item and quantity as input, convert them to float and int, calculate the total bill, and display it with a message like 'Your total bill is ₹350.50'.

price = float(input("Enter the price of the food item: ₹"))
quantity = int(input("Enter the quantity of the food item: "))

total_bill = price * quantity

print(f"Your total bill is ₹{total_bill:.2f}.")