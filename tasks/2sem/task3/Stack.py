import sys


class Stack:
    def __init__(self, obj):
        self.buffer = []
        for i in obj:
            self.buffer.append(i)

    def __len__(self):
        return len(self.buffer)

    def __str__(self):
        string = ''
        for i in self.buffer:
            string += str(i)
            string += ' '
        return string

    def push(self, val):
        self.buffer.append(val)

    def pop(self):
        return self.buffer.pop()

    def top(self):
        return self.buffer[-1]


exec(sys.stdin.read())
