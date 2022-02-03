#変数定義
#correct
import math

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

#correct
def long_function_name(
        var_one, var_two, var_three, var_four
)
# \で区切って改行する
print("このように表示する文章が長かったりする場合は\
      バックスラッシュで区切ると改行できます")

a = 100000000000000000 \
    + 10000 \
    + 1000 \
    + 121 \
    + 100000

#関数間は二行あける
def func():
    pass


def func2():
    pass

#class内は一行あける
class MyClass:
    def __init__(self):
        pass

    def func(self):
        pass

#importのstyle
import os
import sys


#wrong
import os, sys

from subprocess import Popen, PIPE

#順番
#1. standard library (time, sys)
#2. Third Party (numpy, pandas)
#3. Our library
#4. local library
#それぞれ一行あける abc順

#absolute import
import mypkg.sibling

# a = 1
# のあとは半角スペースあける
a = 1  # インラインコメント 2半角スペース空ける

# - _xxx: internal use only(non public)
# - xxx_: pythonですでに使われている単語を使いたいとき　ex type_
# - __xxx: クラスの属性として使うことで名前修飾される
# -__xxx__: magic methodと呼ばれるもので　pythonが特別に設定しているもの
# - _: 最近実行した戻り値や、iteration時に使わない変数

for _ in range(18):
    print("hello")

#return
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

#オブジェクトタイプの確認はisinstance()を使う
if isinstance(obj, int)

#wrong
type(obj) is type(1)

def greeting(name: str) -> str:
    return "Hello" + name
#一つでもannotationをつけたら全てにつける
#pythonがtypeのチェックをしてくれるわけではない
#pythonは動的片付け言語であることを意識