class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)
        self.size += 1
        return item

    def dequeue(self):
        if not self.storage:
            return None
        item = self.storage.pop(0)
        self.size -= 1
        return item

    def len(self):
        return len(self.storage)
