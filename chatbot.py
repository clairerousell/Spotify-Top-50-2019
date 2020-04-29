from random import choice
import spotify_info

computerResponses = [] # list of all computer's questions
humanResponses = []  # list of all the person's responses

def spotify_helper():
    """
        gives a list of songs to the user based on their music taste
        this function asks the user questions to narrow down the list
    """
    userComment = input("Computer >> Hello! I am a chatbot that will recommend you songs \n based on your music taste. Why don't you tell me what kinds \n of songs you're looking for? (e.g. genre, tempo, song length)\nThe User >> ")

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

generalResponses = [
  "What genre of music is your favorite?",
  "Do you mainly listen to short songs or long songs?",
  "What genre of music would you like to listen to?",
  "Do you like short songs or long songs?"
]

if __name__=="__main__":
    spotify_helper()  # call spotify_helper when run as a script
             # but not when imported
