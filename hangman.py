from tkinter import *
import random

import os

#https://en.wikipedia.org/wiki/Camel_case

#No use of classes (OOP)

words = ['pineapple','illness','jazz','headset','pain','beetle','hero','villain']   #See https://github.com/dwyl/english-words, https://www.geeksforgeeks.org/pulling-a-random-word-or-string-from-a-line-in-a-text-file-in-python/
correct_letters = set()
lives = 11
seperationstring = "----------------"

def screen():    #Name for a class not a function e.g showScreen
    nav = int(input("1)Play\n2)Custom Words (not usable rn though)\n3)Exit\n"))     #nav = navigation? why not write navigation or navigationChoice
    print(seperationstring)
    match nav:
        case 1:
            game_loop()
        case 2:
            screen()        #add content here later
        case 3:
            exit(0)         #Good practice to provide a exit code (0 == all good)

def game_loop():
    global lives
    word = random.choice(words)
    wordset = set(word)
    displayer(word)
    while lives > 0:
        guess = input("Guess a letter: ")
        print(seperationstring)

        os.system("cls")                    #clear screen
        
        matcher(guess, word)
        displayer(word)
        if wordset^correct_letters==set():  #this sucks, change it later
            print(seperationstring)
            print("You guessed the correct Word: ",word)
            screen()
    print("You have no lives left!!")
    lives = 11  #this feels stupid
    screen()

def displayer(word):            #Maybe a name for a class but not a function, should be something like displayWord
    word_display(word)
    for i in range(0,lives):
        print('O', end = "")
    print(end="\n")

def matcher(guess, word):       #Maybe a name for a class but not a function, should be something like matchWord
    global lives
    for i in word:
        if i == guess:
            print("Correct Guess!!")
            correct_letters.add(guess)
            lives += 1      #bodged
            return                      #return instead of breaking
    lives -= 1

def word_display(word):         #Maybe a name for a class but not a function, should be something like displayWordGraphic?
    for w in word:
        if w in correct_letters:
            print(w, end = "")
        else:
            print("*", end = "")
    print("")


if __name__ == "__main__":  #https://realpython.com/if-name-main-python/
    screen()                # Should have a recognizable name for a main function e.g hangman, main, entryPoint


#gui coming soon, trust
#window = Tk()
#window.mainloop()