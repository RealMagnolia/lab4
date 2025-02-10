def onlyEven():    #выводит только четные числа, сепарируя их запятой 
    n = int(input())
    for i in range(n+1):
        if i%2 == 0:
            yield i

gen = onlyEven()
ml = list(gen)
for j in ml:
    if j == ml[len(ml) - 1]:
        print(j)
    else:
        print(j, end=", ")