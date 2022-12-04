data = input()

datatype = type(data)

if datatype is str:
    print(ord(data))
elif datatype is int:
    print(chr(data))