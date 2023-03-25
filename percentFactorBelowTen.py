x = 0
n = 0
while x < 1000:
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
        n += 1
    x += 1
print(n)
