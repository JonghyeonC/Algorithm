import sys
input = sys.stdin.readline


cnt = 0
N = int(input())
for _ in range(N):
    word = input()
    flag = 0
    words = {}
    for i in range(len(word)):
        if i != 0:
            if word[i] in words and word[i - 1] != word[i]:
                flag = 1
                break
            elif word[i] not in words:
                words[word[i]] = 1
        elif i == 0:
            words[word[i]] = 1
    if flag == 0:
        cnt += 1
print(cnt)