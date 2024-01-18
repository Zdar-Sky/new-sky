x = int(input('Enter number: '))
y = x % 2
if y == 0:
    z = 0
    a = 0
    b = 0
    while z <= x:
        print(z)
        b += z
        z += 2
        a += 1
    print('This includes ', a, 'even numbers')
    print('The sum of these numbers =', b)
else:
    print('This is an odd number')