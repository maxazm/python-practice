class Duck:
    """
    This is a class for Duck.

    Attributes:
        name: the name of the duck

    Methods:
        walk: print ***
        quack: print ***
        fly: print ***
    """
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking...")

    def quack(self):
        print("quack quack!")

    def fly(self):
        print("Whee!")

class Penguin:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking...?")

    def quack(self):
        print("quack quack?")

    def swim(self):
        print("Swimming!")

def walk_and_quack(duck):
    duck.walk()
    duck.quack()

if __name__ == "__main__":
    help(Duck)
    donald = Duck("Donald")
    pingu = Penguin("pingu")
    donald.fly()
    pingu.quack()
    walk_and_quack(pingu)
    walk_and_quack(donald)
