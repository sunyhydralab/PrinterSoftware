class PriorityQueue:
    def __init__(self):
        self.table = {}
        self.sorted_keys = []

    def enque(self, item):
        if item.priority not in self.table:
            self.table[item.priority] = []
            self.sorted_keys.append(item.priority)
            self.sorted_keys.sort(reverse=True)
        self.table[item.priority].append(item)

    def deque(self):
        out = self.table[self.sorted_keys[0]].pop(0)
        if len(self.table[self.sorted_keys[0]]) == 0:
            self.table.remove(self.sorted_keys.pop(0))
        return out
