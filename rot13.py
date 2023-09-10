import string
def rot13(message):
    def get_key(value):
        for key,val in dict_of_vv.items():
            if val == value:
                return key
            else:
                pass
    def cypher(num):

        if num >= 126:
            num -= 126
            crypto = dict_of_vv[num].upper()
            return crypto
        elif num >= 100:
            num -= 100
            crypto = dict_of_vv[num].upper()
            return crypto

        elif num >= 26:
            num -= 26
            crypto = dict_of_vv[num]
            return crypto
        else:
            crypto = dict_of_vv[num]
            return crypto

    valid_v = string.ascii_lowercase
    dict_of_vv = dict()
    cyphered = []

    for i in range(0, len(valid_v)):
        dict_of_vv[i] = valid_v[i]

    for letter in message:
        if letter in valid_v:
            temp = get_key(letter)
            cyphered.append(temp +13)

        elif letter.lower() in valid_v:
            temp = get_key(letter.lower())
            cyphered.append(temp + 100 + 13) # mayuscula

        else:
            temp = letter
            cyphered.append(temp)
    sol = ""
    print(cyphered)
    for element in cyphered:
        if isinstance(element,int):
            sol += str(cypher(element))
        else:
            sol += element
    return sol

