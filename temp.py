def to_camel_case(text):
    temp = text.split("-")
    lista = []
    for word in temp:
        print(word)
        word2 = word.split("_")
        print(word2)
        lista.extend(word2)

    a = lista[0]
    print(a)
    b = lista[1:]
    print(b)
    bcap = ""
    for word in b:
        word = word.capitalize()
        print(word)
        bcap += word
        print(bcap)

    sol = a + bcap
    return sol

temp2 = to_camel_case('the_stealth_warrior')
print(temp2)