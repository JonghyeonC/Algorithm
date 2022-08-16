arr = [int(input()) for _ in range(9)]
answer = []
for i in range(1 << 9):
    total = 0
    sub_list = []
    for j in range(9):
        if i & (1 << j):
            sub_list.append(arr[j])
    for i in range(len(sub_list)):
        total += sub_list[i]
    if len(sub_list) == 7 and total == 100:
        answer = sub_list

for i in range(6):
    min_idx = i
    for j in range(i+1, 7):
        if answer[min_idx] >= answer[j]:
            min_idx = j
    answer[i], answer[min_idx] = answer[min_idx], answer[i]
for i in answer:
    print(i)