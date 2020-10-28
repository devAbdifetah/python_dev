songs = [
     {"title": "happy birthday", "playcount": 1},
     {"title": "survive", "playcount": 9},
     {"title": "YMCA", "playcount": 99},
     {"title": "toxic", "playcount": 31}
]
print(sorted(songs, key=lambda song: song["title"]))
