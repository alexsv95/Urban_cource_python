import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    parameters = f"user{i}", f"example{i}@gmail.com", f"{i*10}", "1000"
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)", parameters)

cursor.execute("SELECT id FROM Users")
users = cursor.fetchall()

for i in users:
    if i[0] % 2 != 0:
        cursor.execute(f"UPDATE Users SET balance = ? WHERE id = {i[0]}", (500,))\

id = 1
for i in users:
    cursor.execute(f"DELETE FROM Users WHERE id = {id}")
    id += 3

cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
users_2 = cursor.fetchall()
for user in users_2:
    print(f'имя: {user[1]} | почта: {user[2]} | возраст {user[3]} | баланс: {user[4]}')

connection.commit()
connection.close()