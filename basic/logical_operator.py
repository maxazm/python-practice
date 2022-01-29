#論理演算子 and or not
a = 1
b = 1
c = 100
print(a == b and c > a)
print(not a == b)

#Challenge1 年齢が10歳以上かつ身長が110cm以上なら乗れるアトラクション
age = 10
height = 110
print(age >= 10 and height >= 110)

# Challenge2 修士号保持もしくは5年以上の実務経験があればVisaの取得が可能
master = True
job_experience = 0
print(master or job_experience >= 5)