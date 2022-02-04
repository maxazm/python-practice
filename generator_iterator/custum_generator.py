# range(18)
def myrange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1


mr = myrange(10)
print(type(mr))

# for i in mr:
# #     print(i)

print(next(mr))
print(next(mr))
print("end of next()")
print("start of for loop")

for i in mr:
    print(i)


# challenge
def even(num):
    while num != 0:
        if num % 2 == 0:
            yield num
        num -= 1


print("=" * 30)
print("start of even generator")
even_obj = even(23)
for i in even_obj:
    print(i)
