N = int(input())
users = []
for _ in range(N):
    users.append(list(input().split()))

users.sort(key=lambda x:int(x[0]))

for user in users:
    print(f'{user[0]} {user[1]}')