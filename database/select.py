import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

# for row in cursor.execute("SELECT * FROM User"):
#     print(row)

cursor.execute("SELECT * FROM User")
print(next(cursor))
# .fetchall(): 現在のcursor以下全てのタプルのリストを返す
print(cursor.fetchall())
# fetchone(): 現在のcursorのレコードをタプルで返す
print(cursor.fetchone())

