#カプセル化(情報隠蔽)
def casino_entrance(age, min_age=21):
    if age < 21:
        print(f"{min_age}歳以下はお断り")
        return

    def inner_casino_entrance():
        print("ようこそカジノへ")

    return inner_casino_entrance()

casino_entrance(18)
casino_entrance(22)