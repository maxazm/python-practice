class Person(object): #(object)は継承

    num_legs = 2
    count = 0
    #constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def walk(self):
        print(f"{self.name} is walking ... with {Person.num_legs} legs!")

    def run(self):
        print(f"{self.name} is running ... with {Person.num_legs} legs!")

john = Person("John", 28, "male")
taro = Person("Taro", 18, "male")
emma = Person("Emma", 40, "female")

print(john.name)
print(john.age)
print(john.gender)
print(Person.count)

#インスタンス変数
print(taro.name)
print(taro.age)
print(taro.gender)

john.walk()
emma.walk()
john.run()

print(john.num_legs)
Person.num_legs = 3
print(emma.num_legs)