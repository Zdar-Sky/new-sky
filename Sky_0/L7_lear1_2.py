x = r = 1
while x < 10:
    while r < 10:
        print(x, 'x', r, '=', x * r, end='|')
        r += 1
    print()
    r = 1
    x += 1