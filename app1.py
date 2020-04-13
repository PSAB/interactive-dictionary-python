import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    if w in data: # In case exact word w/ caps is found
        return data[w] 
    w = w.lower()
    if w in data: # If all lowercase word is found
        return data[w] 
    elif len(get_close_matches(w, data.keys())) > 0: # Otherwise present close predictions
        response = input('Did you mean {} instead? Y or N \n'.format(get_close_matches(w, data.keys())[0])) # Suggest the closest-matching word to user's word
        if response == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif response == 'N':
            return "The word doesn't exist. Please double-check it."
        else:
            return "Invalid Input. Please try again."
    else:
        return "The word doesn't exist. Please double-check it."



word = input("Enter Word: " ) # Retrieve lookup word from user

output = translate(word)  # display translate result from translate() function
if type(output) == list:
    for item in output:
        print(item)
else:               # If the word doesn't exist, just print the not-found string
    print(output)