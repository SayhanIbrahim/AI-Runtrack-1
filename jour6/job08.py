import mysql.connector as mysql

# connecting to the database using 'connect()' method
# it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="dbms",
    database="laplateforme"
)
cursor = db.cursor()


def showUnit():
    query = "SELECT name FROM unit WHERE name LIKE '%Pool%'"

    # getting records from the table
    cursor.execute(query)

    # fetching all records from the 'cursor' object
    records = cursor.fetchall()

    # Showing the data
    for record in records:
        print(record)


showUnit()
