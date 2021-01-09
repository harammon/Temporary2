import random

num = random.randint(5, 10)
index = 1
print('추출 값 : ', num)
while True:
    if num >= index:
        print(index, '->', index**2)
        index += 1
    else:
        break