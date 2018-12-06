def make_album(artist, album, num_track= "Unknown"):
    dict_album={"artist_name": artist, "album_name": album, "album_track": num_track}
    return dict_album

def print_album(album):
    print("The Artist "+ album["artist_name"] + " create the album "+ album["album_name"] + " witch has " + str(album["album_track"]) + " songs")


met=make_album("Metallica", "Reload")
print_album(met)

met=make_album("Leonard Cohen", "The Future")
print_album(met)

met= make_album("Artic Monkeys", "AM")
print_album(met)

met= make_album("Pantera","Cowboys from Hell","12")
print_album(met)