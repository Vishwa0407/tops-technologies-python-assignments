# 3. Write a Python for loop that checks a list of playlists: ['Chill Vibes', 'Workout', 'Focus', 'Party'], and uses the pass statement when the playlist is 'Focus', but prints all other playlist names.

playlists =  ['Chill Vibes', 'Workout', 'Focus', 'Party']

for playlist in playlists:
    if playlist == "Focus":
        pass
    else:
        print(playlist)