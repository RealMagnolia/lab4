def threeFour(n):   #выводят числа, которые делятся на тройку и четверку одновременно
    for i in range(n+1):
        if i%3 == 0 and i%4 == 0:
            yield i

gen = threeFour(40)
for j in gen:
    print(j)