import tkinter as tk
import random


# list of words 
word_list_five = ["apple", "grape", "chair", "spice", "track", 
                "flame", "brick", "cloud", "plant", "sugar", 
                "light", "sound", "crane", "blaze", "stone", 
                "water", "bread", "smile", "pride", "globe", 
                "sword", "dream", "magic", "storm", "tiger", 
                "zebra", "eagle", "mouse", "snake", "robot", 
                "laser", "piano", "candy", "beach", "ocean", 
                "river", "earth", "space", "metal", "steel", 
                "flock", "scent", "grain", "sweat", "laugh", 
                "teeth", "heart", "brain"]

word_list_four = ["rate","salt","mint","corn","wind","aero","easy","oath",
                "clay","drip","echo","fame","gaze","hush","iron","jolt","keen","loud",
                "moss","navy","opal","palm","quip","roam","soar","tide","ugly","vain",
                "wade","yarn","zest","brim","chop","dune","envy","flap","glow","haze",
                "idle","jazz","knot","lure","melt","numb","oval","perk","rift","sway"]

word_list_six = [
    "planet","silver","branch","marble","candle","forest","gentle","harbor","jungle","kitten",
    "ladder","magnet","nectar","object","puzzle","quartz","rocket","saddle","tunnel","velvet",
    "wander","yellow","zephyr","anchor","butter","copper","dragon","ember","fabric","galaxy",
    "hammer","island","jester","keeper","laptop","market","notion","orange","pocket","quiver",
    "ribbon","shower","throne","unfold","vacuum","window","wonder","yogurt","zipper","bridge"
]



# welcome
print("\nWelcome to Wordle 2.0!")




def easy_diff():

    print("Guess the 4 letter word in 6 tries or less...")

    # pick a random word
    word = random.choice(word_list_four)

    # number of attempts
    attempts = 1


    while attempts <= 6:
        guess = input(f"\nAttempt {attempts}: ").lower().strip() # ask for user guess

        if len(guess) != 4: # if guess isnt 4 letters
            print("Your guess must be 5 letters. ") 
            continue 
        elif guess.isdigit(): # if guess is a number
            print("Your guess must not have any numbers! ")
            continue


        attempts += 1 # increase attempt by 1 if valid guess

        guess_result = "" # empty string

        for i in range(4): # go thru each letter in the guess and the word
            if guess[i] == word[1]:
                guess_result += "🟩"  # if correct position  
            elif guess[i] in word:
                guess_result += "🟨" # incorrect position but word still has letter
            else:
                guess_result += "🟥" # word doesnt have letter

        print(guess_result, "\n") # print the boxes 

        if guess == word:
            print("You guessed the word!") # if u guess the word
            break
    else:
        print(f"\nYou're out of attempts! The word was {word}!") # ran out of attempts

def medium_diff():

    print("Guess the 5 letter word in 6 tries or less...")

    # pick a random word
    word = random.choice(word_list_five)

    # number of attempts
    attempts = 1


    while attempts <= 6:
        guess = input(f"\nAttempt {attempts}: ").lower().strip() # ask for user guess

        if len(guess) != 5: # if guess isnt 5 letters
            print("Your guess must be 5 letters. ") 
            continue 
        elif guess.isdigit(): # if guess is a number
            print("Your guess must not have any numbers! ")
            continue


        attempts += 1 # increase attempt by 1 if valid guess

        guess_result = "" # empty string

        for i in range(5): # go thru each letter in the guess and the word
            if guess[i] == word[1]:
                guess_result += "🟩"  # if correct position  
            elif guess[i] in word:
                guess_result += "🟨" # incorrect position but word still has letter
            else:
                guess_result += "🟥" # word doesnt have letter

        print(guess_result, "\n") # print the boxes 

        if guess == word:
            print("You guessed the word!") # if u guess the word
            break
    else:
        print(f"\nYou're out of attempts! The word was {word}!") # ran out of attempts


def hard_diff():

    print("Guess the 6 letter word in 6 tries or less...")

    # pick a random word
    word = random.choice(word_list_six)

    # number of attempts
    attempts = 1


    while attempts <= 6:
        guess = input(f"\nAttempt {attempts}: ").lower().strip() # ask for user guess

        if len(guess) != 6: # if guess isnt 6 letters
            print("Your guess must be 5 letters. ") 
            continue 
        elif guess.isdigit(): # if guess is a number
            print("Your guess must not have any numbers! ")
            continue


        attempts += 1 # increase attempt by 1 if valid guess

        guess_result = "" # empty string

        for i in range(6): # go thru each letter in the guess and the word
            if guess[i] == word[1]:
                guess_result += "🟩"  # if correct position  
            elif guess[i] in word:
                guess_result += "🟨" # incorrect position but word still has letter
            else:
                guess_result += "🟥" # word doesnt have letter

        print(guess_result, "\n") # print the boxes 

        if guess == word:
            print("You guessed the word!") # if u guess the word
            break
    else:
        print(f"\nYou're out of attempts! The word was {word}!") # ran out of attempts


easy_diff()
