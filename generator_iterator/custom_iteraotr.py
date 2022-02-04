class MyIterator:
    def __init__(self, start=0):
        self.current = start


    def __next__(self):
        num = self.current
        self.current += 1
        return num

    def __iter__(self):
        return self


my_iterator = MyIterator(10)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(id(my_iterator))
print(id(iter(my_iterator)))


class Even:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        if self.current < 2:
            raise StopIteration
        elif self.current % 2 == 0:
            num = self.current
            self.current -= 2
            return num
        else:
            self.current -= 1
            return self.__next__()

    def __iter__(self):
        return self

if __name__ == "__main__":
    even_iterator = Even(21)
    print(next(even_iterator))
    print(next(even_iterator))
    print(next(even_iterator))
    print(next(even_iterator))
    print(next(even_iterator))
    print(next(even_iterator))
    print(next(even_iterator))
    print(next(even_iterator))

