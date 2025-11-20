import sqlite3

connection=sqlite3.connect("student.db")

#creating cursor
cursor = connection.cursor()

#creating table
table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

#inert some more records

cursor.execute('''Insert Into StudenT values('Pooja','Computer Science','A',95)''')
cursor.execute('''Insert Into StudenT values('Fiza','AI/ML','B',90)''')
cursor.execute('''Insert Into StudenT values('Hemanth','Computer Science','A',85)''')
cursor.execute('''Insert Into StudenT values('Mouli','Data Science','C',80)''')
cursor.execute('''Insert Into StudenT values('Harsha','Computer Science','A',90)''')
cursor.execute('''Insert Into StudenT values('sai','AI/ML','B',89)''')

#Display all records
print("The inserted records are")
data=cursor.execute('''Select * From STUDENT''')
for row in data:
    print(row)


#Close the connection

connection.commit()
connection.close()