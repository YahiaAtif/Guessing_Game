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

def evaluateGuess(number, guess):
    state = 0
    if guess > number:
        print("Your guess is too large")
    elif guess < number:
        print("Your guess is too low")
    else:
        print("Congratualations! You got it")
        state = 1
    return state

#evaluateGuess(25,25)

def play():
    number = getRandom() #calling getRandom
    score = 10 # begining score
    for i in range (0,11):
        guess = getGuess()
        state = evaluateGuess(number, guess)
        if state == 1 : #if answer was corret break loop
            break
        score = score - 1 #if not correct subtract one
    return score

#play()

def game():
    choice = 'y'
    scores = [] #initialize the list for scores
    while choice == 'y':
        score = play() #call play
        print ("Your score was", score) #print current score
        scores.append(score)
        choice = input("Do your want to play again? y to continue: ")
        choice.lower()
    return scores

#game()

def getAverageScore(scores):
    total = 0
    for item in scores:
        total += item
    average = total/len(scores)
    return average

#getAverageScore()

def printAverage(average, name):
    print (name, ", Your average score is", average)

#printAverage()

def main():
    intro() #call intro
    name = getName()
    scores = game()
    average = getAverageScore(scores)
    printAverage(average, name)


main()