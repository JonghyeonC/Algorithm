N = int(input())
words = list(input())
tbl = [['A', 'C', 'A', 'G'],
       ['C', 'G', 'T', 'A'],
       ['A', 'T', 'C', 'G'],
       ['G', 'A', 'G', 'T']]
while len(words) != 1:
    b = words.pop()
    a = words.pop()
    tmp_1 = tmp_2 = -1
    if a == 'A':
        tmp_1 = 0
    elif a == 'G':
        tmp_1 = 1
    elif a == 'C':
        tmp_1 = 2
    elif a == 'T':
        tmp_1 = 3
    if b == 'A':
        tmp_2 = 0
    elif b == 'G':
        tmp_2 = 1
    elif b == 'C':
        tmp_2 = 2
    elif b == 'T':
        tmp_2 = 3
    tmp = tbl[tmp_1][tmp_2]
    words.append(tmp)
print(''.join(words))