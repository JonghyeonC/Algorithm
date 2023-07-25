import sys
input = sys.stdin.readline


def digitSum(numlist):
    tmp = 0
    for num in numlist:
        if num.isdigit():
            tmp += int(num)
    return tmp


N = int(input().rstrip())
nums = []
for _ in range(N):
    nums.append(input().rstrip())
nums.sort(key=lambda x: (len(x), digitSum(x), x))

for i in nums:
    print(i)