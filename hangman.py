from tkinter import *
import random

words = ['pineapple','illness','jazz','headset','pain','beetle','hero','villain']   #placeholder wordlist, change into something more elegant later, what, idk
correct_letters = set()
lives = 11
seperationstring = "----------------"

def screen():
    nav = int(input("1)Play\n2)Custom Words (not usable rn though)\n3)Exit\n"))
    print(seperationstring)
    match nav:
        case 1:
            game_loop()
        case 2:
            screen()        #add content here later
        case 3:
            exit()

def game_loop():
    global lives
    word = random.choice(words)
    wordset = set(word)
    displayer(word)
    while lives > 0:
        guess = input("Guess a letter: ")
        print(seperationstring)
        matcher(guess, word)
        displayer(word)
        if wordset^correct_letters==set():  #this sucks, change it later
            print(seperationstring)
            print("You guessed the correct Word: ",word)
            screen()
    print("You have no lives left!!")
    lives = 11  #this feels stupid
    screen()

def displayer(word):
    word_display(word)
    for i in range(0,lives):
        print('O', end = "")
    print(end="\n")

def matcher(guess, word):
    global lives
    for i in word:
        if i == guess:
            print("Correct Guess!!")
            correct_letters.add(guess)
            lives += 1      #bodged
            break
    lives -= 1

def word_display(word):
    for w in word:
        if w in correct_letters:
            print(w, end = "")
        else:
            print("*", end = "")
    print("")


screen()







#gui coming soon, trust
#window = Tk()
#window.mainloop()