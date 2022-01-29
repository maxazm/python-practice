#mutable list, dict, set
fruits = ["apple", "orange", "banana"]
print(fruits)
print(f"fruits[]のIDは{id(fruits)}")
fruits.append("lemon")
print(fruits)
print(f"fruits[]のIDは{id(fruits)}")

#inmutable int, float, str, bool, tuple
fruit = "apple"
print(fruit)
print(f"fruitのIDは{id(fruit)}")
fruit += ", lemon"
print(f"fruitのIDは{id(fruit)}")
print(fruit)

text_list = []
for i in range(1, 11):
    text_list.append(str(i))

text = "-".join(text_list)
print(text)