text = input()
# 알파벳의 갯수를 센다
alpha_cnt = {}
for i in text:
    if i in alpha_cnt:
        alpha_cnt[i] += 1
    else:
        alpha_cnt[i] = 1

alpha = []
for temp in alpha_cnt:
    alpha.append((temp, alpha_cnt[temp]))

alpha.sort()

odd_cnt = 0
center = ''
Palindrome = ''
for temp in alpha:
    if temp[1] % 2 != 0:
        odd_cnt += 1
        center += temp[0]
    Palindrome += temp[0] * (temp[1] // 2)

if odd_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(Palindrome + center + Palindrome[::-1])