my_variable = "This is global variable"

def myfunc():
    print("This is my function")

def another_func():
    print("This is another function")

if __name__ == "__main__":
    myfunc()
    another_func()
    print("This is mymodule")
    print(f"mymodule.__name__: {__name__}")