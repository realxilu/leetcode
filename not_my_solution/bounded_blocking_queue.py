from threading import Semaphore, Lock
from collections import deque

# collection.deque is already thread-safe. However, we want to use a '_lock' to indicate the working principal

class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        self.capacity = capacity

        self._add_flag = Semaphore(capacity)
        self._remove_flag = Semaphore(0)
        self._lock = Lock()

        self._q = deque()

    def enqueue(self, element):
      self._add_flag.acquire()
      self._lock.acquire()

      self._q.append(element)

      self._lock.release()
      self._remove_flag.release()

    def dequeue(self):
        self._remove_flag.acquire()
        self._lock.acquire()

        res = self._q.popleft()

        self._lock.release()
        self._add_flag.release()

        return res

    def size(self):
        return len(self._q)
