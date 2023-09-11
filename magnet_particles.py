def doubles(maxk, maxn):
    def knesimo(k,n):
        term = 1 / (k * (n + 1) ** (2 * k))
        return term
    sol = 0

    for k in range(1,maxk + 1):
        for n in range(1, maxn + 1):
            sol = sol + knesimo(k,n)
    return sol
temp = doubles(10,10)
print(temp)


#     def sum_k(maxk, n):
#         sumk = 0
#         for k in range(1, maxk + 1):
#             sumk += 1 / (k * (n + 1) ** (2 * k))
#             print(sumk)
#         return sumk
#
#     def sum_n(k, maxn):
#         sumn = 0
#         for n in range(1, maxn + 1):
#             sumn += 1 / (k * (n + 1) ** (2 * k))
#             print(sumn)
#         return sumn
#
#     # your code
#
#     return 0
#
# def sum_k(maxk, n):
#     sumk = 0
#     for k in range(1,maxk +1):
#         sumk += 1/(k*(n+1)**(2*k))
#         print(sumk)
#     return sumk
#
# def sum_n(k, maxn):
#     sumn = 0
#     for n in range(1,maxn +1):
#         sumn += 1/(k*(n+1)**(2*k))
#         print(sumn)

#
#
# temp = sum_n(2,10)
# print(temp)