# Faites un programme qui demande à l’utilisateur d’entrer un nom de ‘job’ et qui affiche le nom de ce ‘job’ ainsi que le ‘nom’ de la ‘unit’ qui lui est associée.
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


def showunitsbystudent(nom):

    # query = "SELECT * FROM Livre INNER JOIN Auteur ON Livre.idAuteur= Auteur.idAuteur WHERE (%s, %s)"
    # query = "SELECT current_unit_fk FROM student LEFT JOIN unit ON student.current_unit_fk = unit.id WHERE student.id = %s"

    query = "SELECT current_unit_fk FROM student WHERE student.id = %s"
    nom = (nom, )

    # getting records from the table
    cursor.execute(query, nom)

    # fetching all records from the 'cursor' object
    records = cursor.fetchall()

    chifre = 0
    for record in records:
        chifre = int(record[0])

    # Showing the data
    query1 = "SELECT name FROM unit WHERE unit.id = %s"
    chifre = (chifre, )
    # getting records from the table
    cursor.execute(query1, chifre)
    # fetching all records from the 'cursor' object
    records = cursor.fetchall()
    for record in records:
        print(record)


nom = input("Etrer id de student: ")
showunitsbystudent(nom)
