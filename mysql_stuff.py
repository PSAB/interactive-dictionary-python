import mysql.connector

con = mysql.connector.connect (
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)

# Cursor used to navigate DB table:
cursor = con.cursor()

# query DB
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'line' ") # Expression, Definition
results = cursor.fetchall()

if results:
    for result in results:
        print(result)
else:
    print('word not found')