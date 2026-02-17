import tkinter as tk
import random
from PIL import Image, ImageTk
from tkinter import ttk
from wordfreq import zipf_frequency
import os
import sys
import re


def restart():
    os.execv(sys.executable, ['python'] + sys.argv)


# list of words 
word_list_five = [
    "apple", "grape", "chair", "spice", "track",
    "flame", "brick", "cloud", "plant", "sugar",
    "light", "sound", "crane", "blaze", "stone",
    "water", "bread", "smile", "pride", "globe",
    "sword", "dream", "magic", "storm", "tiger",
    "zebra", "eagle", "mouse", "snake", "robot",
    "laser", "piano", "candy", "beach", "ocean",
    "river", "earth", "space", "metal", "steel",
    "flock", "scent", "grain", "sweat", "laugh",
    "teeth", "heart", "brain",
    "flint", "crown", "bloom", "frost", "shark",
    "whale", "ghost", "skull", "flute", "prism",
    "spore", "cloak", "forge", "quill", "raven",
    "bluff", "crisp", "dwarf", "ember", "fable",
    "giant", "honey", "ivory", "jelly", "knock",
    "lemon", "mango", "nylon", "olive", "pearl",
    "quilt", "rider", "sheep", "torch", "ultra",
    "vivid", "woven", "yeast", "zesty", "badge",
    "charm", "dodge", "fancy", "glide", "haste",
    "index", "jolly", "karma", "lunar", "mirth",
    "noble", "orbit", "punch", "quark", "risky",
    "shiny", "twist", "vapor", "waltz", "youth",
    "adore", "align", "amuse", "angel", "ankle",
    "arbor", "armor", "arrow", "asset", "attic",
    "baker", "balmy", "banjo", "basil", "batch",
    "beast", "belly", "berry", "bison", "bland",
    "blend", "blink", "bliss", "bloom", "blunt",
    "boast", "bonus", "bound", "brave", "briar",
    "brisk", "broad", "broil", "broom", "brush",
    "cabin", "cable", "camel", "canal", "cargo",
    "carol", "carve", "catch", "cedar", "chase",
    "cheer", "chess", "chill", "cider", "civic",
    "clash", "clasp", "cliff", "cling", "clink",
    "cloak", "clone", "close", "clown", "cocoa",
    "coral", "couch", "coven", "cover", "craft",
    "crash", "creek", "crest", "cubic", "curry",
    "daisy", "delta", "diner", "dizzy", "donut",
    "drape", "drift", "drill", "drown", "dusty",
    "eager", "early", "elbow", "ember", "entry",
    "equal", "error", "event", "every", "exact",
    "faith", "feast", "ferry", "fiber", "field",
    "fiery", "fifth", "final", "flair", "fleet",
    "flora", "focus", "folly", "found", "fresh",
    "furry", "gamer", "gauge", "genre", "glare",
    "gleam", "glory", "grasp", "greed", "grill",
    "grove", "habit", "harsh", "haste", "haunt",
    "hazel", "hinge", "hobby", "holly", "honey",
    "hound", "hover", "humor", "hurry", "ideal",
    "image", "imply", "inbox", "inner", "input",
    "irony", "japan", "jazzy", "joint", "judge",
    "juice", "koala", "label", "latch", "layer",
    "learn", "level", "linen", "liver", "lodge",
    "logic", "loyal", "lucky", "lunar", "lyric",
    "macro", "maker", "march", "marsh", "medal",
    "merit", "micro", "miner", "model", "moist",
    "moral", "motel", "motor", "mound", "music",
    "naval", "nerve", "ninth", "nurse", "oasis",
    "occur", "offer", "onion", "opera", "optic",
    "paint", "panel", "panic", "party", "patch",
    "pause", "peach", "phase", "phone", "photo",
    "pilot", "pitch", "pixel", "place", "plain",
    "plant", "plate", "plead", "pluck", "poetry",
    "point", "polar", "pound", "power", "press",
    "price", "pride", "prime", "print", "prior",
    "prize", "proof", "pulse", "pupil", "quack",
    "queen", "query", "quest", "quick", "quiet",
    "quota", "radar", "ranch", "rapid", "ratio",
    "reach", "react", "realm", "rebel", "refer",
    "relax", "reply", "rival", "roast", "rough",
    "round", "royal", "rural", "salad", "scale",
    "scare", "scarf", "scene", "scoop", "scope",
    "score", "scout", "scrap", "sense", "serve",
    "shade", "shaft", "shard", "share", "sharp",
    "shift", "shine", "shirt", "shock", "shore",
    "short", "shout", "shrub", "sight", "siren",
    "skill", "skirt", "slate", "slice", "slope",
    "smart", "smoke", "snack", "snail", "snake",
    "sneak", "solar", "solid", "solve", "sound",
    "south", "space", "spare", "spark", "spear",
    "spice", "spike", "spine", "spoil", "sport",
    "spray", "squad", "stack", "stage", "stain",
    "stair", "stake", "stare", "steam", "steel",
    "steep", "stern", "stick", "stiff", "still",
    "sting", "stock", "stone", "store", "storm",
    "story", "straw", "strip", "stuck", "study",
    "style", "sugar", "sunny", "super", "swear",
    "sweep", "sweet", "swell", "swift", "swing",
    "table", "taste", "teach", "tease", "tempo",
    "thank", "theme", "thick", "thief", "thing",
    "think", "third", "thorn", "those", "three",
    "threw", "throw", "tiger", "tight", "toast",
    "today", "token", "topic", "torch", "total",
    "touch", "tower", "trace", "track", "trade",
    "trail", "train", "treat", "trend", "trial",
    "tribe", "trick", "tried", "trout", "truck",
    "truly", "trust", "truth", "twice", "twist",
    "uncle", "under", "union", "unite", "unity",
    "urban", "usage", "usual", "vague", "valid",
    "value", "vapor", "vault", "venue", "verse",
    "video", "vigor", "vinyl", "viral", "vital",
    "vivid", "voice", "voter", "wager", "wagon",
    "waist", "waltz", "watch", "water", "weary",
    "weird", "whale", "wheat", "wheel", "where",
    "which", "while", "whirl", "whisk", "white",
    "whole", "whose", "wider", "wince", "windy",
    "wiser", "witch", "woman", "world", "worry",
    "wound", "woven", "wrath", "wreck", "write",
    "wrong", "yeast", "young", "youth", "zebra",
    "zesty", "zonal"
]


word_list_four = [
    "rate","salt","mint","corn","wind","aero","easy","oath",
    "clay","drip","echo","fame","gaze","hush","iron","jolt","keen","loud",
    "moss","navy","opal","palm","quip","roam","soar","tide","ugly","vain",
    "wade","yarn","zest","brim","chop","dune","envy","flap","glow","haze",
    "idle","jazz","knot","lure","melt","numb","oval","perk","rift","sway",
    "able","acid","arch","bake","bald","band","bank","barn","bash","beam",
    "beef","belt","bend","best","bite","blip","blob","blur","boil","bolt",
    "bond","boom","boot","bore","born","both","bowl","buck","buff","bulk",
    "bull","bump","burn","buzz","cafe","calm","camp","card","care","cart",
    "case","cash","cast","cell","chap","chat","chef","chip","clap","clip",
    "club","coal","coat","code","coil","cold","comb","cook","cool","cope",
    "core","cork","cove","crew","crib","crop","cube","cure","curl","cute",
    "dare","dark","dash","dawn","deal","dear","deck","deep","deny","dial",
    "diet","dive","dock","doll","doom","door","dose","down","drag","draw",
    "drop","drum","duck","dull","duty","earn","edge","edit","else","epic",
    "even","ever","exit","face","fact","fair","fall","farm","fast","fear",
    "feed","feel","file","fill","film","find","fine","fire","firm","fish",
    "fist","flag","flat","flip","flow","fold","folk","fond","food","fool",
    "foot","form","foul","free","frog","fuel","full","fund","gain","game",
    "gate","gear","gift","girl","give","glad","grab","grid","grip","grow",
    "gulf","half","hall","hand","hang","hard","harm","harp","hate","heal",
    "heap","heat","help","herb","hero","hide","hill","hint","hire","hold",
    "hole","holy","home","hope","host","hour","huge","hunt","hurt","idea",
    "inch","into","join","jump","kick","kind","king","kiss","kite","knee",
    "lace","lack","lady","lake","lamp","land","lane","last","lazy","lead",
    "leaf","leak","lean","left","lend","lens","life","lift","like","limb",
    "line","link","lion","list","live","load","loan","lock","logo","long",
    "look","loop","lose","loss","love","luck","made","mail","main","make",
    "male","mall","many","mark","mass","mate","meal","mean","meet","mild",
    "mile","milk","mill","mind","mine","miss","mode","moon","more","most",
    "move","much","must","name","near","neck","need","nest","next","nice",
    "nick","nine","node","none","note","okay","once","only","open","pack",
    "page","pain","pair","park","part","pass","past","path","peak","peer",
    "pest","pick","pile","pill","pine","pink","pipe","plan","play","plug",
    "plus","poem","pole","poll","pool","port","pose","post","pour","pray",
    "pull","pure","push","quit","race","rail","rain","rank","rare","rate",
    "read","real","rear","rely","rent","rest","rice","rich","ride","ring",
    "rise","risk","road","rock","role","roll","roof","room","root","rope",
    "rose","rule","rush","safe","sail","sale","salt","sand","save","scan",
    "scar","seal","seat","seed","seek","seem","self","sell","send","sent",
    "ship","shop","shot","show","shut","side","sign","silk","sing","sink",
    "site","size","skin","slip","slow","snow","soap","soft","soil","sold",
    "solo","some","song","soon","sort","soul","spot","star","stay","step",
    "stop","such","suit","sure","swim","tall","tank","tape","task","team",
    "tear","tell","tend","tent","term","test","text","than","that","them",
    "then","they","thin","this","thus","till","time","tiny","told","toll",
    "tone","tool","tour","town","trap","tree","trip","true","tune","turn",
    "twin","type","unit","upon","urge","used","user","vast","very","view",
    "vote","wait","wake","walk","wall","want","warm","warn","wash","wave",
    "weak","wear","week","well","west","what","when","whip","wide","wild",
    "will","wind","wine","wing","wire","wise","wish","with","wood","word",
    "work","yard","year","yell","zero","zone"
]


word_list_six = [
    "planet","silver","branch","marble","candle","forest","gentle","harbor","jungle","kitten",
    "ladder","magnet","nectar","object","puzzle","quartz","rocket","saddle","tunnel","velvet",
    "wander","yellow","zephyr","anchor","butter","copper","dragon","ember","fabric","galaxy",
    "hammer","island","jester","keeper","laptop","market","notion","orange","pocket","quiver",
    "ribbon","shower","throne","unfold","vacuum","window","wonder","yogurt","zipper","bridge",
    "absorb","accent","admire","advice","agency","agenda","almost","amount","animal","answer",
    "anyone","appeal","artist","aspect","assign","assist","attack","author","backup","ballet",
    "banner","barrel","battle","beacon","become","behave","belief","belong","better","beyond",
    "bishop","blazer","blonde","breeze","bright","broken","broker","bubble","budget","bundle",
    "cactus","camera","campus","carbon","castle","casual","caught","center","chance","change",
    "charge","cheese","choice","choose","circle","client","clinic","closet","coffee","column",
    "combat","comedy","coming","common","comply","copper","corner","costly","county","couple",
    "course","coyote","create","credit","crisis","custom","damage","danger","debate","decade",
    "decide","defeat","defend","define","degree","demand","depend","design","detail","device",
    "dinner","direct","divide","doctor","dollar","domain","donate","double","dragon","drawer",
    "driver","editor","effect","effort","eighth","either","empire","enable","ending","energy",
    "engage","engine","enough","ensure","entire","escape","estate","ethics","evening","exceed",
    "except","expand","expect","expert","export","fabric","factor","fairly","family","famous",
    "farmer","faster","father","fellow","figure","filter","finger","finish","flight","flower",
    "follow","forest","forget","formal","format","former","fossil","foster","freeze","friend",
    "future","galaxy","garage","garden","gather","gender","gentle","global","golden","govern",
    "gravel","growth","handle","happen","harbor","hazard","health","heaven","height","helmet",
    "hidden","hockey","honest","honour","hunter","ignore","impact","import","income","injury",
    "inside","insist","invest","island","jacket","jungle","keeper","kernel","kidnap","kitten",
    "ladder","launch","lawyer","leader","league","legend","lesson","letter","likely","linear",
    "linger","liquid","listen","little","lively","locate","lonely","luxury","magnet","manage",
    "manner","manual","margin","market","marvel","master","matter","medium","member","memory",
    "mental","mentor","merely","method","middle","mighty","minute","mirror","mobile","modern",
    "modest","moment","monkey","mother","motion","mount","museum","muscle","mystic","native",
    "nature","nectar","needle","normal","notion","number","object","office","online","option",
    "orange","origin","outlet","oxygen","packet","palace","parade","parent","pastel","patrol",
    "people","pepper","period","permit","person","phrase","planet","plasma","player","pocket",
    "poetry","police","policy","prefer","pretty","prince","prison","profit","proper","public",
    "puzzle","quartz","quiver","rabbit","random","ranger","rarely","rather","rating","reader",
    "reason","rebel","record","reduce","refine","region","regret","relate","remain","remark",
    "repair","repeat","report","rescue","resist","result","retail","retire","return","reveal",
    "review","reward","ribbon","rocket","rubber","saddle","safety","salmon","sample","school",
    "screen","script","search","season","second","secret","sector","secure","select","seller",
    "senior","shadow","shaped","shower","signal","silent","silver","simple","singer","single",
    "sister","sketch","smooth","soccer","social","softly","source","speech","spirit","sponsor",
    "stable","staffs","staple","starry","status","steady","stereo","sticky","stoney","stream",
    "street","strike","string","strong","studio","submit","subtle","sudden","summer","sunset",
    "supply","survey","switch","symbol","system","tablet","talent","target","temple","tenant",
    "tender","theory","thirty","throat","ticket","timber","timely","tissue","tomato","tongue",
    "toward","travel","treaty","tunnel","turtle","unable","unfold","unique","update","upward",
    "useful","vacuum","valley","velvet","vendor","victim","victor","viewer","village","vision",
    "visual","volume","wander","wealth","weapon","weekly","weight","whisky","window","winner",
    "winter","wonder","wooden","worker","worthy","writer","yellow","yogurt","zephyr","zipper"
]



# ################################### TKINTER TESTING ###################################


root = tk.Tk()
root.title("Wordle 2.0")  # setting up inital window settings
window_width = 600
window_height = 800
root.attributes("-alpha", 1.0)
root.attributes('-topmost', 1)

root.iconbitmap('./assets/wordle.ico')  

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# cant resize window
root.resizable(False, False) # maybe change to true later



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





############################################################ GUESS CHECKER FUNCTION ###########################################################################
def disappearing_text(label, duration=1000):
    label.after(duration, label.destroy) # destroy label after duration

def check_guess(entry, target_word):
    global current_row
    global guesss
    guess = entry.get().lower().strip()
    entry.delete(0, tk.END) # clear entry after sumbit




    if not re.match(fr"^[a-zA-Z]{{{len(target_word)}}}$", guess): # regex - a-zA-Z = no dgits and length = target word length
        world_letter_invalid = tk.Label(
        screen3,
        text=f"Your guess must be {len(target_word)} letters (A–Z only)!",
        font=("Georgia", 15),
        fg="red",
        bg="#1B1A1A"
        )
        world_letter_invalid.place(relx=0.5, rely=0.775, anchor="center")
        disappearing_text(world_letter_invalid)
        return

    if zipf_frequency(guess, 'en') < 2.5: # check if real word in english
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
    tiles = [] # empty list to store tile labels (row)
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
    guess_entry = tk.Entry(board_frame, font=("Arial", 20), justify="center")
    guess_entry.grid(row=7, column=0, columnspan=word_length, pady=12)
    guess_entry.focus_set()


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


