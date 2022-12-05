T = int(input())
for _ in range(T):
    arr = list(input())
    temp = 0
    score = 0
    for i in arr:
        if i == 'O':
            temp += 1
            score += temp
        else:
            temp = 0
    print(score)