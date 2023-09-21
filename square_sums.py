def squareSumsRow(number):
    def aceptable_pairs(lista, usables):
        acceptable_pair = []
        for item in lista:
            lista.remove(item)
            for numero in lista:
                if item + numero in usables:
                    acceptable_pair.append([item, numero])
        return acceptable_pair

    list = [number for number in range(1,number +1)]

    usable_squares = [item ** 2 for item in list if item ** 2 <= list[-1] + list[-2]]
    print(usable_squares)

    acceptable_pair =aceptable_pairs(list, usable_squares)
    print("Estos son los usable pairs")
    print(acceptable_pair)
    number_list = []
    for cosa in acceptable_pair:
        for number in cosa:
            number_list.append(number)

    print(set(number_list))

    return number_list




temp =squareSumsRow(15)

# any(x in [2,1,8] for x in [3,4,5,6])
