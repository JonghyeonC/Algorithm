import sys

class Queue:
    def __init__(self):
        self.head = []

    def push(self, x):
        self.head.append(x)

    def pop(self):
        if self.empty(): return -1
        else: return self.head.pop(0)

    def size(self):
        return len(self.head)

    def empty(self):
        return len(self.head) == 0

    def front(self):
        if self.empty(): return -1
        else: return self.head[0]

    def back(self):
        if self.empty(): return -1
        else: return self.head[-1]

s = Queue()

for i in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == 'pop': print(s.pop())
    elif command[0] == 'size': print(s.size())
    elif command[0] == 'empty': print(1) if s.empty() else print(0)
    elif command[0] ==  'back': print(s.back())
    elif command[0] == 'front': print(s.front())
    else: s.push(int(command[1]))