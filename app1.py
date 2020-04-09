import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    if w in data:
        return data[w]
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        response = input('Did you mean {} instead? Y or N \n'.format(get_close_matches(w, data.keys())[0]))
        if response == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif response == 'N':
            return "The word doesn't exist. Please double-check it."
        else:
            return "Invalid Input. Please try again."
    else:
        return "The word doesn't exist. Please double-check it."

word = input("Enter Word: " )

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)