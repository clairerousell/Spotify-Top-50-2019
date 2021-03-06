import csv

spotify_info = list(csv.DictReader(open('top50.csv','r'),delimiter=','))

#print("this list has",len(spotify_info),"items in it")
##spotify_info[9]  # the dictionary at position 9 is for bad guy by Billie Eilish


# Printing song information
def printSong(d):
    return str(d['Track.Name'])+'---'+str(d['Artist.Name'])
##printSong(spotify_info[9])

def printSongList(ds):
    song_list=""
    for d in ds:
        song_list=song_list+printSong(d)
        song_list=song_list+"\n"
    return song_list
##printSongList(spotify_info[:5])

pop = [d for d in spotify_info if "pop" in d['Genre']]
trap = [d for d in spotify_info if "trap" in d['Genre']]
rap = [d for d in spotify_info if "rap" in d['Genre']]
hip_hop = [d for d in spotify_info if "hip hop" in d['Genre']]
edm = [d for d in spotify_info if "edm" in d['Genre']]
latin = [d for d in spotify_info if "latin" in d['Genre']]

medium_tempo = [d for d in spotify_info if 84>int(d['Beats.Per.Minute'])>119]
fast_tempo= [d for d in spotify_info if 120>int(d['Beats.Per.Minute'])>155]
very_fast_tempo = [d for d in spotify_info if 156>int(d['Beats.Per.Minute'])>191]

# using user inputs to create the list of songs
#print("This code gives the user a playlist of songs from the Top 50 most popular songs on Spotify from 2019")
#genre=input("Which genre of music are you looking for?")
#print("Here's your playlist based on the genre you specified:")
# if "pop" in genre:
#     printSongList(pop)
# elif "trap" in genre:
#     printSongList(trap)
# elif "rap" in genre:
#     printSongList(rap)
# elif "latin" in genre:
#     printSongList(pop)
# elif "edm" in genre:
#     printSongList(edm)
# elif "hip hop" in genre:
#     printSongList(hip_hop)
# elif "hiphop" in genre:
#     printSongList(hip_hop)
# else:
#     print("Sorry, no song from our list is in that genre.")

#song_speed=input("Do you like [1] medium tempo songs, [2] fast songs, or [3] very fast songs?")
#print("Here is your playlist based on the tempo you specified:")
#if song_speed=="1":
    #printSongList(medium_tempo)
#if song_speed=="2":
    #printSongList(fast_tempo)
#if song_speed=="3":
    #printSongList(very_fast_tempo)