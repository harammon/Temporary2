from random import *

index = 0
while True:
    num = randint(0, 30)
    if num >= 27 or num == 0:
        break
    else:
        print(chr(num+64), '(', num, ')')
        index += 1
print("수행 횟수는", index, "번 입니다.")



 