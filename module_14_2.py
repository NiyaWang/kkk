import sqlite3

connection = sqlite3.connect('not_telegram.db')
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

cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User1", "example1@gmail.com", 10, 1000))
cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User2", "example2@gmail.com", 20, 1000))
cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User3", "example3@gmail.com", 30, 1000))
cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User4", "example4@gmail.com", 40, 1000))
cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User5", "example5@gmail.com", 50, 1000))
cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User6", "example6@gmail.com", 60, 1000))
cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User7", "example7@gmail.com", 70, 1000))
cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User8", "example8@gmail.com", 80, 1000))
cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User9", "example9@gmail.com", 90, 1000))
cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User10", "example10@gmail.com", 100, 1000))

cursor.execute('''
UPDATE Users
SET balance = 500
WHERE id % 2 = 1
''')

cursor.execute("DELETE FROM Users WHERE id IN (SELECT id FROM Users WHERE (id - 1) % 3 = 0)")

cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')

cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total_records = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]

if total_records > 0:
    average_balance = total_balance / total_records
else:
    average_balance = 0

rows = cursor.fetchall()

for row in rows:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

print(f'Общее количество записей: {total_records}')
print(f'Сумма всех балансов: {total_balance}')
print(f'Средний баланс пользователей: {average_balance:.2f}')

connection.commit()
connection.close()