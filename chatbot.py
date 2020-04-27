from random import choice
import spotify_info

computerResponses = [] # list of all computer's questions
humanResponses = []  # list of all the person's responses

def spotify_helper():
    """
        gives a list of songs to the user based on their music taste
        this function asks the user questions to narrow down the list
    """
    userComment = input("Computer >> Hello! I am a chatbot that will recommend you songs based on your music taste. Why don't you tell me what kinds of songs you're looking for? (e.g. genre, danceability, song length)\nThe User >> ")

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
    if contains(comment,danceWords):
        return choice(danceResponses)
    if contains(comment,lengthWords):
        return choice(lengthResponses)
    if contains(comment,energyWords):
        return choice(energyResponses)
    return choice(otherResponses)

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
popWords = "pop".split()
sadResponses=[
"Here are some pop songs:"printSongList(pop)
]

rapWords = "rap".split()
sadResponses=[
"Here are some rap songs:"printSongList(rap)
]

hiphopWords = "hip hop hiphop".split()
hiphopResponses=[
"Here are some hip hop songs:"printSongList(hip_hop)
]

edmWords = "edm".split()
edResponses=[
"Here are some edm songs:"printSongList(edm)
]

trapWords = "trap".split()
trapResponses=[
"Here are some trap songs:"printSongList(trap)
]

latinWords = "latin".split()
latinResponses=[
"Here are some latin songs:"printSongList(latin)
]


# We give these responses if there is nothing else to say!
generalResponses = [
  "What genre of music is your favorite?.",
  "Do you mainly listen to short songs or long songs?",
  "Do you like your music to be high ir low energy?",
  "What genre of music would you like to listen to?"
]


if __name__=="__main__":
    spotify_helper()  # call spotify_helper when run as a script
             # but not when imported
