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

def fibonacci2(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result

print(fibonacci(6))
print(fibonacci2(6))