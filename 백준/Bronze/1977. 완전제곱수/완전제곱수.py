a = int(input())
b = int(input())
index = 1
tempList = list()

while True:
    if a<= index**2 and index**2 <=b:
         tempList.append(index**2)
    elif index**2 >b:
        break
    index+=1
    
if tempList == []:    
    print(-1)
    
else:
    print(sum(tempList))
    print(tempList[0])