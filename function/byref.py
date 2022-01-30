#参照渡し(byref) <->　値渡し(byvalue)
#pythonは参照渡し

def add_nums(a,b):
    print(f"第一引数のid: {id(a)}")
    print(f"第二引数のid: {id(b)}")
    return a + b

one = 1
two = 2
print(f"oneのid: {id(one)}")
print(f"twoのid: {id(two)}")
print(add_nums(one, two))

def add_one(num): #inmutable
    print(f"変更前{id(num)}")
    num+=1
    print(f"変更後{id(num)}")
    return num

number = 1
print(id(number))
print(number)
add_one(number)
print(number)

def add_fruits(fruits, fruit): #mutable
    print(f"変更前のID:{id(fruits)}")
    fruits.append(fruit)
    print(f"変更後のID:{id(fruits)}")
    return fruits

myfruits = ["apple", "orange", "peach"]
myfruit = "lemon"
print(f"関数呼び出し前のmyfruits:{myfruits}")
add_fruits(myfruits, myfruit)
print(f"関数呼び出し後のmyfruits:{myfruits}")