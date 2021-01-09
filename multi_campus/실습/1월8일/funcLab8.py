def print_triangle_withdeco(num, char = '%'):
    if num in range(1, 11):
        for j in range(1, num+1):
            a = j*char
            print(a.rjust(num))
    else:
        pass

print_triangle_withdeco(5, '*')
print_triangle_withdeco(2)
print_triangle_withdeco(11)
