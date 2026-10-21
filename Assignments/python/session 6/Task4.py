# 4. Simulate an infinite loading spinner in the console by printing 'Loading...' repeatedly using a while True loop. Add a break condition to stop after 3 times.<br><br><em><strong>Hint:</strong> Use a counter variable and break when it reaches 3.

count = 0 

while True:
    print("Loading...")

    count += 1

    if count == 3:
        break