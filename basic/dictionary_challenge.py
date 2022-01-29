casino_age = 21
game_dict = {"1": "ルーレット", "2": "ブラックジャック", "3": "ポーカー", "4": "スロット"}

age = int(input("あなたは何歳ですか？："))
if age >= casino_age :
    print("どうぞお入りください")
    while True:
        print("プレーするゲームを選んでください")
        for idx, game in game_dict.items():
            print(f"{idx}: {game}")
        game_select = input(": ")
        if game_dict.get(game_select):
            print("You chose {}".format(game_dict[game_select]))
            break
        else:
            print("1 ~ 4を選んでください")
            continue
else:
    print("You cannot enter here")