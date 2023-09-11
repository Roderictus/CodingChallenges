def doubles(maxk, maxn):

    def knesimo(k,n):
        term = 1 / (k * (n + 1) ** (2 * k))
        return term
    sol = 0

    for k in range(1,maxk + 1):
        for n in range(1, maxn + 1):
            sol = sol + knesimo(k,n)
    return sol
temp = doubles(1000,10000)
print(temp)

# print(temp)