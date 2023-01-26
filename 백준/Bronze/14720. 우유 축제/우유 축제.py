N = int(input())
arr = list(map(int, input().split()))
rule = {0 : 1, 1 : 2, 2 : 0}
now = 0
start = False
cnt = 0
for store in arr:
    if store == 0 and start == False:
        start = True
        cnt += 1
    elif store == rule[now] and start == True:
        cnt += 1
        now = rule[now]
print(cnt)