import mysql.connector as sql

# db = sql.connect(
#     host = "localhost",
#     user = "root",
#     password = "DexterJonson12%",
#     database = "syudentmanagementsystem"
# )


# cursor = db.cursor()

# cursor.execute("iNSERT INTO student (firstname, phone_number) VALUES('mike', 09066089664)")
# db.commit()

# cursor.execute('SELECT * FROM student')
# data = cursor.fetchall()
# print(data)


db = sql.connect(
    host = "localhost",
    user = "root",
    password = "DexterJonson12%",
)

cursor = db.cursor()

cursor.execute('USE my_python_database')
# cursor.execute('CREATE TABLE user(id int PRIMARY KEY AUTO_INCREMENT, firstname TEXT NOT NULL, lastname TEXT NOT NULL, occupation TEXT NOT NULL)')
# cursor.execute('INSERT INTO user(firstname,lastname,occupation) VALUES("mary","clark","supermans mother")')
# db.commit()
cursor.execute('SELECT * FROM user'),
data = cursor.fetchall()
print(data)