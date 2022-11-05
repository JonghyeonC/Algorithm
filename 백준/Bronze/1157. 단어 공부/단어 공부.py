word = input().upper()
words = list(word)

count_dict = {}
for w in words:
    if w in count_dict:
        count_dict[w] += 1
    else:
        count_dict[w] = 1

max_val = max(count_dict.values())

ans = []
for key in count_dict.keys():
    if count_dict[key] == max_val:
        ans.append(key)
if len(ans) >= 2:
    print('?')
else:
    print(*ans)