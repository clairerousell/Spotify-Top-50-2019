from random import choice
import spotify_info

computerResponses = [] # list of all computer's questions
humanResponses = []  # list of all the person's responses

def spotify_helper():
    """
        gives a list of songs to the user based on their music taste
        this function asks the user questions to narrow down the list
    """
    userComment = input("Computer >> Hello! I am a chatbot that will recommend you songs \n based on your music taste. Why don't you tell me what kinds \n of songs you're looking for? (e.g. genre, tempo, song length, valence, speechiness)\nThe User >> ")

    while userComment not in ["goodbye","bye","quit","exit"]:
        humanResponses.append(userComment)
        response = respond(userComment)
        if response in computerResponses:
            response = "Once again, "+response
        computerResponses.append(response)
        print("Computer >> "+response)
        userComment = input("The User >> ")
    print("bye")

def respond(comment):
    """ generate a computer response to the user's comment"""
    if contains(comment,popWords):
        return choice(popResponses)
    if contains(comment,shortWords):
        return choice(shortResponses)
    if contains(comment,longWords):
        return choice(longResponses)
    if contains(comment,mediumWords):
        return choice(mediumResponses)
    if contains(comment,fastWords):
        return choice(fastResponses)
    if contains(comment,trapWords):
        return choice(trapResponses)
    if contains(comment,rapWords):
        return choice(rapResponses)
    if contains(comment,positiveWords):
        return choice(positiveResponses)
    if contains(comment,musicalWords):
        return choice(musicalResponses)
    if contains(comment,spokenWords):
        return choice(spokenResponses)
    if contains(comment,negativeWords):
        return choice(negativeResponses)
    if contains (comment,lowenergyWords):
        return choice(lowenergyResponses)
    if contains (comment,highenergyWords):
        return choice(highenergyResponses)
    if contains (comment,popularWords):
        return choice(popularResponses)
    if contains (comment,unpopularWords):
        return choice(unpopularResponses)
    if contains(comment,hiphopWords):
        return choice(hiphopResponses)
    if contains(comment,latinWords):
        return choice(latinResponses)
    if contains(comment,edmWords):
        return choice(edmResponses)
    return choice(generalResponses)

def contains(sentence,words):
    """ true if one of the words is in the sentence
        where sentence is a string and
        words is a list of strings
    """
    wordsInSentence = [word for word in words if word in sentence]
    return len(wordsInSentence) >= 1

def contains2(sentence,words):
    """
    a more efficient test to see if a word in the list words
    is also in the string sentence. Note, this will return
    True for contains2("lovely day",["el"])
    which might not be what you wanted. We could first split
    sentence into words, which might be better!
    """
    for w in words:
        if w in sentence:
            return True
    return False

# Here are the sad keywords and responses to sad comments
popWords = "pop Pop".split()
popResponses=[
"Here are some pop songs:"+(spotify_info.printSongList(spotify_info.pop))+"\nWhat other kinds of music do you like?"
]

rapWords = "rap Rap".split()
rapResponses=[
"Here are some rap songs:"+(spotify_info.printSongList(spotify_info.rap))+"\nWhat other kinds of music do you like?"
]

hiphopWords = "hip hop hiphop Hip Hop Hiphop".split()
hiphopResponses=[
"Here are some hip hop songs:"+(spotify_info.printSongList(spotify_info.hip_hop))+"\nWhat other kinds of music do you like?"
]

edmWords = "edm EDM Edm".split()
edmResponses=[
"Here are some edm songs:"+(spotify_info.printSongList(spotify_info.edm))+"\nWhat other kinds of music do you like?"
]

trapWords = "trap Trap".split()
trapResponses=[
"Here are some trap songs:"+(spotify_info.printSongList(spotify_info.trap))+"\nWhat other kinds of music do you like?"
]

latinWords = "latin Latin".split()
latinResponses=[
"Here are some latin songs:"+(spotify_info.printSongList(spotify_info.latin))+"\nWhat other kinds of music do you like?"
]


shortWords = "short Short".split()
shortResponses=[
"Here are some short songs:"+(spotify_info.printSongList(spotify_info.short_length))+"\nWhat other kinds of music do you like?"
]


longWords = "long Long".split()
longResponses=[
"Here are some long songs:"+(spotify_info.printSongList(spotify_info.long_length))+"\nWhat other kinds of music do you like?"
]

mediumWords = "medium Medium".split()
mediumResponses=[
"Here are some medium tempo songs:"+(spotify_info.printSongList(spotify_info.medium_tempo))+"\nWhat other kinds of music do you like?"
]

fastWords = "fast Fast".split()
fastResponses=[
"Here are some fast songs:"+(spotify_info.printSongList(spotify_info.fast_tempo))+"\nWhat other kinds of music do you like?"
]

positiveWords = "positive happy optimistic".split()
positiveResponses=[
"Here are some songs with high valence (a more positive and happy mood):"+(spotify_info.printSongList(spotify_info.high_valence))+"\nWhat other kinds of music do you like?"
]

negativeWords = "negative sad pessimistic".split()
negativeResponses=[
"Here are some songs with low valence (a more negative and sad mood):"+(spotify_info.printSongList(spotify_info.low_valence))+"\nWhat other kinds of music do you like?"
]

spokenWords = "spoken speech speak".split()
spokenResponses=[
"Here are some songs with high speechiness (songs that include more spoken word):"+(spotify_info.printSongList(spotify_info.high_speechiness))+"\nWhat other kinds of music do you like?"
]

musicalWords = "sung musical".split()
musicalResponses=[
"Here are some songs with low speechiness (songs that include less spoken word):"+(spotify_info.printSongList(spotify_info.low_speechiness))+"\nWhat other kinds of music do you like?"
]

lowenergyWords = "low slow quiet calm serene calming".split()
lowenergyResponses =[
"Here are some songs with low energy:"+(spotify_info.printSongList(spotify_info.low_energy))+"\nWhat other kinds of music do you like?"
]

higheneryWords = "intense active fast loud noisy".split()
highenergyResponses =[
"Here are some songs with high energy:"+(spotify_info.printSongList(spotify_info.high_energy))+"\nWhat other kinds of music do you like?"
]

unpopularWords = "unheard underground unknown lesser known underplayed".split()
unpopularResponses =[
"Here are some lesser known songs:"+(spotify_info.printSongList(spotify_info.low_popularity))+"\nWhat other kinds of music do you like?"
]

popularWords = "popular famous trendy catchy".split()
popularResponses =[
"Here are some really popular songs:"+(spotify_info.printSongList(spotify_info.high_popularity))+"\nWhat other kinds of music do you like?"
]

danceWords = "dance party fun danceable dancing rhythm rhytmic".split()
danceResponses =[
"Here are some songs that are easy to dance to:"(spotify_info.printSongList(spotify_info.high_danceability))+"\nWhat other kinds of music do you like?"
]

relaxingWords = "relax relaxing chill".split()
relaxingResponses =[ 
"Here are more relaxing songs unwind:"+(spotify_info.printSongList(spotify_info.low_danceability))+"\nWhat other kinds of music do you like?"
]

generalResponses = [
  "What genre of music is your favorite?",
  "Do you mainly listen to short songs or long songs?",
  "What genre of music would you like to listen to?",
  "Do you like short songs or long songs?",
  "Do you prefer songs with a positive or negative mood?",
  "Do you like songs with spoken word or with more of a musical quality?",
  "Do you like songs where the words are more often sung or spoken?",
  "Do you prefer to listen to more energetic or calmer music?"
  "Does your playlist consist more of popular or lesser known songs? Do you prefer one or the other?",
  "Do you want to listen to songs you can dance or unwind to?"

]

if __name__=="__main__":
    spotify_helper()  # call spotify_helper when run as a script
             # but not when imported
