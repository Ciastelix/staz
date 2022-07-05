def p(x):
    return x**2


lists = 3
m = 1000
l1 = [2, 5, 4]
l2 = [3, 7, 8, 9]
l3 = [5, 5, 7, 8, 9, 10]
numbers = [l1, l2, l3]
while True:
    maxValues = []
    suma = 0
    for i in range(lists):
        maxValues.append(max(numbers[i]))
    for i in maxValues:
        suma += p(i)
