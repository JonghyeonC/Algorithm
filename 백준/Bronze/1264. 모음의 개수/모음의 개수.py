while True:
    text = input().lower()
    if text == "#":
        break
    arr = ['a', 'e', 'i', 'o', 'u']
    ans = 0
    for alpha in text:
        for vow in arr:
            if alpha == vow:
                ans += 1
    print(ans)