from itertools import combinations

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    nums.pop(0)
    ans = list(combinations(nums, 6))
    for num in ans:
        print(*num)
    print()