''' Программа которая получает на вход 2 числа больше и меньше,
определить кратно ли 1е число 2му вывести на экран сообщения об этом,
а также остаток отделения если 1е число Не кратно  2 му '''

x = int(input('Enter the number one: '))
y = int(input('Enter the number two: '))
a = x % y
if a == 0:
    print('The first number is a multiple of the second ')
else:
    print('the first number is not a multiple of the second ')