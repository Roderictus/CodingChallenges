def square_sums(number):
    def aceptable_pairs(lista, usables):
        acceptable_pair = []
        for item in lista:
            #lista.remove(item)
            for numero in lista:
                if item + numero in usables and item != numero:
                    acceptable_pair.append([item, numero])
                    #acceptable_pair.append([numero,item])
        return acceptable_pair
    def backtrack(remaining, current_sequence):
        if not remaining:
            return current_sequence
        last_num = current_sequence[-1]
        for num in remaining:
            if (last_num + num) in usable_squares:
                new_sequence = current_sequence + [num]
                #print(new_sequence)
                #time.sleep(1)
                new_remaining = remaining - {num}
                result = backtrack(new_remaining, new_sequence)
                if result:
                    return result
        return None

    lista_numeros = [number for number in range(1,number +1)]
    usable_squares = [item ** 2 for item in lista_numeros if item ** 2 <= lista_numeros[-1] + lista_numeros[-2]]
    #
    for start in range(1, number + 1):
        sequence = backtrack(set(range(1, number + 1)) - {start}, [start])
        if sequence:
            return sequence
    return None

temp = square_sums(6)

print(temp)

    # def flatten_and_count(nested_list):
    #     flatten = [num for sublist in nested_list for num in sublist]
    #     occurrences = {}
    #     for num in range(1,number + 1):
    #         #print(num)
    #         occurrences[num] = flatten.count(num)
    #     inicial = []
    #     for key,value in occurrences.items():
    #         if value == 2:
    #             inicial.append(key)
    #     print(occurrences)
    #     return inicial



    #lista_numeros.remove(inicial)
    # sol = [[8,1]]
    # #sol.append(inicial)
    # acceptableStep = []
    # print("Esto es lista")
    # print(lista_numeros)
    # print("Esto es acceptable pair")
    # print(acceptable_pair)
    #
    # while len(sol) < len(lista_numeros):
    #     valores_aceptables = []
    #     for element in acceptable_pair:
    #         if element[0] == sol[-1][1]:
    #             print(f"valor aceptable {element}")
    #             valores_aceptables.append(element)
    #     print("Estos son valores aceptables")
    #     print(valores_aceptables)
    #     sol += 1
    #
    #     for valor in valores_aceptables:
    #         for element in acceptable_pair:
    #
    # def recursive:




    # for number in lista_numeros:
    #     for element in acceptable_pair:
    #        #print(element)
    #         if element[0] == sol[-1]:
    #             acceptableStep.append(element)
    #             #print("Esto es el primer acceptable step")
    #             #print(acceptableStep)
    #             # si hay sólo un camino que funciona podemos agregarlo a la lista de soluciones
    #             # una vez añadido hay que removerlo de la lista
    #             acceptable_pair.remove(element)
    #             acceptable_pair.remove([element[1],element[0]])
    #             print(acceptable_pair)
    #
    #             if len(acceptableStep) == 1:
    #                 sol.append(element[1])
    #             # si hay más de un camino hay que explorarlos
    #             #función para profundidad arbitraria
    #             else:
    #                 for thing in acceptableStep:
    #                     print("esto es thing")
    #                     print(thing)
    # print(f"esto es sol : {sol}")
    #
    #
    # return acceptable_pair

# todo crear un método para sublistas de profundidad variable
# todo crear función para borrar pareja ya utilizada
# todo ordenar los pares viables de acuerdo a los que tienen menor probabilidad de ocurrencia
# any(x in [2,1,8] for x in [3,4,5,6])
# Para revisdar si están todos los números
# number_list = []
# for cosa in acceptable_pair:
#     for number in cosa:
#         number_list.append(number)
#
# print(set(number_list))

#si se usa 8,1,3 quitar 8,1 1,8 1,3, 3,1 de la lista