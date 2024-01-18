number = int(input())
s = 0
while number:
    s += number % 10
    number //= 10
print(s)