n = int(input('enter your number: '))

def fact(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
        yield a


for i in fact(n):
    print(i)
