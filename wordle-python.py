import tkinter as tk
import random


# list of words 
word_list = ["apple", "grape", "chair", "spice", "track", 
         "flame", "brick", "cloud", "plant", "sugar", 
         "light", "sound", "crane", "blaze", "stone", 
         "water", "bread", "smile", "pride", "globe", 
         "sword", "dream", "magic", "storm", "tiger", 
         "zebra", "eagle", "mouse", "snake", "robot", 
         "laser", "piano", "candy", "beach", "ocean", 
         "river", "earth", "space", "metal", "steel", 
         "flock", "scent", "grain", "sweat", "laugh", 
         "teeth", "heart", "brain"]

# welcome
print("\nWelcome to Wordle 2.0!")
print("Guess the 5 letter word in 6 tries or less...")

# pick a random word
word = random.choice(word_list)

# number of attempts
attempts = 1


while attempts <= 6:
    guess = input(f"\nAttempt {attempts}: ").lower().strip()

    if len(guess) != 5:
        print("Your guess must be 5 letters. ")
        continue

    attempts += 1

    guess_result = ""

    for i in range(5):
        if guess[i] == word[1]:
            guess_result += "🟩"
        elif guess[i] in word:
            guess_result += "🟨"
        else:
            guess_result += "🟥"

    print(guess_result, "\n")

    if guess == word:
        print("You guessed the word!")
        break
else:
    print(f"\nYou're out of attempts! The word was {word}!")





