# 3. Build a small snippet that creates three variables representing a Spotify playlist: playlist_title, number_of_songs, and is_public. Use the id() function to print the memory address of each variable.

playlist_title = "Workout Hits"
number_of_songs = 30
is_public = True

# Printing the memory address of each variable using the id() function

print("Playlist Title:", playlist_title, "Memory Address:", id(playlist_title))
print("Number of Songs:", number_of_songs, "Memory Address:", id(number_of_songs))
print("Is Public:", is_public, "Memory Address:", id(is_public))