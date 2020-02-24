from collections import OrderedDict


class ActionSpace:

    MIN_FIELD_ELEMENT = ord('A')
    MAX_FIELD_ELEMENT = ord('Z')
    MAX_FIELD_SIZE = MAX_FIELD_ELEMENT - MIN_FIELD_ELEMENT

    def __init__(self, length=None):
        self.actions = None
        if length:
            self.reset(length)

    def reset(self, length):
        if not self.actions or len(self.actions) != length:
            size = length ** 2
            numeric_action = []

            for i in range(size):
                row, column = divmod(i, length)
                column += 1

                character_repetition, character = divmod(row, ActionSpace.MAX_FIELD_SIZE)
                character_repetition += 1
                character = chr(character + ActionSpace.MIN_FIELD_ELEMENT)
                character *= character_repetition

                alphabet = f'{character}{column}'
                numeric_action.append((i, alphabet))

            self.actions = OrderedDict(numeric_action)

    def __len__(self):
        return len(self.actions)
