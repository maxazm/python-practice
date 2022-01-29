#is演算子：同じオブジェクトかどうか

a = 1
b = 1
c = 3
d = a
e = 2 - 1
print(id(a))
print(id(b))
print(a is b)
print(a is not c)
print(d is a)
print(e is a)

hello = "hello"
hello2 = "h" + "e" + "l" + "l" + "o"
print(hello is hello2)
hello = "konnichiwa"
print(hello is hello2)