# Author: Rachal Thornton
# Class: CS 410
# Date: 14 September 2026
# Desc: This program manages a SAT word list in a GUI-based display.

# Imports
import word_class
import gui

# Test Code
word1 = word_class.Word("test", "an example", word_class.WordType.NOUN)
print(word1.__repr__())
word2 = word_class.Word("test", "an example", word_class.WordType.VERB)
print(word2.__repr__())