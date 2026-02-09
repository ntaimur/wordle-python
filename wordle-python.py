import tkinter as tk
import random
from PIL import Image, ImageTk
from tkinter import ttk
from wordfreq import zipf_frequency
gameLoop = False # true to run game


# ************************ TKINTER TESTING ************************




import tkinter as tk

root = tk.Tk()
root.title("Wordle 2.0")  # title
window_width = 600
window_height = 800

root.iconbitmap('./assets/wordle.ico')  # set icon

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# cant resize window
root.resizable(False, False) # maybe change to true later

# move to top
root.attributes('-topmost', 1)

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

######################### SCREEN 1 #########################

screen1 = tk.Frame(root, width=600, height=800, bg="#e3e3e1")
screen1.pack(fill="both", expand=True)

######### LOGO #########
img_Wordle_logo = Image.open("./assets/wordle-logo.png") 
img = img_Wordle_logo.resize((100, 100)) # adjust size 

wordle_logo = ImageTk.PhotoImage(img)
logo_label = tk.Label(screen1, image=wordle_logo, bg="#e3e3e1") # image 
logo_label.place(relx=0.5, rely=0.25, anchor="center")   # 25% down the screen

######### TITLE #########
title = tk.Label(screen1,
                 text="Wordle 2.0",
                 font=("Impact", 50),
                 fg="black",
                 bg="#e3e3e1")
title.place(relx=0.5, rely=0.40, anchor="center")        # 40% down the screen
information_title = tk.Label(screen1,
                 text="A word guessing game\n made in Python!",
                 font=("Times New Roman", 25),
                 fg="black",
                 bg="#e3e3e1")
information_title.place(relx=0.5, rely=0.51, anchor="center")        # 51% down the screen


######### FUNC TO GO TO NEXT PAGE #########
def go_screen_2():
    screen1.pack_forget()  # hide the first screen
    screen2.pack(fill="both", expand=True)  # show screen 2

######### PLAY BUTTON #########
play_button = tk.Button(screen1,
                        text="Play ▶",
                        command=go_screen_2,
                        font=("Comfortaa", 15),
                        width=8,
                        height=1,
                        fg="black",
                        bg="#e3e3e1",
                        borderwidth=5,
                        relief="ridge") # border style

play_button.bind("<Enter>", lambda e: play_button.config(bg="#d3d3d3")) # effects on hover
play_button.bind("<Leave>", lambda e: play_button.config(bg="#e3e3e1"))

play_button.place(relx=0.5, rely=0.65, anchor="center")  # 65% down the screen

######################### SCREEN 2 #########################

screen2 = tk.Frame(root, bg="#e3e3e1")
choose_difficulty_text = tk.Label(screen2,
                  text="Choose your difficulty: EASY (E), MEDIUM (M), HARD (H)...",
                  bg="#e3e3e1",
                  font=("Arial", 10))
choose_difficulty_text.pack(pady=20)

root.mainloop()








# ************************ GAME ************************


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


# func for playing again
def game_loop_func():
    global gameLoop
    print("\nWant to play again?")
    playAgain = input("Play again? (Y/N): ").lower().strip()
    if playAgain == "y":
        gameLoop = True # restart main game loop
    elif playAgain == "n": # if no
        print("Thanks for playing!")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.") # keep looping until valid input
        game_loop_func()





while gameLoop: # main game loop
    
    gameLoop = False # stop loop when game starts


    # funcs for all difficulties
    def easy_diff():

        print("\nGuess the 4 letter word in 6 tries or less...")

        # pick a random word
        word = random.choice(word_list_four)

        # number of attempts
        attempts = 1


        while attempts <= 6:
            guess = input(f"\nAttempt {attempts}: ").lower().strip() # ask for user guess

            if len(guess) != 4: # if guess isnt 4 letters
                print("Your guess must be 4 letters. ") 
                continue 
            elif guess.isdigit(): # if guess is a number
                print("Your guess must not have any numbers! ")
                continue
            elif zipf_frequency(guess, 'en') < 3.0: # if guess is not a common word
                print("Your guess must be a real word! ")
                continue



            attempts += 1 # increase attempt by 1 if valid guess

            guess_result = "" # empty string

            for i in range(4): # go thru each letter in the guess and the word
                if guess[i] == word[i]:
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

        print("\nGuess the 5 letter word in 6 tries or less...")

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
            elif zipf_frequency(guess, 'en') < 3.0: # if guess is not a common word
                print("Your guess must be a real word! ")
                continue



            attempts += 1 # increase attempt by 1 if valid guess

            guess_result = "" # empty string

            for i in range(5): # go thru each letter in the guess and the word
                if guess[i] == word[i]:
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

        print("\nGuess the 6 letter word in 6 tries or less...")

        # pick a random word
        word = random.choice(word_list_six)

        # number of attempts
        attempts = 1


        while attempts <= 6:
            guess = input(f"\nAttempt {attempts}: ").lower().strip() # ask for user guess

            if len(guess) != 6: # if guess isnt 6 letters
                print("Your guess must be 6 letters. ") 
                continue 
            elif guess.isdigit(): # if guess is a number
                print("Your guess must not have any numbers! ")
                continue
            elif zipf_frequency(guess, 'en') < 3.0: # if guess is not a common word
                print("Your guess must be a real word! ")
                continue


            attempts += 1 # increase attempt by 1 if valid guess

            guess_result = "" # empty string

            for i in range(6): # go thru each letter in the guess and the word
                if guess[i] == word[i]:
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



    # welcome
    print("\nWelcome to Wordle 2.0!")

    print("\nChoose your difficulty: EASY (E), MEDIUM (M), HARD (H)...") # choose difficulty
    while True:
        input_choice = input("Difficulty: ").lower().strip()
        if input_choice == "e":
            easy_diff()
            game_loop_func() # ask to play again
            break
        elif input_choice == "m":
            medium_diff()
            game_loop_func()
            break
        elif input_choice == "h":
            hard_diff()
            game_loop_func()
            break
        else:
            print("Invalid input. Please enter 'E', 'M', or 'H'.") # keep looping until valid input
            continue