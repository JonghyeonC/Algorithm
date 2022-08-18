n = int(input())
arr = list(map(int, input().split()))

inc_cnt = 1
dec_cnt = 1
max_val = 1
for i in range(n-1):
    if arr[i] <= arr[i + 1]:
        inc_cnt += 1
        if max_val < inc_cnt:
            max_val = inc_cnt
    else:
        inc_cnt = 1

for i in range(n-1):
    if arr[i] >= arr[i+1]:
        dec_cnt += 1
        if max_val < dec_cnt:
            max_val = dec_cnt
    else:
        dec_cnt = 1

print(max_val)