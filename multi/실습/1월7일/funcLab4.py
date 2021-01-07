def print_triangle(x):
    if x in range(1, 11):
        for i in range(x):
            print('*' * (i+1))

while True:
    n = int(input("숫자를 입력하세요. :"))
    print_triangle(n)
    print()