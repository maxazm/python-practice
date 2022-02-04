fruits = ["apple", "orange", "banana"]


# print(next(fruits))
fruits_iterator = iter(fruits)
# print(next(fruits_iterator))
# print(next(fruits_iterator))
# print(next(fruits_iterator))

print(id(fruits_iterator))
print(id(iter(fruits_iterator)))


print(fruits_iterator.__next__())