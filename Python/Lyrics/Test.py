def get_lyrics(artists, song_limit):
    c = 0
    for artist in artists:
        try:
            songs = (genius.search_artist(artist, max_songs=song_limit, sort='popularity')).songs
            song_lyrics_list = [song.lyrics for song in songs]
            file = open(f"{artist}_lyrics_of_{len(song_lyrics_list)}_songs.txt", "w", encoding='utf-8')
            file.write("\n \n \n \n \n".join(song_lyrics_list))
            c += 1
            print(f"Songs grabbed:{len(song_lyrics_list)}")
            file.close()
            print("___________________________________________________\n\n\n\n")
        except:
            print(f"some exception at {artist}: {c}")
# Sorts = popularity release_date title

api_key = input("Your api key")
import lyricsgenius as lg
genius = lg.Genius(api_key, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
art = ["Pop Smoke","Weekend"]
lyrics = get_lyrics(art, 5)
#