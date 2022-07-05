from itertools import combinations
input()
c = list(combinations(input().split(), int(input())))
cs = 0
for i in c:
    if "a" in i:
        cs+=1
print(round(cs/len(c),3))