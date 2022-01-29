age = int(input("何歳ですか？"))
casino_age = 20
game_text = """
    Please choose the game
    1. ルーレット
    2. ブラックジャック
    3. ポーカー
"""
# print(f"あなたは{age}歳です")

#challenge1,2
if age >= casino_age :
    print("どうぞお入りください")
    game_select = input(game_text)
    if game_select == '1': print("You chose ルーレット")
    elif game_select == '2': print("You chose ブラックジャック")
    elif game_select == '3': print("You chose ポーカー")
    else: print("1 ~ 3を選んでください")

else:
    print("You cannot enter here")