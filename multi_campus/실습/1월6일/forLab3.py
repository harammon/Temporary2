import random

num1 = random.randint(1, 10)
num2 = random.randint(30, 40)
sum = 0
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        sum += i
print('X :', num1)
print('Y :', num2)
print('X부터 Y까지의 짝수의 합 : ', sum)
