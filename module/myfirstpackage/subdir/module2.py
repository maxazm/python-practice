from .module3 import myfunc3
from .. import module1

def myfunc():
    print("This is myfunc from module2")
    module1.myfunc()

def myfunc2():
    print("This is myfunc2 from module2")
    myfunc3()