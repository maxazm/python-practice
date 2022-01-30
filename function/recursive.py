#factorial 階乗　3! = 3 * 2 * 1

def factorial(num):
    if num == 1:
        return num
    return num * factorial(num-1)

print(factorial(5))

def fibonacci(num):
    return fibonacci_helper(0, 1, num)


def fibonacci_helper(num1, num2, count):
    if count <= 1:
        return num2
    return fibonacci_helper(num2, num1+num2, count-1)

print(fibonacci(5))

