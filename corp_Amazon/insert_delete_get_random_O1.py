import random

class RandomizedSet:
    def __init__(self):
        self._list = []
        self._dic = {}

    def insert(self, val: int) -> bool:
        if val not in self._dic:
            self._list.append(val)
            self._dic[val] = len(self._list) - 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self._dic:
            index, last = self._dic[val], self._list[-1]
            # swap the to be removed val with the last element
            self._list[index], self._list[-1] = self._list[-1], self._list[index]
            # swap values in the dictionary due to the position change
            self._dic[val], self._dic[last] = self._dic[last], self._dic[val]
            self._list.pop()
            self._dic.pop(val)
            return True

        return False

    def getRandom(self) -> int:
        rand = random.randint(0, len(self._list) - 1)
        return self._list[rand]

# [KEY] composite data structure, can't do it with array alone
# Hashmap + array
