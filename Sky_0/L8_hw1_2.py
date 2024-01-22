skip_numbers = {7, 13, 21, 29}  # We set the numbers that you need to miss
t = int(input('Enter number: '))
while t > 35:
    t -=t
    print('The number should be <= 35')
    t = int(input('Enter number: '))
else:
    for i in range(1, t + 1):
        if i in skip_numbers:
            print('-Number delete-')
            continue
        print(i)