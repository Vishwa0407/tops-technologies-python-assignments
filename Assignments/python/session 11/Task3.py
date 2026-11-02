# 3. Write a function display_friends() that takes a dictionary of Instagram usernames as keys and their follower counts as values, and prints each username with their followers in the format: 'username: 2.3K followers'.

def display_friends(friends):
    for username, followers in friends.items():
        if followers >= 1000:
            print(f"{username}: {followers / 1000:.1f}K followers")
        else:
            print(f"{username}: {followers} followers")


instagram_friends = {
    "Alice": 2300,
    "Bob": 1500,
    "John": 850,
    "Katty": 3200
}

display_friends(instagram_friends)