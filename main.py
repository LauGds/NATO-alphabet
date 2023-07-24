# import pandas
#
# #TODO 1. Create a dictionary in this format:
# # {"A": "Alfa", "B": "Bravo"}
#
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#
# word = input("Enter a word: ").upper()
# phonetic_list = [new_dict[letter] for letter in word]
# print(phonetic_list)


import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
is_on = True
while is_on:
    word = input("Enter a word: ").upper()
    try:
        phonetic_list = [new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
    else:
        print(phonetic_list)
        is_on = False


