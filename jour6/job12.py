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


def showjobsbyunit(nom):

    query = "SELECT job_fk FROM registration WHERE registration.group_id = %s"
    nom = (nom, )

    # getting records from the table
    cursor.execute(query, nom)

    # fetching all records from the 'cursor' object
    records = cursor.fetchall()
    print(records)
    chifre = 0
    liste = []
    for record in records:
        chifre = int(record[0])
        liste.append(chifre)
    print(liste)

    # Showing the data
    query1 = "SELECT job.name, unit.name FROM job LEFT JOIN unit ON job.id = unit.id WHERE job.id = %s"
    # query2 = "SELECT name FROM job LEFT JOIN unit ON Livre.idAuteur= Auteur.idAuteur WHERE (%s, %s)"
    chifre = (chifre, )
    # getting records from the table
    cursor.execute(query1, chifre)
    # fetching all records from the 'cursor' object
    records = cursor.fetchall()
    for record in records:
        print(record)


nom = input("Etrer group_id de registration: ")
showjobsbyunit(nom)
