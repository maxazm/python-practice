#for文でループを回す
# with open("pep8_introduction.txt") as f:
#     for line in f:
#         print(line, end="")

# .read()でファイルの中身を全て一つのstringとして返す
# with open("pep8_introduction.txt") as f:
#     print(f.read())

# .readline()で一行ずつ取得してstringで返す
# with open("pep8_introduction.txt") as f:
#     line = f.readline()
#     while line:
#         print(line, end="")
#         line = f.readline()

# .readlines()で全ての行をlistで返す
with open("pep8_introduction.txt") as f:
    lines = f.readlines()
    print(lines)
