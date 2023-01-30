word = 'A' + input()
ans = 0
for i in range(len(word) - 1):
    clock = ord(word[i]) - ord(word[i + 1])
    counter = ord(word[i+1]) - ord(word[i])

    if clock < 0:
        clock += 26
    if counter < 0:
        counter += 26
    ans += min(clock, counter)
print(ans)