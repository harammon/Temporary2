#1~50까지의 수 중 3의배수의 합(단, 5의 배수 제외)
#continue 사용 x
sum = 0
for i in range(1, 51):
    if i % 3 == 0:
        if i % 5 != 0:
            sum += i
print("결과 : ", sum)