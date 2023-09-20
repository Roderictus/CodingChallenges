# https://www.codewars.com/kata/64348795d4d3ea00196f5e76

def average_to_binary(n):
    sol = []

    i = 0
    while n > (2**i):
        i += 1
        print(f"n:{n} i = {i} 2**i ={2**i}")

    lista_sqr = [2**(i-(n+1)) for n in range(0,i)]
    lista_avg = [(2**(i-(n+1)))/2 for n in range(0,i)]
    lista_avg[0] = 2**(i-1)

    list_zero = [0] * len(lista_sqr)
    print(lista_sqr)
    print(list_zero)
    print(lista_avg)
    for num in range(0, (len(lista_avg))):
        n_temp = n - lista_avg[num]
        if n_temp == 0:
            list_zero[num] = lista_avg[num]
            break
        elif n_temp < 0:
            pass
        elif n_temp > 0:
            n = n_temp
            list_zero[num] = lista_avg[num]
    return list_zero

temp = average_to_binary(10)

print(temp)

#
# test_cases = [(0, ['0'])
#               (0.5, ['x']),
#               (1, ['1']),
#               (1.5, []),
#               (2, ['x0']),
#               (2.5, ['1x', 'xx']),
#               (5, ['1x0', 'x01', 'xx0']),
#               (5.5, ['1xx', 'xxx']),
#               (10, ['10x1', '1x00', 'x010', 'x0x1', 'xx00']),
#               (10.5, ['101x', '1x0x', 'x01x', 'xx0x']),
#               (21, ['101x0', '10x11', '1x001', '1x0x0', 'x0101', 'x01x0', 'x0x11', 'xx001', 'xx0x0']),
#               (21.5, ['101xx', '1x0xx', 'x01xx', 'xx0xx']),
#               (23.5, ['1xxxx', 'xxxxx']),
#               (2050, ['1000000000x1', '100000000x00', 'x00000000010', 'x000000000x1', 'x00000000x00'])]
#
#
# @test.describe('Binary with unknown bits: average to binary')
# def tests():
#     def verify(n, ans):
#         user_sol = average_to_binary(n)
#         if not isinstance(user_sol, list):
#             test.fail(f'Input={n}: Your solution should return a list.')
#         else:
#             test.assert_equals(sorted(user_sol), sorted(ans), f'Input={n}, with your return list sorted')
#
#     @test.it('Basic Tests')
#     def tests():
#         for n, ans in test_cases:
#             verify(n, ans)
#
# for num in range(0, (len(lista_sqr))):
#     n_temp = n - lista_sqr[num]
#     if n_temp == 0:
#         list_zero[num] = lista_sqr[num]
#         break
#     elif n_temp < 0:
#         pass
#     elif n_temp > 0:
#         n = n_temp
#         list_zero[num] = lista_sqr[num]
