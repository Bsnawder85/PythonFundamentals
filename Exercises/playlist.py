

playlist = {
    'title': 'Patagonia Bus',
    'author': 'whoever',
    # songs:  title, artist, album, duration
    'songs': [
        {'title':'song1', 'artist': ['blue'], 'duration': '02:35'},
        {'title':'meowmeow (the remix, the meow-mix, the meow-remix)', 'artist': ['kitty', 'djcat'], 'duration': '07:3o'},
        {'title':'lasagna', 'artist': ['garfield'], 'duration': '05:35'}
    ]
}
# the order in which the songs will be played is determined by the order they appear in the 'songs' list.



for song in playlist['songs']:
    print(song['title'])


