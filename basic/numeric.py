#数値型 integer, float, complex
#numeric operator
integer = 1
float = 2.5
print(type(integer))
print(type(float))
print(1.2 + 1.2 + 1.2)
print(1 + 0.4)
print(1 * 23)
print(1 / 32)
result = 1 + 2.5
print(f"type of result:{result} is {type(result)}")
print(14 // 3) #floor division
print(15 % 2) #modulo
print(2 ** 3) #exponentiation

hit_point = 100
attack_point = 40.3
remain = hit_point - attack_point
print(f"remain hit point is {remain}")

#augmented assignment
a = 1
a = a + 1
print(a)