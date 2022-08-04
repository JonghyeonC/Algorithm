num = int(input())
for test_case in range(1, num+1):
    pri_1, pri_2, lim_w, pri_add, use_w = map(int, input().split()) 
    total_a = pri_1 * use_w
    if use_w <= lim_w:
        total_b = pri_2
    elif use_w > lim_w:
        total_b = pri_2 + (use_w - lim_w) * pri_add
    
    if total_a <= total_b:
        print(f'#{test_case} {total_a}')
    elif total_b <= total_b:
        print(f'#{test_case} {total_b}')