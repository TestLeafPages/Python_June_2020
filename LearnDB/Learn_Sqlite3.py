# pip install db-sqlite3

import sqlite3

# create the connection
con = sqlite3.connect("demo_student.db")
print('Create Connection')


# create table
con.execute(''' CREATE TABLE IF NOT EXISTS student_info('R_No','Name', 'Email' ) ''')
print('Create Table')


# insert record
con.execute(''' INSERT INTO student_info('R_No','Name', 'Email') 
                VALUES('004', 'Gopinath', 'gopithri@gmail.com')  ''')
con.commit()
print('inserted records')


# reading the data
data = con.execute(''' SELECT * FROM student_info ''')
print(type(data))
for i in data:
    print(i)
print("reading all values")



# update the value
con.execute(''' UPDATE student_info SET Name = "Gopinath Jayakumar" WHERE R_No = "003" ''')
con.commit()
print('Updated the value')


#close
con.close()
print("closed")