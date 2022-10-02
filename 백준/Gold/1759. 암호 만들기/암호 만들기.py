def dfs(k, s):
    v = c = 0
    if k == L:
        for i in range(L):
            if result[i] in vowels:
                v += 1
            else:
                c += 1
        if v >= 1 and c >= 2:
            print(''.join(result))
    else:
        for i in range(s, C):
            result.append(words[i])
            dfs(k + 1, i + 1)
            result.pop()


L, C = map(int, input().split())
words = input().split()
words.sort()
result = []
vowels = 'aeiou'
dfs(0, 0)