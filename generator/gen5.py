def revGen():   #возвращает все числа от н до нуля
    n = int(input())
    for i in range(n, -1, -1):
        yield i

gen = revGen()
for j in gen:
    print(j)
