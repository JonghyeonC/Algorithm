arr = input()
cnt_one = 0
cnt_zero = 0
arr_one = arr.split('0')
arr_zero = arr.split('1')
for i in arr_one:
    if i:
        cnt_one += 1
for i in arr_zero:
    if i:
        cnt_zero += 1

ans = 0
if cnt_zero == 0 or cnt_one == 0:
    ans = 0
else:
    flag = 0
    if cnt_zero >= cnt_one:
        for i in arr:
            if i == '1':
                flag = 1
            else:
                if flag == 0:
                    flag = 0
                elif flag == 1:
                    flag = 0
                    ans += 1
        if flag == 1:
            ans += 1
            flag = 0
    else:
        for i in arr:
            if i == '0':
                flag = 1
            else:
                if flag == 0:
                    flag = 0
                elif flag == 1:
                    flag = 0
                    ans += 1
        if flag == 1:
            ans += 1
            flag = 0
print(ans)