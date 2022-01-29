fruits = ["apple", "peach", "melon", "banana"]
#for else
for fruit in fruits:
    user_ans = input("あなたが探しているフルーツは{}ですか？ y/n ".format(fruit))
    if user_ans == "y":
        print("見つかって良かったですね")
        break
    else:
        print("そうですか...")
else:
    print("お探しのフルーツは見つかりませんでした")

#while else
count = 0
while count < 10:
    print(count)
    count += 1
else:
    print("10未満ではなくなりました")