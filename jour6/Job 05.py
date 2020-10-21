# importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

# connecting to the database using 'connect()' method
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="dbms",
    database="runtrack1"
)
cursor = db.cursor()


def showLivresbyAuthor(nom):
    # query = "SELECT * FROM Livre INNER JOIN Auteur ON Livre.idAuteur= Auteur.idAuteur WHERE (%s, %s)"

    query = "SELECT idAuteur FROM auteur WHERE auteur.nom = %s"
    nom = (nom, )

    # getting records from the table
    cursor.execute(query, nom)

    # fetching all records from the 'cursor' object
    records = cursor.fetchall()
    chifre = 0
    for record in records:
        chifre = int(record[0])

    # Showing the data
    query1 = "SELECT titre, idLivre FROM livre WHERE livre.idAuteur = %s"
    chifre = (chifre, )
    # getting records from the table
    cursor.execute(query1, chifre)
    # fetching all records from the 'cursor' object
    records = cursor.fetchall()
    for record in records:
        print(record)


nom = input("Etrer nom de auteur: ")
showLivresbyAuthor(nom)
