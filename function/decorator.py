#decorator 関数に機能を付属する

def greeting(func):
    def inner(*args, **kwargs):
        print("Hello!")
        func(*args, **kwargs)
        print("Nice to meet you!")
    return inner

@greeting
def say_name(name):
    print(f"I am {name}")

@greeting
def say_name_and_origin(name,origin):
    print(f"I'm {name}, I'm from {origin}")

# say_name = greeting(say_name)
# say_name("Jiro")
say_name_and_origin("Taro", "Tokyo")
# say_name("Jiro")

def decorate_func(func):
    def decorator(*args):
        func(*args)
        print("This is decorator")

    return decorator

@decorate_func
def printing_func(param):
    print(f"{param}")
    print("This is printing func")

# function = decorate_func(printing_func)
printing_func("hello")
# function("hello", "hellooooo")