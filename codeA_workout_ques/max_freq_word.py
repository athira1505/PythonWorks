
# Write a Python program that reads a block of text and identifies the most
# frequently occurring word in that text. If there are multiple words with the same
# maximum frequency,return any one of them.
# Requirements:
# The program should ignore case sensitivity (i.e., "Word" and "word" are
# considered the same).
# Punctuation should be ignored.
# Function Signature: def most_frequent_word(text: str) -> str:
# Input: A string text containing the text to analyze.
# Output: The most frequently occurring word in the text
# text = "Hello world! Hello everyone. Welcome to the world."
# most_frequent_word(text) # should return "hello" or "world"



text = "Hello world! Hello everyone. Welcome to the world."
words=text.split(" ")


def most_frequent_word(w):
    return words.count(w)
freq_word=max(words,key=most_frequent_word)
print(freq_word)
