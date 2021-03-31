def tracklist(**artists):
    for artist in artists:
        print(artist)
        for album in artists[artist]:
            print(f'ALBUM: {album} TRACK: {artists[artist][album]}')
