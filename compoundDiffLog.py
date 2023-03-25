import math


log2: float = 0.30102
log3: float = 0.47712
log5: float = 0.69897
log7: float = 0.84509


def log(x: int) -> float:
    arr: list[float] = []
    while True:
        if x % 2 == 0:
            x //= 2
            arr.append(log2)
        elif x % 3 == 0:
            x //= 3
            arr.append(log3)
        elif x % 5 == 0:
            x //= 5
            arr.append(log5)
        elif x % 7 == 0:
            x //= 7
            arr.append(log7)
        else:
            break
    sum: float = 0
    # print(arr)
    for n in arr:
        sum += n
    if x != 1:
        sum = (log(x - 1) + log(x + 1)) / 2
    return sum


a: int = 11
print(log(a))
print(math.log10(a))
