# Программы которые проверяет является ли введенная пользователем число четным
x = int(input('Enter the number: '))
y = x % 2
if y == 0:
    print('This is an even number')
else:
    print('This is an odd number')