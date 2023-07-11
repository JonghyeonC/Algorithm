numbers = list(input())
dict = [0] * 10
for num in numbers:
    if int(num) == 9:
        dict[6] += 1
    else:
        dict[int(num)] += 1
if dict[6] > 0:
    if dict[6] % 2 == 0:
        dict[6] //= 2
    else:
        dict[6] = dict[6] // 2 + 1
print(max(dict))