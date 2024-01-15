import datetime
a = int(input('Enter year: '))
b = datetime.date.today().year
c = a % 4 # We count on the leap year of the leap year of four. Рассчитываем високосный год, кратен четырем.
if c == 0:
    print("It's a leap year")
else:
    print("It's not a leap year")
if a == b:
    pass
else:
    d = b % 4
    if d == 0:
        print('Current year:', b, "it's a leap year")
    else:
        print('Current year:', b, "it's not a leap year")