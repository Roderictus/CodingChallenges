# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python
def solution(args):
    string = ""
    primero = False
    for i in range(1, len(args)+1):
        print(f"ciclo" + str(i) )

        if i == (len(args)):
            if primero == True:
                print(f"esto es i : {i} esto es lenarg {len(args)} esto {args[i-1]}")
                print(f"string es: {string}")
                string = string + "-" + str(args[i - 1])
                #primero = False
                print(5)
            elif primero == False:
                #string = string + str(args[i - 1]) + ","
                #primero = True
                print(6)

        elif args[i]-args[i-1] > 1:
            if primero == True:
                string = string + "-" + str(args[i - 1]) + ","
                primero = False
                print(3)
            elif primero == False:
                string = string + str(args[i - 1]) + ","
                primero = False
                print(4)

        elif args[i]-args[i-1] == 1: #funcion distancia
            if primero == True:
                #prim_arg = str(args[i-1])
                #string = string + str(args[i-1]) + "-"
                print(1)
            elif primero == False:
                string = string + str(args[i - 1])
                primero = True
                print(2)

    return string

#args = [1,2,3,5,7,11,12,13]
args = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]
#args = [-3,-2,-1,2,10,15,16,18,19,20]
#args = [0,1,2,3,4,5,7,9,11,12,13,14,15,17,20,24]
temp= solution(args)
print(temp)

# # if args[i+1]-args[i] == 1:
# # list.append()
#
# # string = string + str(args[i])  + "-"+ str(args[i + 1]) + ","
# pass
# else:
# # list.append(args[i])
# # string = string + str(args[i]) + ","

# list = []

#     if args[i + 1] - args[i] != 1:
#         string = string + str(args[i]) + "," + str(args[i + 1])
#         print(f"distancia diff uno {args[i]},  {args[i + 1]}")
#     else:
#         string = string + str(args[i])
#         print(f" distancia uno {args[i]},  {args[i + 1]}")  # aqui ya sabemos que hay más, pero que tantos más_
#         # if args[i + 2] - args[i]
#
# return string

# def solution(args):
#     string = ""
#     primero = True
#     for i in range(1, len(args) + 1):
#         print(f"ciclo" + str(i) )
#         if i == (len(args)) or args[i]-args[i-1] > 1:
#             if primero == True:
#                 string = string + str(args[i - 1]) + ","
#                 #primero = False
#                 print(3)
#             elif primero == False:
#                 if i == (len(args)):
#                     string = string + str(args[i - 1]) + ","
#                 primero = True
#                 print(4)
#         elif args[i]-args[i-1] == 1: #funcion distancia
#             if primero == False:
#                 print(2)
#                 #pass
#             elif primero == True:
#                 #prim_arg = str(args[i-1])
#                 primero = False
#                 string = string + str(args[i-1]) + "-"
#                 print(1)
#                 #pass
#         #     if primero == True:
#         #         string = string + str(arg)
#         #         primero = False
#         #     if primero == False:

