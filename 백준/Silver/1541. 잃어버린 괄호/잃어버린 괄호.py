numbers = input().split('-')
sum_number = []
for number in numbers:
    add = number.split('+')
    temp = 0
    for i in add:
        temp += int(i)
    sum_number.append(temp)

ans = sum_number[0]
sum_number.pop(0)
for number in sum_number:
    ans -= number
print(ans)