def squareSumsRow(number):
    def aceptable_pairs(lista, usables):
        acceptable_pair = []
        for item in lista:
            #lista.remove(item)
            for numero in lista:
                if item + numero in usables and item != numero:
                    acceptable_pair.append([item, numero])
                    #acceptable_pair.append([numero,item])
        return acceptable_pair

    def flatten_and_count(nested_list):
        flatten = [num for sublist in nested_list for num in sublist]
        occurrences = {}
        for num in range(1,number + 1):
            #print(num)
            occurrences[num] = flatten.count(num)
        inicial = []
        for key,value in occurrences.items():
            if value == 2:
                inicial.append(key)
        print(occurrences)
        return inicial

    list = [number for number in range(1,number +1)]
    usable_squares = [item ** 2 for item in list if item ** 2 <= list[-1] + list[-2]]
    acceptable_pair =aceptable_pairs(list, usable_squares)
    inicial = flatten_and_count(acceptable_pair)
    print("esto es inicial")
    print(inicial)

    inicial = inicial[0]
    list.remove(inicial)
    sol = []
    sol.append(inicial)
    acceptableStep = []

    for number in list:
        for element in acceptable_pair:
            if element == sol[-1]:
                acceptableStep.append(element)
                # si hay sólo un camino que funciona podemos agregarlo a la lista de soluciones
                if len(acceptableStep) == 1:
                    sol.append(element[1])
                # si hay más de un camino hay que explorarlos
                else
                print(sol)



    return acceptable_pair


temp =squareSumsRow(15)

print(temp)
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