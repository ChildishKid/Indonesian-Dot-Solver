class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == []

    def insert(self, h, data):
        self.queue.append((h, data))

    def delete(self):
        # False = smallest to largest
        self.queue.sort(key=lambda el: el[0], reverse=True)
        return self.queue.pop()

    def get_queue_states(self):
        states_actions = [i[1] for i in self.queue]
        states = [i[1] for i in states_actions]
        return states

    def __len__(self):
        return len(self.queue)