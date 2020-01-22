class Space(object):
    def sample(self):
        raise NotImplementedError

    def contains(self, item):
        raise NotImplementedError

    def __contains__(self, item):
        return self.contains(item)

