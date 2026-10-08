# 3 .Create a Python program that checks if a person can order food from Zomato late at night: input age and current time (24-hour format). If age is 18 or above and time is between 22 (10pm) and 2 (2am), print 'Order allowed', else print 'Order not allowed'. Use nested if statements.<br><br><em><strong>Hint:</strong> Handle the time range that crosses midnight by checking if time >= 22 or time <= 2.</em>

age = int(input("Enter your age: "))
current_time = int(input("Enter the current hour (0-23): "))

if age >= 18:
    if current_time >= 22 or current_time <= 2:
        print("Order allowed")
    else:
        print("Order not allowed")
else:
    print("Order not allowed")
