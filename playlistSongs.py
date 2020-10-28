playList = {
     'title':'patagonia bud',
     'author':'colt steele',
     'songs': [
          {'title': 'song1', 'artist':['blue'], 'duration':3},
          {'title': 'song2', 'artist':['ketty','djcat'], 'duration':3.5},
          {'title': 'meowmeow', 'artist':['garield'], 'duration':2.0}
     ]     
}

##for song in playList['songs']:
##      print(song)

total_length = 0
for song in playList['songs']:
     total_length+=song['duration']
print(total_length)     
