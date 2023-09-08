def row_sum_odd_numbers(n):
    return sum(([i+i+1 for i in range(0,sum([i for i in range(1, n+1)]))])[-n:])




temp = row_sum_odd_numbers(3)
print(temp)


# suma de los números en la n esima linea
# remover los números que no queremos sumar
#
# def row_sum_odd_numbers(n):
#     nden = sum([i for i in range(1, n+1)])
#     lista_impar = ([i+i+1 for i in range(0,nden)])[-n:]
#     print(lista_impar)
# lista_impar = sum(([i+i+1 for i in range(0,sum([i for i in range(1, n+1)]))])[-n:])
#     print(lista_impar)