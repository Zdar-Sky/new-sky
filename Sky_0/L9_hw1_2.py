x = input('Enter text: ')
lenth = len(x)
half = lenth // 2
if lenth % 2 == 0:
    print(x[:half])
    print(x[half:])
else:
    print(x[:half])
    print(x[half:])