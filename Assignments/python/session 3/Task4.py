# 4. Write a script that asks the user for their Instagram follower count, converts it to an integer, and prints the count in a formatted string like 'You have 1,500 followers'. Use escape characters to add a new line and tab before the output.<br><br><em><strong>Hint:</strong> Use '\n' for new line and '\t' for tab in your print statement.</em>

follower_count = int(input("Enter your Instagram follower count: "))
print(f"\n\tYou have {follower_count} followers.")