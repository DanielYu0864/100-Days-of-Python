# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# TODO 3. Add error handler to make user input only alphabet.

def generate_phonetice():
    word = input("Enter a word: ").upper()
    if len(word) > 0:
        try:
            output_list = [phonetic_dict[letter] for letter in word]
        except KeyError:
            print('Sorry, only letters in the alphabet please.')
            generate_phonetice()
        else:
            print(output_list)
            return
    else:
        generate_phonetice()


generate_phonetice()
