# Author: Rachal Thornton
# Class: CS 410
# Date: 14 September 2026
# Desc: This program manages a SAT word list in a GUI-based display.

# IMPORTS
import tkinter as tk
import word
import gui

# Load words.dat
word.load_words()

# Open the program window
root = tk.Tk()
root.title("SAT Word Program")

# BUTTONS
add_button = tk.Button(root, text="Add New Word", command=gui.add_word)
check_button = tk.Button(root, text="Check Meaning", command=gui.check_meaning)
save_button = tk.Button(root, text="Save Word List", command=word.save_words)
quit_button = tk.Button(root, text="Quit", command=root.destroy)

# Pack buttons
add_button.pack(pady=5)
check_button.pack(pady=5)
save_button.pack(pady=5)
quit_button.pack(pady=5)

root.mainloop()