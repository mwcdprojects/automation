#!C:\Python27\python.exe

import mysql.connector


conn = mysql.connector.connect(host='bl-mbp-mysql.southindia.cloudapp.azure.com' ,port=3306 , user='user' , password='HWf6frqGoR61', db='MWCD_TEST')

a = conn.cursor()

sql = 'SHOW TABLES;'
sql1 = "SELECT count(*) from BankBranch;"
a.execute(sql1)
print a.fetchall()

