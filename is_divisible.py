def is_divisible(*args):
    res = [args[0] % args[i]==0 for i in range(1, len(args))]
    if False in res:
        return False
    else:
        return True

temp = is_divisible(10,2,5,2,6,2)
print(temp)

# def is_divisible(*args):
#     num = args[0]
#     for n in range(1,len(args)):
#         if num % args[n] == 0 and n == len(args)-1:
#             return True
#         elif num % args[n] == 0:
#             pass
#         else:
#             return False
def is_divisible(n, *args):
    return all(not n % i for i in args)

