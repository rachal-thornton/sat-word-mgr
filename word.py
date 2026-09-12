# Author: Rachal Thornton
# Class: CS 410
# Date: 14 September 2026
# Desc: This program contains the functions needed to handle words in the words.dat file.

# FUNCTIONS
# load_words: take a file in and seperate parts into words in a Python dictionary 
# Pre: file name is provided with corrent format needed
# Post: a Python dicitonary named 'words' is created
def load_words(filename):
    # Create an empty dictionary to store words
    words = {}

    # Open and read file
    with open(filename, "r") as file:
        # For each line in file, split each word into a max of 3 parts
        for line in file:
            parts = line.strip().split(maxsplit=2)

            # Assign each part of the word to its associated variable
            if len(parts) == 3:
                word = parts[0].lower()
                word_type = parts[1]
                definition = parts[2]

                # Define the framework for a nested dictionary to include word type and definition for a word
                words[word] = {
                    "word_type": word_type,
                    "definition": definition
                }
    return words
