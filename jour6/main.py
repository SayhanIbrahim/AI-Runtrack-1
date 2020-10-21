# Connecting to the database

# importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

# connecting to the database using 'connect()' method
# it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="dbms",
    database="runtrack1"
)
cursor = db.cursor()


def printdb():
    print(db)  # it will print a connection object if everything is fine

    # executing the statement using 'execute()' method
    cursor.execute("SHOW DATABASES")

    # 'fetchall()' method fetches all the rows from the last executed statement
    databases = cursor.fetchall()  # it returns a list of all databases present

    # printing the list of databases
    print(databases)

    # showing one by one database
    for database in databases:
        print(database)


def insertAuteur():
    # defining the Query
    query = "INSERT INTO auteur (nom, prenom) VALUES (%s, %s)"
    # storing values in a variable
    values = ("NomAuteur5", "PrenomAuteur5")

    # executing the query with values
    cursor.execute(query, values)

    # to make final output we have to run the 'commit()' method of the database object
    db.commit()

    print(cursor.rowcount, "record inserted")


def insertLivre():
    # defining the Query
    query = "INSERT INTO livre (titre, idAuteur) VALUES (%s, %s)"
    # storing values in a variable
    values = ("livre3", "5")

    # executing the query with values
    cursor.execute(query, values)

    # to make final output we have to run the 'commit()' method of the database object
    db.commit()

    print(cursor.rowcount, "record inserted")


def showAuteurs():
    query = "SELECT * FROM auteur"

    # getting records from the table
    cursor.execute(query)

    # fetching all records from the 'cursor' object
    records = cursor.fetchall()

    # Showing the data
    for record in records:
        print(record)


def showLivres():
    query = "SELECT * FROM livre"

    # getting records from the table
    cursor.execute(query)

    # fetching all records from the 'cursor' object
    records = cursor.fetchall()

    # Showing the data
    for record in records:
        print(record)


def deleteAuteur():

    # defining the Query
    query = "DELETE FROM auteur WHERE idAuteur = 6"

    # executing the query
    cursor.execute(query)

    # final step to tell the database that we have changed the table data
    db.commit()
    print(cursor.rowcount, "record deleted")


def deleteLivre():

    # defining the Query
    query = "DELETE FROM livre WHERE idlivre = 5"

    # executing the query
    cursor.execute(query)

    # final step to tell the database that we have changed the table data
    db.commit()
    print(cursor.rowcount, "record deleted")


def showLivresbyAuthor():
    query = "SELECT * FROM Auteur INNER JOIN Livre ON Auteur.idAuteur = Livre.idAuteur"

    # getting records from the table
    cursor.execute(query)

    # fetching all records from the 'cursor' object
    records = cursor.fetchall()

    # Showing the data
    for record in records:
        print(record)


printdb()
# insertAuteur()
# insertLivre()
# deleteAuteur()
# deleteLivre()
# showAuteurs()
# showLivres()
# showLivresbyAuthor()
