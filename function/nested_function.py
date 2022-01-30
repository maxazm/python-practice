msg = "I am global"

def outer(outer_param):
    msg = "I am outer"
    def inner():
        nonlocal msg
        msg = "I am inner"
        inner_param = "inner arg"
        print("this is inner function")
        print(outer_param)
        print(msg)
    inner()
    print(msg)
    # print(inner_param)

outer("outer arg")
print(msg)
# inner()