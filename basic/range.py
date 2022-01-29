#range(start, stop, step)
# for i in range(1, 7, 1):
#     print(i)
#     print("hello")
# for _ in range(10):
#     print("1")

#challenge
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: print(i)