a = int(input())
number = a if a < 20 else 100
''' Or such an option
if a < 20:
    number = a
else:
    number = 100
'''
print(number)