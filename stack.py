class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) >= 1:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) >= 1:
            return self.stack[-1]
        else:
            return None

    def clear(self):
        self.stack = []

    def get_stack(self):
        return self.stack

    def search(self, query_item):
        for index, item in enumerate(self.stack):
            if item == query_item:
                return index

        return None
