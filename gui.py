# Author: Rachal Thornton
# Class: CS 410
# Date: 14 September 2026
# Desc: This program contains the functions needed in a GUI for the SAT Word Program using Tkinter.

# IMPORTS
import tkinter as tk
import word

# FUNCTIONS
# add_word: Opens a new window for the user to imput information on a new word
# Pre: none
# Post: saves new word information to the words dictionary
def add_word():
    # Open new window
    word_window = tk.Toplevel()
    word_window.title("Add New Word")

    # Prompt for word
    tk.Label(word_window, text="Word: ").grid(row=0, column=0)
    word_entry = tk.Entry(word_window)
    word_entry.grid(row=0, column=1)

    # Prompt for word type
    tk.Label(word_window, text="Word Type: ").grid(row=1, column=0)
    # String variable to hold selected value
    selected_type = tk.StringVar()
    # Radio buttons
    radio_noun = tk.Radiobutton(word_window, text="Noun", variable=selected_type, value="n")
    radio_noun.grid(row=1, column=1)
    radio_verb = tk.Radiobutton(word_window, text="Verb", variable=selected_type, value="v")
    radio_verb.grid(row=1, column=2)
    radio_adj = tk.Radiobutton(word_window, text="Adjective", variable=selected_type, value="a")
    radio_adj.grid(row=1, column=3)

    # Prompt for definition
    tk.Label(word_window, text="Definition: ").grid(row=2, column=0)
    definition_entry = tk.Text(word_window, height=5, width=40)
    definition_entry.grid(row=2, column=1)

    # submit: gets the information the user added to the GUI
    # Pre: all entries are filled out
    # Post: adds the word to the words dictionary
    def submit():
        # Get information user entered
        user_word = word_entry.get().strip().lower()
        word_type = selected_type.get()
        definition = definition_entry.get("1.0", tk.END).strip()

        # Add word info to word dictionary
        word.words[user_word] = {
        "word_type": word_type,
        "definition": definition
    }
        # Close window after submitting
        word_window.destroy()

    # Submit button
    submit_button = tk.Button(word_window, text="Submit", command=submit)
    submit_button.grid(row=3, column=0)

# check_meaning:
# Pre:
# Post:
def check_meaning():
    # Open new window
    search_window = tk.Toplevel()
    search_window.title("Check Meaning")

    # Search for word
    tk.Label(search_window, text="Type in a word to search for: ").pack()
    search_entry = tk.Entry(search_window)
    search_entry.pack()

    # search: 
    # Pre: User typed word in search bar
    # Post: Display word info or error
    def search():
        user_word = search_entry.get().strip().lower()

        # Check if user-searched word is in word dictionary
        if user_word in word.words:
            entry = word.words[user_word]
            # Clear display
            display.delete("1.0", tk.END)
            # Insert all parts of the word
            display.insert(
                tk.END, 
                f"Word: {user_word}\n"
                )
            display.insert(
                tk.END,
                f"Word Type: {entry['word_type']}\n"
            )
            display.insert(
                tk.END,
                f"Definition: {entry['definition']}\n"
            )
        else:
            display.delete("1.0", tk.END)
            display.insert(
                tk.END,
                f"'{user_word}' was not found in the word list."
            )

    search_button = tk.Button(search_window, text="Search", command=search)
    search_button.pack()

    display = tk.Text(search_window, height=10, width=50)
    display.pack()

