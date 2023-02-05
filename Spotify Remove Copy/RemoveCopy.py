import pandas as pd
from pathlib import Path

data_frame = pd.read_excel("SpotifySongsList.xlsx", usecols=[2, 3])

def toTuple(name):
    i = 1
    artist, song = '', ''
    name_length = len(name)

    while i < name_length and name[i] != ',' and name[i] != ']':
        artist += name[i]
        i += 1
    
    i += 2
    while i < name_length and name[i] != '(' and name[i] != '[':
        song += name[i]
        i +=1
    
    if song.endswith(".mp3"):
        song = song[:len(song)-4]
    
    if song.endswith(" "):
        song = song[:len(song)-1]

    return (song, artist)

base_path = Path("C:\\Users\\user\\Music\\Songs")
names = (entry.name for entry in base_path.iterdir() if (entry.is_file() and entry.name.endswith(".mp3")))

i = 0
for name in names:
    song, artist = toTuple(name)
    print(f"Song: {song}, Artist: {artist}")
    if i > 5:
        break
    i += 1
