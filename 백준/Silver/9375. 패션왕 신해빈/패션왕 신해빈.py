T = int(input())
for _ in range(T):
    n = int(input())
    cloth_dict = {}
    for _ in range(n):
        cloth, kind = map(str, input().split())
        if kind in cloth_dict.keys():
            cloth_dict[kind].append(cloth)
        else:
            cloth_dict[kind] = [cloth]
    together = 1
    for k in cloth_dict.values():
        together *= len(k) + 1
    print(together - 1)