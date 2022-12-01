T = int(input())
for _ in range(T):
    arr = list(input())
    stack = []
    flag = False
    for parent in arr:
        if parent == "(":
            stack.append("(")
        elif parent == ")":
            if stack:
                stack.pop()
            else:
                flag = True
    if len(stack) or (flag == True):
        print("NO")
    else:
        print("YES")