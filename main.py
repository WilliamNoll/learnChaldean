from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint
import tkinter.font as tkFont
#import vocabulary
import alphabet
import pygame
import keyboardEng2Syriac
import random

from chaldeanGrammar import (
    pronouns, prepositions, verbs2, verbs, adjectives, nouns
)
# Import Introductory Chaldean modules
from introductoryChaldean import (
    greetings, family, garden, church, directions, calendar,
    weekdays, sacraments, outdoors, seasons, months, weather,
    colors, town, school, time, food, feelings, animals
)

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
current_book = "Chaldean Grammar"  # Default book

# Define book categories and their subcategories
book_categories = {
    "Chaldean Grammar": {
        "Vocabulary": ["Nouns", "Adjectives", "Verbs", "Pronouns", "Prepositions", "Subject Verb Pairs"],
        "Conjugations": []  # Add conjugation categories if needed
    },
    "Introductory Chaldean": {
        "Basic Vocabulary": ["Greetings", "Family", "Garden", "Church", "Directions", "Calendar", 
                           "Weekdays", "Sacraments", "Outdoors", "Seasons", "Months", "Weather",
                           "Colors", "Town", "School", "Time", "Food", "Feelings", "Animals"],
        "Common Phrases": ["Greetings", "Directions", "Time", "Weather"]
    }
}

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

def update_book_categories(*args):
    """Update the category dropdown based on the selected book."""
    selected_book = book_var.get()
    category_menu['values'] = list(book_categories[selected_book].keys())
    category_var.set(list(book_categories[selected_book].keys())[0])
    update_subcategories()
    update_words()

def update_subcategories(*args):
    """Update the subcategory checkboxes based on the selected book and category."""
    selected_book = book_var.get()
    selected_category = category_var.get()
    
    # Clear existing subcategory checkboxes
    for widget in subcategory_frame.winfo_children():
        widget.destroy()
    
    # Create a canvas with scrollbar for vertical scrolling
    canvas = Canvas(subcategory_frame)
    scrollbar = ttk.Scrollbar(subcategory_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create new subcategory checkboxes in columns
    subcategory_vars.clear()
    items_per_column = 5
    current_column = 0
    current_row = 0
    
    for subcategory in book_categories[selected_book][selected_category]:
        var = StringVar(value=subcategory)
        subcategory_vars.append(var)
        cb = Checkbutton(scrollable_frame, text=subcategory, variable=var,
                        onvalue=subcategory, offvalue="")
        cb.grid(row=current_row, column=current_column, sticky="w", padx=5, pady=2)
        
        current_row += 1
        if current_row >= items_per_column:
            current_row = 0
            current_column += 1
        
        var.trace_add("write", update_words)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def update_words(*args):
    """Update the words variable based on user selection."""
    global words, count
    selected_book = book_var.get()
    selected_category = category_var.get()
    selected_subcategories = [var.get() for var in subcategory_vars if var.get()]

    words = []
    
    if selected_book == "Chaldean Grammar":
        if selected_category == "Vocabulary":
            if "Nouns" in selected_subcategories:
                words.extend(nouns.syriac_letters)
            if "Adjectives" in selected_subcategories:
                words.extend(adjectives.syriac_letters)
            if "Verbs" in selected_subcategories:
                words.extend(verbs.syriac_letters)
            if "Pronouns" in selected_subcategories:
                words.extend(pronouns.syriac_letters)
            if "Prepositions" in selected_subcategories:
                words.extend(prepositions.syriac_letters)
            if "Subject Verb Pairs" in selected_subcategories:
                words.extend(verbs2.syriac_letters)
    else:  # Introductory Chaldean
        if selected_category == "Basic Vocabulary":
            if "Greetings" in selected_subcategories:
                words.extend(greetings.syriac_letters)
            if "Family" in selected_subcategories:
                words.extend(family.syriac_letters)
            if "Garden" in selected_subcategories:
                words.extend(garden.syriac_letters)
            if "Church" in selected_subcategories:
                words.extend(church.syriac_letters)
            if "Directions" in selected_subcategories:
                words.extend(directions.syriac_letters)
            if "Calendar" in selected_subcategories:
                words.extend(calendar.syriac_letters)
            if "Weekdays" in selected_subcategories:
                words.extend(weekdays.syriac_letters)
            if "Sacraments" in selected_subcategories:
                words.extend(sacraments.syriac_letters)
            if "Outdoors" in selected_subcategories:
                words.extend(outdoors.syriac_letters)
            if "Seasons" in selected_subcategories:
                words.extend(seasons.syriac_letters)
            if "Months" in selected_subcategories:
                words.extend(months.syriac_letters)
            if "Weather" in selected_subcategories:
                words.extend(weather.syriac_letters)
            if "Colors" in selected_subcategories:
                words.extend(colors.syriac_letters)
            if "Town" in selected_subcategories:
                words.extend(town.syriac_letters)
            if "School" in selected_subcategories:
                words.extend(school.syriac_letters)
            if "Time" in selected_subcategories:
                words.extend(time.syriac_letters)
            if "Food" in selected_subcategories:
                words.extend(food.syriac_letters)
            if "Feelings" in selected_subcategories:
                words.extend(feelings.syriac_letters)
            if "Animals" in selected_subcategories:
                words.extend(animals.syriac_letters)
        elif selected_category == "Common Phrases":
            # Common phrases can be combinations of different categories
            if "Greetings" in selected_subcategories:
                words.extend(greetings.syriac_letters)
            if "Directions" in selected_subcategories:
                words.extend(directions.syriac_letters)
            if "Time" in selected_subcategories:
                words.extend(time.syriac_letters)
            if "Weather" in selected_subcategories:
                words.extend(weather.syriac_letters)

    count = len(words)
    next()  # Load the first word after updating

# Create the book selection dropdown at the top
book_var = StringVar(value="Chaldean Grammar")
book_menu = ttk.Combobox(root, textvariable=book_var, 
                        values=list(book_categories.keys()))
book_menu.pack(pady=10)
book_menu.bind("<<ComboboxSelected>>", update_book_categories)

# Create the mode toggle button
mode_button = Button(root, text="Switch to English-to-Syriac", command=switch_mode)
mode_button.pack(pady=10)

# Create the category dropdown menu
category_var = StringVar(value="Vocabulary")
category_menu = ttk.Combobox(root, textvariable=category_var, 
                            values=list(book_categories["Chaldean Grammar"].keys()))
category_menu.pack(pady=10)
category_menu.bind("<<ComboboxSelected>>", update_subcategories)

# Initialize subcategory variables and frame
subcategory_vars = []
subcategory_frame = Frame(root)
subcategory_frame.pack(pady=10)

# Initialize the subcategories for the default book and category
update_subcategories()

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
        
        if user_input == correct_answer:
            answer_label.config(text=f"Correct! {syriac_word.cget('text')} is {correct_answer}", font=answer_font)
        else:
            answer_label.config(text=f"Incorrect! {syriac_word.cget('text')} is NOT {user_input}", font=answer_font)
    else:
        correct_answer = words[random_word][0]
        answer_font = syriac_font
        if user_input == correct_answer:
            answer_label.config(text=f"Correct! {correct_answer} is {syriac_word.cget('text')}", font=answer_font)
        else:
            answer_label.config(text=f"Incorrect! {user_input} is NOT {syriac_word.cget('text')}", font=answer_font)

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

# Special character combinations:
# Shift+J: Elongates a letter
# Shift+J: Produces a ̮ symbol
# Right Alt+U: Produces a syame silencer
# Taw + Yoth / Taw + Alap + heh-yodh combination creates a new symbol

root.mainloop()
