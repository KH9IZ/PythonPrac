import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

with open(filename1) as f:
    text1 = f.read()
with open(filename2) as f:
    text2 = f.read()

uni_text1 = ast.unpars(ast.parse(text1))
uni_text2 = ast.unpars(ast.parse(text2))
