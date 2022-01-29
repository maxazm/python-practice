#関数

fahrenheit = 72
# celsius = (fahrenheit - 32) * 5/9
# print(celsius)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)

