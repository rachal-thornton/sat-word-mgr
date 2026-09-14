# Author: Rachal Thornton
# Class: CS 410
# Date: 14 September 2026
# Desc: This program contains the functions needed to handle words in the words.dat file.

# Create an empty dictionary to store words
words = {}

# FUNCTIONS
# load_words: read file 'words.dat' and split word parts into Python dictionary
# Pre: 'words' dictionary and 'words.dat' file exist
# Post: a Python dicitonary named 'words' is initialized
def load_words():
    # Open and read file
    try:
        with open("words.dat", "r") as file:
            # For each line in file, split each word into a max of 3 parts (word, type, desc.)
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
                else:
                    print("File is not structured correctly.")
        return words
    # Exception handling
    except FileNotFoundError:
        print("Error: The specified file could not be found.")
    except Exception as err:
        print(f"An unexpected error occured: {err}")


# save_words: write from the 'words' dictionary to the 'words.dat file'
# Pre: 'words' dictionary and 'words.dat' file exist
# Post: user-entered words are saved to the 'words.dat' file
def save_words():
    try:
        with open("words.dat", "w") as file:
            for word, info in words.items():
                file.write(
                    f"{word} "
                    f"{info['word_type']} "
                    f"{info['definition']}\n"
                )
    # Exception handling
    except FileNotFoundError:
        print("Error: The specified file could not be found.")
    except Exception as err:
        print(f"An unexpected error occured: {err}")

