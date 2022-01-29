#tuple 変更できないリスト[]ではなく（）を用いる
#主に変更する必要のないものに使用する

date_of_birth = (1999,2,22)
print(date_of_birth)
year, month, date = date_of_birth #unpackする
print(year, month, date)

# date_of_birth[0] = 1992
# print(date_of_birth)