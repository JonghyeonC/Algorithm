N = int(input())
num_list = list(map(int, input().split()))
check_num = int(input())
ans = 0
for num in num_list:
    if num == check_num:
        ans += 1
print(ans)