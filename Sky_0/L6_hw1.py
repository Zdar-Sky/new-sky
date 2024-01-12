a = int(input('Enter first number '))
b = int(input('Enter second number '))
c = int(input('Enter third number '))
if (b < a > c) and (a > b < c): # a largest and b smallest
    print(a, 'largest and', b, 'smallest, Amount', a, '+', b, '=', a + b)
elif (a < b > c) and (b > a < c): # b largest and a smallest
    print(b, 'largest and', a, 'smallest, Amount', a, '+', b, '=', a + b)
elif (b < a > c) and (a > c < b): # a largest and c smallest
    print(a, 'largest and', c, 'smallest, Amount', a, '+', c, '=', a + c)
elif (b < c > a) and (b > a < c): # c largest and a smallest
    print(c, 'largest and', a, 'smallest, Amount', c, '+', a, '=', a + c)
elif (a < b > c) and (a > c < b): # b largest and c smallest
    print(b, 'largest and', c, 'smallest, Amount', b, '+', c, '=', b + c)
elif (a < c > b) and (a > b < c): # c largest and b smallest
    print(c, 'largest and', b, 'smallest, Amount', c, '+', b, '=', b + c)