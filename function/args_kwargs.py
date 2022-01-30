#*args 不特定多数のパラメーターを受け取る
print("hello","world")

def get_average(*args):
    num = len(args)
    print(args)
    if num == 0:
        return 0
    total = sum(args)
    return total / num

average = get_average(1,2,3,4,5)
print(average)

#**kwargs *argsのdict ver
def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(param1=10, param2=6, param3=100)

#* unpacking operator
numbers= (1,2,3)
print(numbers)
print(*numbers) #tupleがunpackされる

a = {"a": 1, "b": 2}
b = {"c": 3, "d": 4}
c = {**a, **b}
print(c)
