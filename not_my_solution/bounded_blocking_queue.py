import threading
import collections

# we do not need editing lock since deque is already thread-safe

class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        self.capacity = capacity

        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        # self.editing = threading.Lock()

        self.queue = collections.deque()

    def enqueue(self, element):
      self.pushing.acquire()
    # self.editing.acquire()

      self.queue.append(element)

    # self.editing.release()
      self.pulling.release()

    def dequeue(self):
        self.pulling.acquire()
    #   self.editing.acquire()

        res = self.queue.popleft()

    #   self.editing.release()
        self.pushing.release()

        return res

    def size(self):
        return len(self.queue)
