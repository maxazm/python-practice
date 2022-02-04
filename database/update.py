import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

target_name = input("Whose 'age' do you want to update?: ")
new_age = input("Tell me new age: ")
print(target_name, new_age)
# SQL injection (脆弱性がある)
update_query = f"UPDATE User SET age = {new_age} WHERE name = '{target_name}'"
# cursor.execute(update_query)
update_query = 'UPDATE User SET age = ? WHERE name = ?'
cursor.execute(update_query, (new_age, target_name))
con.commit()
