k = int(input())
s = 0
for _ in range(k):
    number = int(input())
    if number % 6 == 0:
        s += number
print(s)