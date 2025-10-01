#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
input_sentence = input("Enter a sentence: ")
# 2. Split the sentence
punctuations = ".?!,;:-'"
for char in punctuations:
    input_sentence = input_sentence.replace(char, "")

splitted_words = input_sentence.split(' ')
# 3. Create lists to store words and their corresponding frequencies.
stored_words = []
frequency = []
# 4. Iterate through words and update frequencies

for word in splitted_words:
    word = word.lower()
    if word in stored_words:
        frequency_index = stored_words.index(word)
        frequency[frequency_index] += 1
    else:
        frequency.append(1)
        stored_words.append(word)

for i in range(len(stored_words)):
    print(f"{stored_words[i]}: {frequency[i]}")



import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_input = input("Enter a sentence: ")
    
