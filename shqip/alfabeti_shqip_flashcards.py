### Alfabeti Shqip - Language Learning Flaschard Set

# %% [markdown]
# Developed by Alex Sessums
# August 2022

# %%
# Import Libraries
from tkinter import *
from random import randint

# Flashcard Formatting
root = Tk()
root.title("Alfabeti Shqip Flashcards")
root.geometry("800x500")

# %%
# Shqip Vocabulary List
words = [(("E hënë"), ("Monday")),
         (("E martë"), ("Tuesday")), 
         (("E merkurë"), ("Wednesday")), 
         (("E enjte"), ("Thursday")), 
         (("E premte"), ("Friday")),
         (("E shtunë"), ("Saturday")),
         (("E diel"), ("Sunday")),
         (("Pranverë"), ("Spring")),
         (("Verë"), ("Summer")),
         (("Vjesthe"), ("Autumn")),
         (("Dimër"), ("Winter")),
         (("Janar"), ("January")),
         (("Shkurt"), ("February")),
         (("Mars"), ("March")),
         (("Prill"), ("April")),
         (("Maj"), ("May")),
         (("Qershor"), ("June")),
         (("Korrik"), ("July")), 
         (("Gusht"), ("August")), 
         (("Shtator"), ("September")), 
         (("Tetor"), ("October")), 
         (("Nëntor"), ("November")), 
         (("Dhjetor"), ("December")), 
         (("Ditët"), ("Days")), 
         (("muajt"), ("Months")), 
         (("Stinët"), ("Seasons")), 
         (("Veshjet"), ("Clothing")), 
         (("Këmishë"), ("Shirt")), 
         (("Bluzë"), ("Blouse")),
         (("Pantallona"), ("Pants")),
         (("Fund"), ("Skirt")),
         (("Fustan"), ("Dress")),
         (("Pallto"), ("Coat")),
         (("Kollare"), ("Tie")),
         (("Çorape"), ("Socks")),
         (("Rrip"), ("Belt")),
         (("Këpuce"), ("Shoes")),
         (("Xhaketë"), ("Jacket")),
         (("Çizme"), ("Boots")),
         (("Shtëpi"), ("Home")),
         (("Dhomë"), ("Room")),
         (("Derë"), ("Door")),
         (("Dritare"), ("Window")),
         (("Kuzhinë"), ("Kitchen")),
         (("Dhomë Gjume"), ("Bedroom")),
         (("Tualet"), ("Toilet")),
         (("Dhomë Ngrënie"), ("Dining Room")),
         (("Televizor"), ("TV")),
         (("Divan"), ("Couch")),
         (("Kolltuk"), ("Armchair")),
         (("Frigorifer"), ("Fridge")),
         (("Tavolinë"), ("Table")),
         (("Tryezë"), ("Table")),
         (("Karrige"), ("Chair")),
         (("Çarçaf"), ("Sheet")),
         (("Batanije"), ("Blanket")),
         (("Jastëk"), ("Pillow")),
         (("Kush"), ("Who")),
         (("Çfare"), ("What")),
         (("Pse"), ("Why")),
         (("Ku"), ("Where")),
         (("Kur"), ("When")),
         (("Të Cilat"), ("Which")),
         (("Sa larg"), ("How far?")),
         (("Sa shumë"), ("How much?")),
         (("Sa është ora"), ("What time is it?")),
         (("Sa vjeç jeni"), ("How old are you?")),
         (("Nga jeni?"), ("Where are you from?")),
         (("Ndoshta"), ("Maybe")),
         (("Ju lutem"), ("Please")),
         
         ]

# %%
# Length of Words List
count = len(words)

# %%
# Define a function to create a random word
def next():
    global hinter, hint_count
    '''Clear the screen'''
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text = "")
    # Reset hint
    hinter = ""
    hint_count = 0
    
    '''Create a global variable as a random selection'''
    global random_word
    random_word = randint(0, count-1)
    '''Update the label with a Shqip word'''
    shqip_word.config(text=words[random_word][0])
    
# %%
# Define a function to return the answer
def answer():
    if my_entry.get().capitalize() == words[random_word][1]:
        answer_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][1]}")
    else:
        answer_label.config(text=f"Incorrect! {words[random_word][0]} is not {my_entry.get().capitalize()}")

# %%
# Define a function to give a hint
hinter = ""
hint_count = 0

def hint():
    global hint_count
    global hinter

    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_label.config(text = hinter)
        hint_count += 1

# %%
# Get a count of the word list
shqip_word = Label(root, text="", font=("TW Cen MT", 50))
shqip_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

info = StringVar()
my_entry = Entry(root, textvariable=info, font=("TW Cen MT", 35))
my_entry.pack(pady=20)
my_entry.get()

# str(EntryAnswer)
# EntryAnswer.pack(pady=20)

# %%
# Create Answer, Next & Hint Buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=1)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=2, padx=20)

# Create Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=40)

# %%
# Run next function when program starts
next()

# %%
# Loop through the program to keep it running
root.mainloop()