# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
REPLACE_TEXT = '[name]'
with open('./Input/Letters/starting_letter.txt', mode='r') as letter:
    whole_text = letter.read()
with open('./Input/Names/invited_names.txt', mode='r') as names:
    inv_name = names.readlines()
    new_inv_name = []
    for inv in inv_name:
        new_inv_name.append(inv.strip('\n'))

    for inv_p in new_inv_name:
        new_text = whole_text.replace(REPLACE_TEXT, inv_p)
        with open(f'./Output/ReadyToSend/letter_for_{inv_p}.txt', mode='w') as send_letter:
            send_letter.write(new_text)


