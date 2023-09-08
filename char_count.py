from collections import defaultdict
import string

def get_char_count(s):
    alphabet = string.ascii_lowercase + str(1234567890)
    temp = sorted(s.lower())
    hilo = ""
    for char in temp:
        if char in alphabet:
            hilo += char
    print(f"hilo: {hilo}")
    unique = sorted(set(hilo))
    print(f"unique: {unique}")
    value_list = [hilo.count(char) for char in unique]
    value_list = sorted(set(value_list), reverse = True)
    #print(f"sorted unique value list : {value_list}")
    sol = dict()
    for char in unique:
        if int(hilo.count(char)) in sol:
            sol[int(hilo.count(char))].append(char)
        else:
            sol[int(hilo.count(char))] = [char]
    sol = {k:sol[k] for k in value_list}
    return sol


print(get_char_count("Mississippi"))#, {4: ["i", "s"], 2: ["p"], 1: ["m"]}))
print(get_char_count("Hello. Hello? HELLO!"))#, {6: ["l"], 3: ["e", "h", "o"]}))
print(get_char_count("aaa...bb...c!"))#, {3: ["a"], 2: ["b"], 1: ["c"]})
print(get_char_count("abc123"))#, {1: ["1", "2", "3", "a", "b", "c"]})
print(get_char_count("aaabbbccc"))#, {3: ["a", "b", "c"]})

# def get_char_count(s):
#     counts = {}
#     for c in (c.lower() for c in s if c.isalnum()):
#         counts[c] = counts[c] + 1 if c in counts else 1
#     m = {}
#     for k, v in counts.items():
#         m[v] = sorted(m[v] + [k]) if v in m else [k]
#     return m