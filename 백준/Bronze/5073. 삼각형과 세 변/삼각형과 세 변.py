while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    else:
        if x == y == z:
            print("Equilateral")
        elif x == y or y == z or z == x:
            arr = [x, y, z]
            arr.sort(reverse=True)
            if arr[0] < arr[1] + arr[2]:
                print("Isosceles")
            else:
                print("Invalid")
        elif x != y != z:
            arr = [x, y, z]
            arr.sort(reverse=True)
            if arr[0] < arr[1] + arr[2]:
                print("Scalene")
            else:
                print("Invalid")
        else:
            print("Invalid")