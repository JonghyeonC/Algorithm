num_list = list(map(int, input().split()))

flag = 0
for i in range(1, len(num_list)):
    if num_list[i] < num_list[i - 1]:
        flag = 1
        break
    # else:
    #     flag = 0
if flag == 0 or len(num_list) == 1:
    print('Good')
elif flag == 1:
    print('Bad')