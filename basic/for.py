fruits = ["apple", "grapes", "melon", "banana"]

for fruit in fruits:
    print(f"I love {fruit}")

for i in range(21):
    print(i)

text = "hello world"
for char in text:
    print(char)

user_fav = input("好きなフルーツは何ですか？　")
for fruit in fruits:
    if fruit == user_fav:
        print(f"{fruit}は好き")
    else:
        print(f"{fruit}は好きじゃない")

fav = []
non_fav = []
for fruit in fruits:
    user_ans = input(f"{fruit}は好きですか？ y/n ")
    if user_ans == "y":
        fav.append(fruit)
    else:
        non_fav.append(fruit)
print(f"Your favorite fruits are {fav}")
print(f"you don't like these fruits {non_fav}")

