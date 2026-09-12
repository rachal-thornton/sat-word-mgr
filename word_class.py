# Author: Rachal Thornton
# Class: CS 410
# Date: 14 September 2026
# Desc: This program contains the class information of a word.

# Imports
from enum import Enum

# WordType(Enum) class to enforce words being only accepted types
class WordType(Enum):
    VERB = "verb"
    NOUN = "noun"
    ADJECTIVE = "adjective"

# Word class to define the aspects of a word
class Word:
    # Constructor method for a Word object
    # Pre: none
    # Post: a word object is initialized
    def __init__(self, word: str, desc: str, type:WordType):
        self.word = word
        self.desc = desc
        self.type = type

        # Raise exception if WordType is not in enum list
        if not isinstance(type, WordType):
            raise TypeError(f"Expected a WordType enum, instead got {type}")

    # Printable representation of a Word object
    # Pre: the passed in word object exists and is initialized
    # Post: print statement to screen with word name, desc, and type
    def __repr__(self):
        return (f"{self.word}\t{self.type.value}\t{self.desc}")