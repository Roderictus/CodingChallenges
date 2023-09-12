def doubles(maxk, maxn):
    def knesimo(k,n):
        term = 1 / (k * (n + 1) ** (2 * k))
        return term
    sol = 0

    for k in range(1,maxk + 1):
        for n in range(1, maxn + 1):
            temp = knesimo(k,n)
            sol = sol + temp
            if temp <  0.000000000000000001:
                break

    return sol

# Hacer una lista iterable




temp = doubles(700,700)
print(temp)

# print(temp)