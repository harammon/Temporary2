'''9 : 홀수
   8 : 짝수
   7 : 홀수
   6 : 짝수
   5 : 홀수
   4 : 짝수'''
for i in range(6):
    index = 9 - i
    if index % 2 == 0:
        print(index, ': 짝수')
    else:
        print(index, ': 홀수')
