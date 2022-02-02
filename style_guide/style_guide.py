#変数定義
#correct
x = 1
y = 2

#wrong
xxx       = 1
y         = 2

x = 1

#関数の引数の「=」にはスペース不要
#correct
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

#wrong
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

#operatorの周りにスペースを一個, operatorにpriorityがある場合はスペースを除く
#correct
x = x + 1
y = x
y += y
x = x*x + y*y

#wrong
x=x+1

#カンマの後にはスペースを入れる
range(1, 11)
a = [1, 2, 3, 4, 5]
#閉じ括弧の場合はスペース不要
foo = (0,)

FILLES = [
    "setup.cfg",
    "tox.ini",
]
#行の折り返し
foo = long_function_name(
    var_one, var_two,
    var_three, var_four
)
