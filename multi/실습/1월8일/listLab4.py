from random import *

listnum = list()
for i in range(10):
    num = randint(1, 50)
    listnum.append(num)
print(listnum)
for i in range(len(listnum)):
    if listnum[i] < 10:
        listnum[i] = 100
print(listnum)
print(listnum[0])
print(listnum[-1])
print(listnum[1:6])
print(listnum[::-1])
print(listnum[0:])
del listnum[5]
print(listnum[0:])
del listnum[2:3]
print(listnum[0:])