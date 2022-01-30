def square(x):
    return x * x

print(square(3))

s = lambda x: x * x

print(s(5))

def power(exponent):
    return lambda x: x ** exponent

four_power = power(4)
four_power(2)
#
# def filter_func(num):
#     return not num % 2 == 0

numbers = [6, 2, 4, 434, 43, 324, 322, 2, 5]
filter_num = filter(lambda num: num % 2, numbers)
print(list(filter_num))