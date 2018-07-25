class te_stack:
    def __init__(self):
        self.items_ = {}  # Dictionary to store TE info

    def push(self, item):
        self.items_.update(item)

    def remove(self, item):
        self.items_.pop(item)

    def is_empty(self):
        if self.items_ == {}:
            return True
        return False

    def peek(self):
        if not self.is_empty():
            return self.items_[-1]

    def printstats(self):
        # return self.items
        print("{" + "\n".join("{}: {}".format(k, v) for k, v in self.items_.items()) + "}")
