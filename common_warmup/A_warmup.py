# queue
from collections import deque
q = deque()

try:
    q.append(1)
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
except:
    print('exception thrown')

# stack
stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)
try:
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
except:
    print('exception thrown')

# fast arr reverse
a = [1, 2, 3]
print(a[::-1])

# fast swap
x, y = 1, 2
x, y = y, x
print(x, y) # 2 1





