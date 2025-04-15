class Queue:
    def __init__(self):
        self.queue = []

    def offer(self, item):
        self.queue.append(item)

    def poll(self):
        if len(self.queue) >= 1:
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if len(self.queue) >= 1:
            return self.queue[0]
        else:
            return None

    def get_queue(self):
        return self.queue

    def search(self, query_item):
        for index, item in enumerate(self.queue):
            if item == query_item:
                return index

        return None

    def clear(self):
        self.queue = []
        