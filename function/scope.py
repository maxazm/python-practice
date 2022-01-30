def print_name_local(): #ローカル変数
    first_name = "Taro"
    last_name = "Yamada"
    print(f"I'm {first_name} {last_name}")

print_name_local()
# print(first_name)

age = 30  #グローバル変数（モジュール変数）
def print_age():
    global age #global変数を上書き
    age = 28
    print(f"I'm {age} years old")

print_age()
print(age)