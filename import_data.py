# save this as app.py
import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS F1")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS F1.Piloti (
    Nome VARCHAR(30) ,
    Cognome VARCHAR(30) ,
    Étà INTEGER,
    N°pilota INTEGER,
    ScuderiaF1 VARCHAR(30),
    PRIMARY KEY (Nome)
 );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM F1.Piloti")
mydb.commit()

#Read data from a csv file
f1_data = pd.read_csv('./Tabella1.csv', index_col=False, delimiter = ',')
f1_data = f1_data.fillna('Null')
print(f1_data.head(20))

#Fill the table
for i,row in f1_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO F1.Piloti VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM F1.Piloti")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)