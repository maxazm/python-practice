class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking!")

class Dog(Animal):
    def bark(self):
        return print(f"{self.name} is barking")


def walk_with_me(animal):
    method = getattr(animal, "walk", None)
    if callable(method):
        animal.walk()
    else:
        raise TypeError(f"{type(animal).__name__}は散歩できません")

if __name__ == "__main__":
    pochi = Animal("Pochi")
    pochi.walk()
    walk_with_me(pochi)
