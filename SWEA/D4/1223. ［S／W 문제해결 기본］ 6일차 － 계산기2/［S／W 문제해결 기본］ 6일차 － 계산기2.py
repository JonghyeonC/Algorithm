T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = input()
    stack = []
    solve = []
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    isp = {'+': 1,
           '-': 1,
           '*': 2,
           '/': 2,
           '(': 0
           }  # 스택 안에서

    icp = {'+': 1,
           '-': 1,
           '*': 2,
           '/': 2,
           '(': 3
           }  # 스택 밖에서

    for i in range(n):
        if arr[i] in num:
            solve.append(arr[i])

        else:
            if len(stack) == 0:
                stack.append(arr[i])

            elif stack:
                if arr[i] == '(':
                    stack.append(arr[i])

                elif arr[i] == ')':
                    while stack[-1] != '(':
                        solve.append(stack.pop())
                    stack.pop()

                else:
                    while stack and icp[arr[i]] <= isp[stack[-1]]:
                        solve.append(stack.pop())
                    stack.append(arr[i])
    while stack:
        solve.append(stack.pop())

    equation = ''.join(solve)
    # print(equation)
    # print(stack)
    stack = []
    for i in range(len(equation)):
        if equation[i] in num:
            stack.append(equation[i])
        else:
            if equation[i] == '+':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 + num2)
            elif equation[i] == '-':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 - num2)
            elif equation[i] == '*':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 * num2)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 // num2)

    for i in range(len(stack)):
        print(f'#{tc} {stack[i]}')