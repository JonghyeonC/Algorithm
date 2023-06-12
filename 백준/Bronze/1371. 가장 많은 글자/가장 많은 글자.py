word = {}
while True:
    try:
        sentence = input()
        for i in sentence:
            if i in word:
                word[i] += 1
            elif i not in word:
                word[i] = 1
    except EOFError:
        ans = []
        if " " in word:
            del(word[" "])
        max_val = 0
        for value in word.values():
            max_val = max(value, max_val)
        for key, value in word.items():
            if value == max_val:
                ans.append(key)
        ans.sort()
        print(''.join(ans))
        break