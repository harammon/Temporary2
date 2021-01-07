def expr(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        return num1 / num2
    else:
        return None

while True:
    a, b, c = input("숫자 두 개와 연산자를 차례로 입력하세요 : ").split()
    a = int(a)
    b = int(b)
    if expr(a, b, c) == None:
        print("수행 불가")
        print()
    else:
        print("연산결과 :", expr(a, b, c))
        print()
