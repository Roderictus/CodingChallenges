import math
def solution(n):
    div_list =   [1000,500,100,50,10,5,1]
    characters = "MDCLXVI"
    except_dict = {"VIIII": "IX", "DCCCC":"CM", "LXXXX":"XC",
                   "IIII":"IV", "XXXX":"XL", "CCCC":"CD"}
    num_list = []
    for div in div_list:
        num_list.append(math.floor(n/div))
        if math.floor(n/div) >= 1 :
            n = n - (math.floor(n/div)) * div
    print(num_list)
    sol =""
    i =0
    for num in num_list:
        print(num)
        sol = sol + (num * characters[i])
        i += 1
    for key in except_dict.keys():
        sol = sol.replace(key,except_dict[key])
    return sol
temp = solution(999)
print(temp)

