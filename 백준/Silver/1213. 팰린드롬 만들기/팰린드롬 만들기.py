ATOZ = input()
flag = 0
front = mid = back = ''

for i in range(65,91):
    if chr(i) in ATOZ:
        cnt = ATOZ.count(chr(i))
        if cnt%2 == 1:
            if mid != '': 
                flag = 1
                break
            mid = chr(i)
        
        front = front + chr(i)*(cnt//2)
        back = back + chr(i)*(cnt//2)
            
print( "I'm Sorry Hansoo" if flag else front + mid + back[::-1]) 