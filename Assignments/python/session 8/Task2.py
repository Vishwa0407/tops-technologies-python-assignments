#2. Write a function extract_artist(song_title) that takes a string in the format 'Song Name - Artist Name' (like you see on Spotify) and returns just the artist's name using string slicing.<br><br><em><strong>Hint:</strong> Use the index() method to find the position of the dash.</em>

def extract_artist(song_title):
    dash_index = song_title.index("-")
    artist = song_title[dash_index + 1:].strip()
    print(artist)

song = "Perfect - Ed Sheeran"
extract_artist(song)