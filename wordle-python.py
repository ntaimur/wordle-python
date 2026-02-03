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

print(word)



