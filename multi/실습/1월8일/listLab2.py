listnum = [10, 5, 7, 21, 4, 8, 18]
min = listnum[0]
for i in listnum:
    if i < min:
        min = i
print('최솟값 : %d' %min)
