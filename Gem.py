import math
arr = [16.5, 18.0, 20.7, 25.1, 30.7]
sumsq = 1
res = 0
start = 0.7
end = 0.8
acc = 10000
for i in range(acc):
    k = (end - start) / acc
    step = start + k * i
    temp_sumsq = 0.0
    for j in arr:
        temp_sumsq += math.pow(j % (step), 1)
    if temp_sumsq < sumsq:
        sumsq = temp_sumsq
        res = step
        print((step), sumsq)
print(sumsq)
print(res)
