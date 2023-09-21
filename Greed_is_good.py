#https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

def score(dice):
    #lista = sorted(set(dice))
    #dice = sorted(dice)
    dice_dict = {}
    score = 0
    for elem in sorted(set(dice)):
        dice_dict[elem] = dice.count(elem)
    print(dice_dict.values())
    while any(x in [3,4,5,6] for x in dice_dict.values()):
        print("Hay una tercia")
        for key, value in dice_dict.items():
            print(key, ":", value)
            if value >= 3:
                print("tercia!")
                dice_dict[key] = value - 3
                if key == 1:
                    score += 1000
                elif key == 2:
                    score += 200
                elif key == 3:
                    score += 300
                elif key == 4:
                    score += 400
                elif key == 5:
                    score += 500
                elif key == 6:
                    score += 600
                break
    while any(x in [1,2] for x in dice_dict.values()):
        for key, value in dice_dict.items():
            print(key, ":", value)
            if value >= 1:
                print("número con valor")
                dice_dict[key] = value - 1
                if key == 1:
                    score += 100
                elif key == 2:
                    score += 0
                elif key == 3:
                    score += 0
                elif key == 4:
                    score += 0
                elif key == 5:
                    score += 50
                elif key == 6:
                    score += 0
                break
    return score




# lista = [5, 1, 3, 4, 1]#), 250)
# lista = [1, 1, 1, 3, 1]#), 1100)
# lista = [2, 3, 4, 6, 2]#), 0)
# lista = [4, 4, 4, 3, 3]#), 400)
lista = [1, 1, 2, 5, 5]#), 450)
#lista = [1,1,2,2,3,3]
temp = score(lista)
print(temp)


def score(dice):
    sum = 0
    counter = [0, 0, 0, 0, 0, 0]
    points = [1000, 200, 300, 400, 500, 600]
    extra = [100, 0, 0, 0, 50, 0]
    for die in dice:
        counter[die - 1] += 1

    for (i, count) in enumerate(counter):
        sum += (points[i] if count >= 3 else 0) + extra[i] * (count % 3)

    return sum