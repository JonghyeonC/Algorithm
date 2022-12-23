num1, num2 = map(list, input().split())
n_num1 = num1[::-1]
n_num2 = num2[::-1]
if int(''.join(n_num1)) > int(''.join(n_num2)):
    print(''.join(n_num1))
else:
    print(''.join(n_num2))