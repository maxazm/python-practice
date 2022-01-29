#whileループ
count = 0
while(count < 10):
    print(count)
    count += 1

#break continue
while True:
    age = int(input("あなたは何歳ですか？ "))
    if not 0 <= age <= 120:
        print("入力された値は正しくありません")
        continue
    else:
        print("あなたは{}歳です".format(age))
        break

#challenge
casino_age = 21
game_text = """
    Please choose the game
    1. ルーレット
    2. ブラックジャック
    3. ポーカー
"""

age = int(input("あなたは何歳ですか？："))
if age >= casino_age :
    print("どうぞお入りください")
    while True:
        game_select = input(game_text)
        if game_select == '1':
            print("You chose ルーレット")
            break
        elif game_select == '2':
            print("You chose ブラックジャック")
            break
        elif game_select == '3':
            print("You chose ポーカー")
            break
        else:
            print("1 ~ 3を選んでください")
            continue
else:
    print("You cannot enter here")