if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    scores = list(set([i[1] for i in records]))
    scores.sort()
    records.sort()
    secLow = scores[1]
    for i in records:
        if i[1] == secLow:
            print(i[0])
