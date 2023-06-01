import numpy as np

np.set_printoptions(linewidth=150)

size: int = 17
# C = size - 2
matrix: list[list[int]] = []
factor: list[list[int]] = []

for i in range(0, size):
    matrix.append([])
    factor.append([])
    for j in range(0, size):
        matrix[i].append(0)
        factor[i].append(0)

matrix[size - 1][size - 1] = 1


polynomial: list[int] = [1] * size

for i in range(0, size):
    for j in range(0, size - i):
        factor[i + j][j] = polynomial[j] // polynomial[0]
        matrix[size - 1][j] = polynomial[j] // polynomial[0]
        matrix[size - 1][j] *= -1 if (size - j) % 2 == 0 else 1
        if i != size - 1:
            matrix[i][size - 2] = polynomial[j] // polynomial[0]
            matrix[i][0] = polynomial[j] // polynomial[0]
            matrix[i][0] *= -1 if (size - j) % 2 == 0 else 1
    polynomial.pop(0)
    for j in range(0, size - i - 1):
        polynomial[j] *= j + 1
    # print(polynomial)

for i in range(size - 2, -1, -1):
    for j in range(size - 3, 0, -1):
        for k in range(0, size):
            matrix[i][j] += matrix[k][j + 1] * factor[k][i]

print(np.matrix(matrix))
print(np.matrix(factor))

out: str = "S_{%d}(t)=[\\frac{1}{%d!}(" % (size - 2, size - 1)
for c in range(0, 2):
    for i in range(0, size):
        if c == 0:
            append: str = "P[n+%d].x(" % (i) if i != 0 else "P[n].x("
        else:
            append: str = "P[n+%d].y(" % (i) if i != 0 else "P[n].y("
        for j in range(0, size):
            if j == 0:
                append = "".join([append, "%d" % (matrix[j][i])])
            elif j == 1:
                append = "".join([append, "%dt" % (matrix[j][i])])
            else:
                append = "".join([append, "%dt^{%d}" % (matrix[j][i], j)])
            if j != size - 1:
                append = "".join([append, "+"])

        append = "".join([append, ")"])
        out = "".join([out, append])
        if i != size - 1:
            out = "".join([out, "+"])
    if c == 0:
        out = "".join([out, ","])

out = "".join([out, ")\\operatorname{for}n=[1...P.\\operatorname{length}]]"])
out = out.replace("[", "\\left[")
out = out.replace("]", "\\right]")
out = out.replace("(", "\\left(")
out = out.replace(")", "\\right)")
print(out)
