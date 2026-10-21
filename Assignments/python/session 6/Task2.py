# 2. Build a simple Zomato-style offer countdown: start with a variable 'minutes_left' set to 5, and use a while loop to print 'Offer ends in X minutes' until it reaches 0.

minutes_left = 5

while minutes_left > 0:
    print(f"Offer ends in {minutes_left} minutes")
    minutes_left -= 1

print("Offer has ended!")