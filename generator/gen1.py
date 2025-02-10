def newGen(n):    #выводит квадраты чисел 
    for i in range(n+1):
        yield i**2

gen = newGen(7)
for j in gen:
    print(j)