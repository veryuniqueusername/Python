import time
from math import log10
from math import floor


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


x = 0
n = 1
pn = 0
po = 0
arr: list[int] = []
y = 0

start = time.perf_counter()

while x < 10000000:
    # t1 = time.perf_counter()
    y += 1
    n *= 1024
    x += 10
    po = pn
    pn = floor(log10(n))
    # print(x, ":")
    # print("first digit:", int(str(n)[:1]))
    # print("pow:", pn)
    # print("diff pow:", pn - po)
    if pn - po == 4:
        arr.append(x)
        print(x)

arrdiff: list[int] = []
arrdiffarr: list[int] = []
for i in range(0, len(arr) - 1):
    diff = arr[i + 1] - arr[i]
    if diff == 980:
        # arrdiff.append(bcolors.FAIL + str(diff) + bcolors.ENDC)
        arrdiff.append(diff)
        arrdiffarr.append(arr[i + 1])
    else:
        arrdiff.append(diff)

arrdiffarrdiff: list[int] = []
for i in range(0, len(arrdiffarr) - 1):
    diff = arrdiffarr[i + 1] - arrdiffarr[i]
    if diff == 10680:
        arrdiffarrdiff.append(diff)
    else:
        arrdiffarrdiff.append(diff)
        # arrdiffarrdiff.append(bcolors.FAIL + str(diff) + bcolors.ENDC)

end = time.perf_counter() - start

# print(", ".join(arr))
# print(", ".join(arrdiff))
# print(", ".join(arrdiffarr))
# print(", ".join(arrdiffarrdiff))
print(arr)
print(arrdiff)
print(arrdiffarr)
print(arrdiffarrdiff)
print(len(arr) / y)
print(end)
