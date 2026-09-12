# Author: Rachal Thornton
# Class: CS 410
# Date: 14 September 2026
# Desc: This program manages a SAT word list in a GUI-based display.

# Imports
import word
# import gui

# Test Code
words = word.load_words("words.dat")
# Just the words
for word in words:
    print(word)
# All word info
for word, info in words.items():
    print(f"Word: {word}")
    print(f"Type: {info["word_type"]}")
    print(f"Definition: {info["definition"]}")