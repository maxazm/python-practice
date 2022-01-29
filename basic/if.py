age = 25
age_alcohol = 23
age_drive = 18

if age >= age_alcohol:
    print(f"You're {age} years old and you can drink alcohol")
else:
    print("You are too young to drink alcohol")

if age >= age_alcohol:
    print("you can drink beer!")
elif age < age_drive:
    print("You cannot even drive")
else:
    print("You cannot drink beer but you can drive a car only if you have driver's license")

if not 0 < age < 120:
    print("hello")

#Challenge1, 2
balance = 241412414
withdrawal = 2221
withdraw_limit = 1000000
if withdrawal > withdraw_limit:
    print(f"Limitation. You cannot withdraw over ¥{withdraw_limit}")
elif balance >= withdrawal:
    balance -= withdrawal
    print(f"You withdrew ¥{withdrawal} and your new balance is ¥{balance}")
else:
    print("Not enough balance. You cannot withdraw money")


