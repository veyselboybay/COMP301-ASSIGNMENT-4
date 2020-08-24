"""
AUTHOR: VEYSEL BOYBAY
STUDENT ID: 301115376
Program: generator.py
Generates and displays sentences using simple grammar
and vocabulary. Words are chosen at random.
"""

import random

def getWords(file_name):
    fileobject=open(f"{file_name}","r")
    contents=fileobject.read()
    fileobject.close()
    File=contents.split(",")
    nouns=()
    for element in File:
        nouns+=(element,)
    return nouns



nouns=getWords("nouns.txt")
articles=getWords("articles.txt")
prepositions=getWords("prepositions.txt")
verbs=getWords("verbs.txt")
adjectives=getWords("adjectives.txt")
conjunctions=getWords("conjunctions.txt")
    
def compoundSentence():
    """Combine two sentences and returns it"""
    return sentence()+" "+random.choice(conjunctions)+" "+sentence()

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) +" "+random.choice(adjectives)+ " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + " "+nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(compoundSentence())
        
main()