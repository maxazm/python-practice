import sys

square_list = [num * num for num in range(10)]
print(square_list)

print("=" * 30)
square_gen = (num * num for num in range(10))
print(square_gen)
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))

print("=" * 30)
print(sys.getsizeof(square_gen))
print(sys.getsizeof(square_list))

even_squares = [num * num for num in range(10) if num % 2 == 0]
print(even_squares)

# generator expressions
even_squares_gen = (num * num for num in range(10) if num % 2 == 0)
for num in even_squares_gen:
    print(num)