# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
# characters included in the string, they should be returned as they are. Only letters from the latin/english
# alphabet should be shifted, like in the original Rot13 "implementation". {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
# 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r',
# 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
import string
def rot13(message):
    def get_key(value):
        for key,val in dict_of_vv.items():
            if val == value:
                return key
            else:
                pass
    def cypher(num):
        if num >= 26:
            num -= 26
            return num
        else:
            return num


    for element in cyphered:
        if element >= 26:
            element -= 26
            cyphered2.append(element)
        else:
            cyphered2.append(element)
    #string.ascii_lowercase
    #string.ascii_uppercase
    valid_v = string.ascii_lowercase
    dict_of_vv = dict()
    #print(len(valid_v))
    original = []
    cyphered = []
    cyphered2 = []
    i = 0
    for value in valid_v:
        dict_of_vv[i] = valid_v[i]
        i += 1
    #loop para mayússculas
    for letter in message:
        if letter in valid_v:
            temp = get_key(letter)
            print(temp)
            original.append(temp)
            cyphered.append(temp +13)
        elif letter.lower() in valid_v:
            temp = get_key(letter.lower())
            print(temp)
            original.append(temp)
            cyphered.append(temp + 13)
        else:
            temp = letter
            cyphered.append




    #print(cyphered)
    #print(cyphered2)
    sol = ""
    for element in cyphered2:
        temp2 = dict_of_vv.get(element)
        sol += temp2
        #print(temp2)


    return sol



temp =rot13("unonOmicon")
print(temp)


    #longitud
    #retener información de mayusculas minúsculas
    #llenar espacios
    #con puntuación
    #con letras
    #cambiar a mayúsculas

