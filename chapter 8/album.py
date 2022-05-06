def make_album(artist, title, number_of_songs = None):
    """creates a dictionary containing the title and artist of an album the number of songs can be included as well"""
    album = {}
    album["artist"] = artist
    album["title"] = title
    if number_of_songs:
        album["number of songs"] = number_of_songs
    return album

while True:
    print("This program gathers information on your favorite album. Press q to quite whenever you want")
    album = input("What's your favorite album? ")
    if album == "q":
        break
    artist = input("Who published the album? ")
    if artist == "q":
        break
    number_of_songs = input("How many songs are in the album (optional)")
    if number_of_songs == "q":
        break
    album_info = make_album(artist, album, number_of_songs)
    print(album_info)