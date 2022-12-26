N = int(input())
nums = list(map(int, input().split()))
max_v = -1000
i = 0
temp = 0
while i < N:
    if nums[i] >= 0:
        temp += nums[i]
        if temp > max_v:
            max_v = temp
        i += 1
    elif nums[i] < 0:
        temp += nums[i]
        if temp > 0:
            if temp > max_v:
                max_v = temp
        else:
            if temp > max_v:
                max_v = temp
            temp = 0
        i += 1
print(max_v)