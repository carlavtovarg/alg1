def make_album(artist, album, num_track= "Unknown quantity of"):
    dict_album={"artist_name": artist, "album_name": album, "album_track": num_track}
    return dict_album

def print_album(album):
    print("The Artist "+ album["artist_name"] + " create the album "+ album["album_name"] + " that has " + str(album["album_track"]) + " songs")


while True:
    artist=input("Enter an artist>>")
    if artist == "quit" or artist == "":
        break
    album = input("Enter an album>>")
    if album == "quit" or album == "":
        break
    track = input("Enter the quantity of tracks>>")
    if track == "quit":
        break
    if track=="":
        met = make_album(artist, album)
    else:
        met = make_album(artist, album, track)
    print_album(met)
