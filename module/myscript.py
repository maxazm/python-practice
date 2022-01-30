#標準ライブラリ, サードパーティのライブラリ、自分達のライブラリ、ローカルのライブラリ

import sys
sys.path.append("/Users/ryokiazuma/Desktop/python-practice/function/")
import docstring
# import mymodule (as mm)
# from mymodule import myfunc, my_variable, another_func
from mymodule import *

myfunc() #mm.myfunc()
print(my_variable)
another_func()

# mymodule.myfunc()
# print(mymodule.my_variable)
print(sys.path)
print(docstring.multiply(3, 4))
