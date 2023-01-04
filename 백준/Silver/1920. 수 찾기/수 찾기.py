N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
check_list = list(map(int, input().split()))
num_list.sort()

for num in check_list:
    left = 0
    right = N - 1
    flag = 0
    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] == num:
            print(1)
            flag = 1
            break
        elif num_list[mid] < num:
            left =  mid + 1
        else:
            right = mid - 1
    if flag == 0:
        print(0)