import statistics
import math

sP = 3
P = [300, 300, 300, 300]
st = 0.2
t = [46.38, 78.2, 93,3, 120]

sm = 0.015
m = [0.200, 0.200, 0.300, 0.400]
sT = 1
T = [20, 20, 20, 20]

sE = []
sc = []

for i in range(0,4):
    E = P[i] * t[i]
    sE.append(E *
        math.sqrt(
            math.pow(sP / P[i], 2) + 
            math.pow(st / t[i], 2)
        ))

print(sE)

for i in range(0,4):
    E = P[i] * t[i]
    c = E / (m[i] * T[i])
    sc.append(
        math.sqrt(c *
            math.pow(sE[i] / E, 2) + 
            math.pow(sm / m[i], 2) + 
            math.pow(sT / T[i], 2)
        ))

print(sc)
print(statistics.mean(sc))