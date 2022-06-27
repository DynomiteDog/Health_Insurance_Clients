!pip install pandas-datareader -q

import requests 				# data from api
import sqlite3 					# provides python with a library for sqlite
import pandas as pd

df = pd.read_csv('https://www.ishelp.info/data/insurance.csv')
conn = sqlite3.connect('insurance.db')

#############
    #The Built-in pandas method that writes to the database using the entire framework
		#this creates the databse plus the table(s), the column(s) and the data (row(s))
df.to_sql(name="clients", conn='conn', if_exists='append', index="false")
#############
	
#############
    #The alternative method for inserting data into a database
            # provides a connection to the database
#cursor = conn.cursor() 			
            # create the table to import data into
			#   create an obj to hold the cursor function
#insurance_table = "CREATE TABLE IF NOT EXISTS clients (age INTEGER, sex TEXT, bmi REAL, children INTEGER, smoker TEXT, region TEXT, charges REAL);"
            # call the object to create the table
#cursor.execute(insurance_table)
            # create a loop to upload the tables records
#for row in df.itertuples():
            # create another oblect with 
#	insurance_data = f"INSERT INTO Clients (age, sex, bmi, children, smoker, region, charges) VALUES ({row[1]},'{row[2]}',{row[3]},{row[4]},'{row[5]}','{row[6]}',{row[7]})"
#cursor.execute(insurance_data)
#############

conn.commit()

cursor = conn.cursor() 			
cursor.execute('''SELECT age FROM clients.insurance.db;''')

conn.close()
