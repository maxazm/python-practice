import re
#Regular Expressio　（正規表現　通称RegEx）

#challenge1
def is_valid_format():
    while True:
        user_input = input("生年月日を入力してください（yyyy/mm/dd）：")
        validation = re.search("^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[0-1])$", user_input)
        if validation:
            print("ok")
            break
        else:
            continue

def is_valid_email():
    while True:
        user_input = input("emailアドレスを入力してください（example@sample.com）：")
        validation = re.search("^(\w|\.|-)+@(\w|\.|-)+\.[a-zA-Z]{2,3}$", user_input)
        if validation:
            print("ok")
            break
        else:
            print("invalid")
            continue

is_valid_format()
is_valid_email()

email = "myemail@sample.com"
print("@" in email)

matched = re.search("@\w+\.", email)

if matched:
    print(matched)
    print("Matched")
else:
    print("Not found!")

#metacharacter
#[]
print(re.search("[a-c]", "a"))
print(re.search("[0-9]", "131312"))

#^最初の文字
print(re.search("^[a-c]", "0test"))
print(re.search("^[a-c]", "atest"))

#{n} n回リピート
print(re.search("^[0-9]{4}", "21/3/31"))

# {n, m} 最低n回, 最高m回リピート
print(re.search("^[0-9]{2,4}", "2021/3/31"))

# $ 最後の文字
print(re.search("[0-9]{2}$", "2021/3/31"))

# * 左のパターンを0回以上繰り返す
print(re.search("a*b", "aaaab"))

# + 左のパターンを1回以上繰り返す
print(re.search("a+b", "ab"))

# ? 左のパターンを0回か1回繰り返す
print(re.search("ab?c", "abc"))

# | or
print(re.search("abc|012", "01"))

# () グループ
print(re.search("te(s|x)t", "test"))

# . 任意の1文字
print(re.search("h.t", "hot"))

# \ エスケープ
print(re.search("h\.t", "h.t"))

# \w [a-zA-Z0-9_]　全てのアルファベット、数字及びアンダースコア
print(re.search("h\wt", "h_t"))

