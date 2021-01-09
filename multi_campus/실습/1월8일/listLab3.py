listnum = [10, 5, 7, 21, 4, 8, 18]
max = listnum[0]
min = listnum[0]
for i in listnum:
    if i > max:
        max = i
    if i < min:
        min = i
print('최솟값 : %d   최댓값 : %d' %(min, max))

