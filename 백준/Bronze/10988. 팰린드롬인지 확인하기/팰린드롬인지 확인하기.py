word = input()
N = len(word)
flag = 0
for i in range(N // 2):
    if word[i] != word[N - 1 - i]:
        flag = 1
        break
if flag == 0:
    print(1)
else:
    print(0)
