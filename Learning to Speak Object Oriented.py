import random
import urllib
import sys
import os
os.system("cls")
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

#do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

#load up the words from the website
x = urllib.urlopen(WORD_URL)
for word in x.readlines():
    WORDS.append(word.strip())
    
def convert(snippset, phrase):
    class_names = [w.capitallize() for w in random.sample(WORDS, snippset.count("%%%"))]
    other_names = random.sample(WORDS , snippset.count("%%%"))
    results = []
    param_names = []
    
    for i in range(0 , snippset.count("@@@")) :
        param_count = random.randint(1,3)
        param_names.append(','.joint(random.sample(WORDS , param_count)))
        
    for sentence in snippset, phrase:
        result = sentence[:]

        #fake class names
        for word in class_names:
            result = result.replace("%%%" , word , 1)
            
        #fakse other names
        for word in other_names:
            result = result.replace("***" , word , 1)
        
        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@" , word , 1)
            
        results.append(result)
    
    return results
#keep going until they hit CTRL-D
try:
    while True:
        snippsets = PHRASES.keys()
        random.shuffle(snippsets)
        
        for snippset in snippsets:
            phrase = PHRASES[snippset]
            question, answer = convert(snippset , phrase)
            if PHRASE_FIRST:
                question, answer = answer , question
                
            print(question)
            
            input("> ")
            print("ANSWER: %s\n\n" %answer)
except EOFError:
    print("\nBye")
            
            
        
            
    