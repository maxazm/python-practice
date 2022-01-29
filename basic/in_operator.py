fruits = ["apple", "peach", "orange", "melon"]
print("apple" in fruits)
print("lemon" in fruits)
print("lemon" not in fruits)

#challenge
favorite_fruits = input("好きなフルーツを入力してください : ")
if favorite_fruits in fruits:
    fruits.remove(favorite_fruits)
    print(fruits)
elif favorite_fruits not in fruits:
    fruits.append(favorite_fruits)
    print(fruits)
