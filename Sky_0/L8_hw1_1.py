n = int(input('Enter number: '))
print('We derive all even numbers')
i = 0
for s in range(0, n, 2):
    i += s
    print(s)
print('Sum of numbers: ', i)