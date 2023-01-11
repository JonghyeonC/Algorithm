import sys
input = sys.stdin.readline
S, C = map(int, input().split())

sp = []                            # 파 길이를 담을 배열
for _ in range(S):
    sp.append(int(input()))

start = 1                          # 길이를 탐색하기 위해 이분탐색을 진행할 때 시작 값
end = max(sp)                      #             "                          마지막 값
ans = 0                            # 파닭에 들어갈 파의 길이
while start <= end:                # 이분탐색 실시
    cnt = 0                        # 파의 길이에 따라서 넣을 수 있는 치킨의 갯수
    mid = (start + end) // 2       # 최대의 파 길이에서 최대로 넣을 수 있는 파의 길이를 이분탐색으로 구함

    for num in sp:                 # 파 길이를 순회하면서 넣을 수 있는 파닭의 개수를 구함
        cnt += num // mid

    if cnt >= C:                   # 파닭의 갯수보다 같거나 많을 경우에 더 길게 넣을 수 있는 경우가 있을 수도 있으므로
        start = mid + 1            # 파의 최대길이를 늘리고 다시 진행
        ans = max(mid, ans)        # 파의 최대길이라고 예측한 중간값과 현재의 최대 길이 중 최대값을 겟
    else:                          # 파닭의 갯수가 요구사항을 충족못할 경우 최대 길이를 줄임
        end = mid - 1

print(sum(sp) - C * ans)           # 전체 파의 길이 중 파닭에 넣는 파의 길이를 뺀 값을 구함
