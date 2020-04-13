import mysql.connector
from collections import defaultdict
from difflib import get_close_matches

# Remote sql setup
con = mysql.connector.connect (
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)

# Cursor used to navigate DB table:
cursor = con.cursor()

# query DB
cursor.execute("SELECT * FROM Dictionary ") # Expression, Definition
results = cursor.fetchall()
res_expressions = [x[0] for x in results]

# dictionary forming
data = defaultdict(list)
for expr, definition in results:
    data[expr].append(definition)


# 'Dictionary' translate function
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



# print(expression_list)
# print(res_expressions)
# print(len(results_dict))

# if results:
#     for result in results:
#         print(result)
# else:
#     print('word not found')