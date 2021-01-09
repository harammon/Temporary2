import random

while True:
    pairNum1, pairNum2 = random.randint(1, 6), random.randint(1, 6)
    print('pairNum1 :', pairNum1, 'pairNum1 :', pairNum2)
    if pairNum1 == pairNum2:
        print("게임 끝")
        break
    else:
        if pairNum1 > pairNum2:
            print('pairNum1이 pairNum2보다 크다.')
        else:
            print('pairNum1이 pairNum2보다 작다.')
        print()
        
