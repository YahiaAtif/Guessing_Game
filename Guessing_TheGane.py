# import random function
from random import randrange

#Introduction
def intro():
    print("**************************")
    print("The game will choose a random number ")
    print("berween 1 and 1000. you will be given ")
    print("10 guesses. you start with 10 Points. Each ")
    print("worng guess subracts a point. You can play")
    print("As many tines as you like ")
    print("***************************")
    
#intro()

#get the users name
def getName():
    name = input("Enter your player name: ")
    #print(name)
    return name

#getName()

#Set the random number
def getRandom():
    number = randrange(1,1001)
    return number

#getRandom()

def getGuess():
    guess = int(input("Enter your guess: "))
    return guess

#getGuess()