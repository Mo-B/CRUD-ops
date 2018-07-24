class te_stack:
    def __init__(self):
        self.items = {}  # Dictionary to store TE info

    def push(self, item):
        self.items.update(item)

    def remove(self, item):
        self.items.pop(item)

    def is_empty(self):
        if self.items == {}:
            return True
        return False

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def printstats(self):
        return self.items
