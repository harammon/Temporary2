def sumEven1(*args):
    if len(args) == 0:
        return -1
    sum = 0
    for i in args:
        if i % 2 == 0:
            sum += i
    if sum == 0:
        return 0
    else:
        return sum
print(1, 2, 3, 4, 5)
print(sumEven1(1, 2, 3, 4, 5))
print(0, -1)
print(sumEven1(0, -1))
print(sumEven1())
