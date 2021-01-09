def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def sumAll(*args):
    if len(args) == 0:
        return None
    sum = 0
    for i in args:
        if isNumber(i) == True and type(i) != bool:
            sum += i
    if sum == 0 and args.count(0)==0:
        return None
    else:
        return sum
print(1, 2, 3, 4, 5)
print(sumAll(1, 2, 3, 4, 5))
print(0, -1)
print(sumAll(0, -1))
print(sumAll())
print(1, 2, '*', -1.1, 'asdasda')
print(sumAll(1, 2, '*', -1.1, 'asdasda', True))
print(sumAll(0, 0, 0, 0))
