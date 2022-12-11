N = int(input())
ans_list = []
for _ in range(N):
    word = input()
    n = len(word)
    temp = ""
    for i in range(n):
        if word[i].isdecimal():
            temp += word[i]
        elif word[i].isdecimal() == False:
            if temp:
                ans_list.append(int(temp))
                temp = ""
    if temp:
        ans_list.append(int(temp))
ans_list.sort()
for ans in ans_list:
    print(ans)