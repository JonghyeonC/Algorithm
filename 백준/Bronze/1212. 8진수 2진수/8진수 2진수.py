n = input()
#8진수변환
m = int(n, 8) 
#2진수 변환 후, 0b 삭제
m = format(m, 'b')

print(m)