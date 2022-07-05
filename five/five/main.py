from collections import Counter

int(input())
sizes = list(map(int, input().split()))
money = 0
stock = Counter(sizes)
for i in range(int(input())):
    x, y = list(map(int, input().split()))
    if stock[x]:
        money += y
        stock[x] -= 1
print(money)
# wersja bez countera
# shoes = int(input())
# aShoes = input().split()
# avableShoes = [int(i) for i in aShoes]
# customers = []
# for _ in range(int(input())):
#     customer = input().split()
#     customer[1] = int(customer[1])
#     customer[0] = int(customer[0])
#     customers.append(customer)
# money = 0
# for customer in customers:
#     if customer[0] in avableShoes:
#         money += customer[1]
#         avableShoes.remove(customer[0])
# print(money)
