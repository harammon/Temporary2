from random import *

def differtwovalue(a, b):
    if a >= b:
        return a - b
    else:
        return b - a

for i in range(5):
    x, y = randint(1, 30), randint(1, 30)
    result = differtwovalue(x, y)
    print(x, '와', y, '의 차는', result, '입니다.')
    print()
