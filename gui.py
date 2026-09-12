# Author: Rachal Thornton
# Class: CS 410
# Date: 14 September 2026
# Desc: This program contains the framework for a GUI for the SAT Word Program using Tkinter.

# Imports
import tkinter as tk

# Constants
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 3
BUTTON_PADDING = 5

# Functions
# Open a new window to handle the GUI for adding a new word to the list
def open_addWord_window():
    # Opening and setting up the new window
    new_window = tk.Toplevel(root)
    new_window.title("Add Word")

    # Prompt for new word
    word_prompt = tk.Label(new_window, text="New Word:")
    word_prompt.grid(row=0, column=0)

    # Entry to type new word
    word_entry = tk.Entry(new_window)
    word_entry.grid(row=0, column=1)

    # Prompt for word type
    type_prompt = tk.Label(new_window, text="Word Type:")
    type_prompt.grid(row=1, column=0)

    # Radiobutton to choose word type
    type_choice = tk.IntVar()
    verb_button = tk.Radiobutton(new_window, text="verb", variable=type_choice, value=1)
    verb_button.grid(row=1, column=1)
    noun_button = tk.Radiobutton(new_window, text="noun", variable=type_choice, value=2)
    noun_button.grid(row=1, column=2)
    adj_button = tk.Radiobutton(new_window, text="adjective", variable=type_choice, value=3)
    adj_button.grid(row=1, column=3)

    # Prompt for definition of word
    def_prompt = tk.Label(new_window, text="Word Definition:")
    def_prompt.grid(row=2, column=0)

    # Text field to type definition of word
    def_text = tk.Text(new_window, height=5, width=50, wrap="word")
    def_text.grid(row=2, column=1)

# Open a new window to handle the GUI for checking meaning of word
def open_checkMeaning_window():
    # Opening and setting up the new window
    new_window = tk.Toplevel(root)
    new_window.title("Check Meaning")


# Create application window and name it
root = tk.Tk()
root.title("SAT Word Program")

# Widgets
# Program name
label = tk.Label(root, text="SAT Word Program")
label.pack()

# Buttons
# Add word button opens new window to add a new word
addWord = tk.Button(root, text="Add Word", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=open_addWord_window)

# Check meaning button opens a new window to see all words, or search for a specific word
checkMeaning = tk.Button(root, text="Check Meaning", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=open_checkMeaning_window)
# Safe words button to save the word list into the words.dat file
saveWords = tk.Button(root, text="Save Word List", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
# Quit button to close program
quit = tk.Button(root, text="Quit", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=root.destroy)

# Pack buttons vertically 
addWord.pack(pady=BUTTON_PADDING)
checkMeaning.pack(pady=BUTTON_PADDING)
saveWords.pack(pady=BUTTON_PADDING)
quit.pack(pady=BUTTON_PADDING)


# Start event loop and keep window responsive
root.mainloop()