from random import *

while True:
    num = int(input("숫자를 하나 입력하세요. : "))
    if num == 0:
        print("종료")
        break
    elif num < -10 or num > 10:
        print()
        continue
    else:
        result = 1
        if num > 0:
            for i in range(1, num+1):
                result *= i 
            print("입력값 :", num)
            print(result, '\n')
        else:
            num = abs(num)
            for i in range(1, num+1):
                result *= i 
            print("입력값(부호변경) :", num)
            print(result, '\n')

