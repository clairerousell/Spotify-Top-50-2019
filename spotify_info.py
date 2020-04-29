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

# def song_length(length):
#     length = input("Do you want short, medium, or long songs? The songs range from 115-309 seconds"))
# short_length = [d for d in spotify_info if int(d['Length.'])<115 and int(d['Length.'])>180]
# medium_length= [d for d in spotify_info if >int(d['Length.'])<181 and int(d['Length.'])>244]
# long_length = [d for d in spotify_info if int(d['Length.'])<245 and int(d['Length.'])>309]

medium_tempo = [d for d in spotify_info if int(d['Beats.Per.Minute'])<130]
fast_tempo= [d for d in spotify_info if 134<int(d['Beats.Per.Minute'])]


short_length = [d for d in spotify_info if int(d['Length.'])<175]
long_length = [d for d in spotify_info if 176<int(d['Length.'])]


low_speechiness = [d for d in spotify_info if int(d['Speechiness.'])<24]
high_speechiness = [d for d in spotify_info if 47<int(d['Speechiness.'])]


low_valence = [d for d in spotify_info if int(d['Valence.'])<49]
high_valence = [d for d in spotify_info if 95<int(d['Valence.'])]
