import tkinter as tk
import random
from PIL import Image, ImageTk
from tkinter import ttk
from wordfreq import zipf_frequency
gameLoop = False # true to run game
import os
import sys

def restart():
    os.execv(sys.executable, ['python'] + sys.argv)


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

# ################################### TKINTER TESTING ###################################


root = tk.Tk()
root.title("Wordle 2.0")  # title
window_width = 600
window_height = 800
root.attributes("-alpha", 1.0)


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


######################### FADING ANIMATION #########################


def switch_to_next_screen(callback=None):
    if screen1.winfo_ismapped():
        screen1.pack_forget()
        screen2.pack(fill="both", expand=True)
    elif screen2.winfo_ismapped():
        screen2.pack_forget()
        screen3.pack(fill="both", expand=True)
    elif screen3.winfo_ismapped():
        screen3.pack_forget()
        screen4.pack(fill="both", expand=True)
    elif screen4.winfo_ismapped():
        screen4.pack_forget()
        screen1.pack(fill="both", expand=True)

    if callback:
        callback()



def fade_in(window, step=0.05):
    alpha = float(window.attributes("-alpha"))
    if alpha < 1:
        alpha += step
        window.attributes("-alpha", alpha)
        window.after(20, lambda: fade_in(window, step))

def fade_out(window, step=0.05, callback=None):
    alpha = float(window.attributes("-alpha"))
    if alpha > 0.5:
        alpha -= step
        window.attributes("-alpha", alpha)
        window.after(20, lambda: fade_out(window, step, callback))
    else:
        switch_to_next_screen(callback)
        fade_in(window)



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
title.place(relx=0.5, rely=0.40, anchor="center")        
information_title = tk.Label(screen1,
                 text="A word guessing game\n made in Python!",
                 font=("Georgia", 25),
                 fg="black",
                 bg="#e3e3e1")
information_title.place(relx=0.5, rely=0.51, anchor="center")       



######### PLAY BUTTON #########
play_button = tk.Button(screen1,
                        text="Play ▶",
                        command=lambda: fade_out(root),
                        font=("Comfortaa", 15),
                        width=8,
                        height=1,
                        fg="black",
                        bg="#e3e3e1",
                        borderwidth=5,
                        relief="ridge") # border style

play_button.bind("<Enter>", lambda e: play_button.config(bg="#d3d3d3")) # effects on hover
play_button.bind("<Leave>", lambda e: play_button.config(bg="#e3e3e1"))

play_button.place(relx=0.5, rely=0.65, anchor="center")  

######################### SCREEN 2 #########################

screen2 = tk.Frame(root, bg="#e3e3e1")

###### CHOOSE DIFFICULTY TEXT ######
choose_difficulty_text = tk.Label(screen2,
                                text="Choose your difficulty: ",  # text formatting for choosing difficulty
                                font=("Impact", 35),
                                fg="black",
                                bg="#e3e3e1")

choose_difficulty_text.place(relx=0.5, rely=0.37, anchor="center")        




########### DIFFICULTY BUTTONS ############


## create 3rd screen 
screen3 = tk.Frame(root, width=600, height=800, bg="#1B1A1A")


## create game over screen 
screen4 = tk.Frame(root, width=600, height=800, bg="#1B1A1A")


############## GUESS CHECKER ##############

def disappearing_text(label, duration=1000):
    label.after(duration, label.destroy) # destroy label after duration



def check_guess(entry, target_word):
    global current_row
    global guess
    guess = entry.get().lower().strip()
    entry.delete(0, tk.END) # clear entry after sumbit




    # check guess
    if len(guess) != len(target_word):
        world_letter_amount_invalid = tk.Label(screen3,
                                text=f"Your guess must be {len(target_word)} letters!",  
                                font=("Georgia", 15),
                                fg="red",
                                bg="#1B1A1A")
        world_letter_amount_invalid.place(relx=0.5, rely=0.775, anchor="center")
        disappearing_text(world_letter_amount_invalid) # call destroying func   
        return
    if any(char.isdigit() for char in guess):
        world_letter_has_digit_invalid = tk.Label(screen3,
                                text=f"Your guess must have no digits!",  
                                font=("Georgia", 15),
                                fg="red",
                                bg="#1B1A1A")
        world_letter_has_digit_invalid.place(relx=0.5, rely=0.775, anchor="center")
        disappearing_text(world_letter_has_digit_invalid) # call destroying func   
        return
    if zipf_frequency(guess, 'en') < 3.0: # check if real word in english
        world_letter_not_real_invalid = tk.Label(screen3,
                                text=f"Your guess must be a real word!",  
                                font=("Georgia", 15),
                                fg="red",
                                bg="#1B1A1A")
        world_letter_not_real_invalid.place(relx=0.5, rely=0.775, anchor="center")
        disappearing_text(world_letter_not_real_invalid) # call destroying func   
        return

    # fill tiles
    for i in range(len(guess)):
        letter = guess[i]
        tile = tiles[current_row][i]
        tile.config(text=letter.upper())

        kb_tile = keyboard_tiles[letter.upper()]

        if guess[i] == target_word[i]:
            tile.config(bg="#359e35")  # right
            kb_tile.config(bg="#359e35") # update keyboard tile color   
        elif guess[i] in target_word:
            tile.config(bg="#d8d843")  # wrong pos
            if kb_tile.cget("bg") != "#359e35": # only update keyboard tile color if not already green
                kb_tile.config(bg="#d8d843")
        else:
            tile.config(bg="#424242")  # no
            if kb_tile.cget("bg") != "#359e35" and kb_tile.cget("bg") != "#d8d843": # only update keyboard tile color if not already green or yellow
                kb_tile.config(bg="#424242")
    current_row += 1


    ############### CHECK IF GAME OVER ##############

    if guess == target_word:
        fade_out(root) # go to game over screen
        win_label = tk.Label(screen4, 
                             text="You Won!",
                            font=("Impact", 60), 
                            fg="white", 
                            bg="#1B1A1A")
        win_label.place(relx=0.5, rely=0.3, anchor="center")    

        ############### PLAY AGAIN BUTTON ###############

        play_again_button = tk.Button(screen4,
                        text="Play Again",
                        command=lambda: restart(),
                        font=("Comfortaa", 15),
                        width=10,
                        height=2,
                        fg="black",
                        bg="#e3e3e1",
                        borderwidth=5,
                        relief="ridge") # border style

        play_again_button.bind("<Enter>", lambda e: play_again_button.config(bg="#d3d3d3")) # effects on hover
        play_again_button.bind("<Leave>", lambda e: play_again_button.config(bg="#e3e3e1"))

        play_again_button.place(relx=0.5, rely=0.65, anchor="center")      
    elif current_row >= 6:
        fade_out(root) # go to game over screen
        game_over_label = tk.Label(screen4,
                                    text="You Lost!",
                                    font=("Impact", 60),
                                    fg="white", 
                                    bg="#1B1A1A")
        game_over_label.place(relx=0.5, rely=0.3, anchor="center")
        game_over_desc1 = tk.Label(screen4,
                                    text=f"You're out of attempts!\n The word was {target_word.upper()}!",
                                    font=("Georgia", 20),
                                    fg="white", 
                                    bg="#1B1A1A")
        game_over_desc1.place(relx=0.5, rely=0.5, anchor="center")
        
        ############### PLAY AGAIN BUTTON ###############

        play_again_button = tk.Button(screen4,
                        text="Play Again",
                        command=lambda: restart(),
                        font=("Comfortaa", 15),
                        width=10,
                        height=2,
                        fg="black",
                        bg="#e3e3e1",
                        borderwidth=5,
                        relief="ridge") # border style

        play_again_button.bind("<Enter>", lambda e: play_again_button.config(bg="#d3d3d3")) # effects on hover
        play_again_button.bind("<Leave>", lambda e: play_again_button.config(bg="#e3e3e1"))

        play_again_button.place(relx=0.5, rely=0.65, anchor="center")  

############################################################ MAIN GAME FUNCTION ###########################################################################
def start_game(word_length, word_list):
    screen2.pack_forget()
    screen3.pack(fill="both", expand=True)

    # pick random word
    target_word = random.choice(word_list)


    board_frame = tk.Frame(screen3, bg="#1B1A1A")
    board_frame.pack(pady=25)

    # store tiles
    global tiles, current_row
    tiles = [] # empty list to store tile labels
    current_row = 0

    # create 6 rows of tiles
    for row in range(6):
        row_tiles = []
        for col in range(word_length):
            tile = tk.Label(board_frame,
                            text="",
                            font=("Arial Black", 20, "bold"),
                            width=4,
                            height=2,
                            bg="#1B1A1A",
                            fg="white",
                            relief="ridge",
                            borderwidth=3)
            tile.grid(row=row, column=col, padx=5, pady=2)
            row_tiles.append(tile)
        tiles.append(row_tiles)

    # input box
    guess_entry = tk.Entry(board_frame, font=("Georgia", 20), justify="center")
    guess_entry.grid(row=7, column=0, columnspan=word_length, pady=12)


    # submit 
    guess_entry.bind("<Return>", lambda e: check_guess(guess_entry, target_word))


    ############################# KEYBOARD #############################

    alphabet = ["QWERTYUIOP ", " ASDFGHJKL ", "  ZXCVBNM  "]
    keyboard_frame = tk.Frame(screen3, bg="#1B1A1A")
    global keyboard_tiles
    keyboard_tiles = {}
    keyboard_frame.pack(pady=1)
    for r, row in enumerate(alphabet):
        for i, letter in enumerate(row):
            tile = tk.Label (keyboard_frame,
                            text=letter,
                            font=("Arial", 20),
                            width=2,
                            height=1,
                            bg="#1B1A1A",
                            fg="white",
                            relief="sunken",
                            borderwidth=1
                            )
            tile.grid(row=r, column=i, padx=1, pady=5)
            keyboard_tiles[letter] = tile


#### EASY BUTTON #####
easy_button = tk.Button(screen2,
                        text="Easy",
                        font=("Georgia", 15),
                        width=8,
                        height=1,
                        fg="black",
                        bg="#8ef08e",
                        borderwidth=5,
                        relief="ridge",
                        command=lambda: fade_out(root, callback=lambda: start_game(4, word_list_four)),)





easy_button.bind("<Enter>", lambda e: easy_button.config(bg="#cbf0cb")) # effects on hover
easy_button.bind("<Leave>", lambda e: easy_button.config(bg="#8ef08e"))

easy_button.place(relx=0.25, rely=0.5, anchor="center")  

## quick description of easy difficulty
easy_diff_desc = tk.Label(screen2,
                            text="(4 letters)",  
                            font=("Georgia", 12),
                            fg="#000000",
                            bg="#e3e3e1")

easy_diff_desc.place(relx=0.25, rely=0.55, anchor="center")  


### MEDIUM BUTTON #####
medium_button = tk.Button(screen2,
                        text="Medium",
                        font=("Georgia", 15),
                        width=8,
                        height=1,
                        fg="black",
                        bg="#ebeb78",
                        borderwidth=5,
                        relief="ridge",
                        command=lambda: fade_out(root, callback=lambda: start_game(5, word_list_five)),)

medium_button.bind("<Enter>", lambda e: medium_button.config(bg="#fafac8")) 
medium_button.bind("<Leave>", lambda e: medium_button.config(bg="#ebeb78"))

medium_button.place(relx=0.5, rely=0.5, anchor="center")  

## quick description of medium difficulty
medium_diff_desc = tk.Label(screen2,
                            text="(5 letters)",  
                            font=("Georgia", 12),
                            fg="#000000",
                            bg="#e3e3e1")

medium_diff_desc.place(relx=0.5, rely=0.55, anchor="center")  

#### HARD BUTTON #####
hard_button = tk.Button(screen2,
                        text="Hard",
                        font=("Georgia", 15),
                        width=8,
                        height=1,
                        fg="black",
                        bg="#fd7979",
                        borderwidth=5,
                        relief="ridge",
                        command=lambda: fade_out(root, callback=lambda: start_game(6, word_list_six))) 

hard_button.bind("<Enter>", lambda e: hard_button.config(bg="#ffcece")) 
hard_button.bind("<Leave>", lambda e: hard_button.config(bg="#fd7979"))

hard_button.place(relx=0.75, rely=0.5, anchor="center")  

## quick description of hard difficulty
hard_diff_desc = tk.Label(screen2,
                        text="(6 letters)",  
                        font=("Georgia", 12),
                        fg="#000000",
                        bg="#e3e3e1")

hard_diff_desc.place(relx=0.75, rely=0.55, anchor="center")  










#### MAIN LOOP #####
root.mainloop()








# ################################### GAME ###################################





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