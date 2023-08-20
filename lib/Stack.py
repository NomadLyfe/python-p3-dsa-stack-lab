class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit
        if len(items) <= limit:
            self.items = items
        else:
            for i in range(limit):
                self.items.append(items[i])

    def isEmpty(self):
        return not self.items

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop(-1)

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if not (target in self.items):
            return -1
        return len(self.items) - 1 - self.items.index(target)
