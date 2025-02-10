def squareNums():   #квадраты чисел в рейндже от а до б
    a, b = input().split()
    for i in range(int(a), int(b) + 1):
        yield i*i

gen = squareNums()
for j in gen:
    print(j)
