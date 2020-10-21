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
    # query = "SELECT * FROM student"
    # query = "SELECT COUNT(DISTINCT promotion_fk) FROM student"
    #query ="SELECT client, SUM(tarif) FROM achat GROUP BY client"
    query = "SELECT COUNT(id) FROM student GROUP BY promotion_fk"

    # getting records from the table
    cursor.execute(query)

    # fetching all records from the 'cursor' object
    records = cursor.fetchall()

    # Showing the data
    for record in records:
        print(record)


showUnit()
