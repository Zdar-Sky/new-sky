x = int(input('Enter number X: '))
y = int(input('Enter number Y > X: '))
z = 0
while x <= y:
    z += 1
    print(x)
    x += 1
print('Between X and Y,', z, 'numbers')