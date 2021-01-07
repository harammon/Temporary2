def print_gugudan(x):
    if x in range(1, 10):
        print('구구단 :', x, '단')
        for i in range(9):
            print(x, '*', (i+1), '=', x * (i+1))

print_gugudan(1.1)
print_gugudan(3)
