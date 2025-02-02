from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint
import tkinter.font as tkFont
#import vocabulary
import alphabet
import nouns
import adjectives
import verbs
import verbs2
import pygame
import keyboardEng2Syriac
import random

root = Tk()
root.title('Chaldean flashcards')
root.geometry("550x600")  # Increased height to accommodate Pronounce button and dropdowns

# List of letters
# IMPORTANT: NEED TO TYPE STRINGS WITH FIRST LETTER CAPITALIZED
syriac_letters = nouns.syriac_letters

words = syriac_letters
# Get a count of the word list
count = len(words)

# Define custom fonts
syriac_font = tkFont.Font(family="East Syriac Adiabene", size=30)
english_font = tkFont.Font(family="Helvetica", size=18)

# Initialize mode
current_mode = "syriac_to_english"  # Default mode: question in Syriac, answer in English

def switch_mode():
    """Toggle between Syriac-to-English and English-to-Syriac modes."""
    global current_mode
    if current_mode == "syriac_to_english":
        current_mode = "english_to_syriac"
        mode_button.config(text="Switch to Syriac-to-English")
    else:
        current_mode = "syriac_to_english"
        mode_button.config(text="Switch to English-to-Syriac")
    next()  # Load a new word after switching modes

correct_words = []

def next():
    """Load the next flashcard."""
    global hinter, hint_count, correct_words

    # Stop any currently playing audio
    pygame.mixer.music.stop()

    # Clear the screen
    answer_label.config(text="")
    my_entry.delete(0, END)

    # Reset hint
    hint_label.config(text="")
    hinter = ""
    hint_count = 0

    # Create a random selection excluding correct words
    available_words = [i for i in range(count) if i not in correct_words]
    if not available_words:
        # All words have been answered correctly
        syriac_word.config(text="All words completed!", font=syriac_font)
        return

    # Create a random selection
    global random_word
    random_word = random.choice(available_words)

    # Update the question based on the current mode
    if current_mode == "syriac_to_english":
        syriac_word.config(text=words[random_word][0], font=syriac_font)
    else:
        syriac_word.config(text=words[random_word][1], font=english_font)

def mark_correct():
    """Mark the current word as answered correctly."""
    global correct_words
    if random_word not in correct_words:
        correct_words.append(random_word)

def answer():
    """Check the user's answer."""
    user_input = my_entry.get()
    try:
        user_input = user_input.encode('utf-8').decode('utf-8')  # Ensure the input is in UTF-8
    except UnicodeDecodeError as e:
        messagebox.showerror("Encoding Error", f"Error decoding input: {e}")
        return

    if current_mode == "syriac_to_english":
        correct_answer = words[random_word][1]
        answer_font = syriac_font
    else:
        correct_answer = words[random_word][0]
        answer_font = syriac_font

    if my_entry.get() == correct_answer:
        answer_label.config(text=f"Correct! {syriac_word.cget('text')} is {correct_answer}", font=answer_font)
    else:
        answer_label.config(text=f"Incorrect! {syriac_word.cget('text')} is NOT {my_entry.get()}",  font=answer_font)

hinter = ""
hint_count = 0
def hint():
    """Provide a hint for the current word."""
    global hint_count
    global hinter

    if current_mode == "syriac_to_english":
        hint_text = words[random_word][1]
        hint_font = english_font
    else:
        hint_text = words[random_word][0]
        hint_font = syriac_font

    if hint_count < len(hint_text):
        hinter += hint_text[hint_count]
        hint_label.config(text=hinter, font=hint_font)
        hint_count += 1

pygame.mixer.init()

def convert_to_seconds(time_str):
    """Convert time in MM:SS format to seconds."""
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def pronounce():
    """Play a specific segment of the pre-saved audio file."""
    try:
        #audio_file = words[random_word][2]  # Audio file path
        audio_file = f"audio/{words[random_word][2]}"  # Audio file path
        start_time_str = words[random_word][3]  # Start time in seconds
        end_time_str = words[random_word][4]  # End time in seconds

        # Convert MM:SS format to seconds
        start_time = convert_to_seconds(start_time_str)
        end_time = convert_to_seconds(end_time_str)

        # Load and play the audio file
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play(loops=0, start=start_time)

        # Schedule stop after the desired duration
        duration = (end_time - start_time) * 1000  # Convert to milliseconds
        root.after(duration, pygame.mixer.music.stop)

    except Exception as e:
        answer_label.config(text=f"Error playing audio: {e}")

key_map = keyboardEng2Syriac.key_map

def do_key(event):
    if current_mode == "english_to_syriac":
        # Check for Shift key
        if event.state & 0x1:  # Shift key is pressed
            key = f'Shift-{event.keysym.lower()}'
        # Check for Alt key
        elif event.state & 0x20000:  # Alt key is pressed
            key = f'Alt-{event.keysym.lower()}'
        else:
            key = event.char

        char = key_map.get(key)
        if char:
            my_entry.insert(INSERT, char)
            return 'break'
    else:
        return None

def update_words():
    """Update the words variable based on user selection."""
    global words, count
    selected_category = category_var.get()
    selected_subcategories = [var.get() for var in subcategory_vars if var.get()]

    if selected_category == "Vocabulary":
        words = []
        if "Nouns" in selected_subcategories:
            words.extend(nouns.syriac_letters)
        if "Adjectives" in selected_subcategories:
            words.extend(adjectives.syriac_letters)
        if "Verbs" in selected_subcategories:
            words.extend(verbs.syriac_letters)
        if "Pronouns" in selected_subcategories:
            words.extend(vocabulary.syriac_letters)  # Assuming pronouns are in vocabulary.py
    elif selected_category == "Conjugations":
        # Implement logic for conjugations
        pass

    count = len(words)
    next()  # Load the first word after updating

# Create the mode toggle button at the top
mode_button = Button(root, text="Switch to English-to-Syriac", command=switch_mode)
mode_button.pack(pady=10)

# Create the category dropdown menu
category_var = StringVar(value="Vocabulary")
category_menu = ttk.Combobox(root, textvariable=category_var, values=["Vocabulary", "Conjugations"])
category_menu.pack(pady=10)
category_menu.bind("<<ComboboxSelected>>", lambda e: update_words())

# Create subcategory checkboxes
subcategory_vars = [StringVar(value="Nouns"), StringVar(value="Adjectives"), StringVar(value="Verbs"), StringVar(value="Pronouns")]
subcategory_frame = Frame(root)
subcategory_frame.pack(pady=10)
for var in subcategory_vars:
    Checkbutton(subcategory_frame, text=var.get(), variable=var, onvalue=var.get(), offvalue="").pack(side=LEFT)

# Create the question label
syriac_word = Label(root, text="", font=syriac_font)
syriac_word.pack(pady=20)

# Create the answer label
answer_label = Label(root, text="")
answer_label.pack(pady=10)

# Create the entry box with a Syriac-compatible font
my_entry = Entry(root, font=("East Syriac Adiabene", 18))
my_entry.pack(pady=20)
my_entry.bind('<KeyPress>', do_key)

# Create buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=2, padx=20)

pronounce_button = Button(button_frame, text="Pronounce", command=pronounce)
pronounce_button.grid(row=0, column=3, padx=20)

# Create the hint label below the buttons
hint_label = Label(root, text="")
hint_label.pack(pady=20)

# Run next function when program starts
next()

root.mainloop()