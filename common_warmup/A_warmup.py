# QUEUE
from collections import deque
q = deque() # thread-safe

try:
    q.append(1)
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
except:
    print('exception thrown')

# STACK
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

# HASHMAP/DICTIONARY
dic = {}
dic['a'] = 'alex'
dic['b'] = 'bob'
dic['c'] = 'charie'

print(dic['a'])
print(dic['b'])
print(dic['c'])
print(dic.get('a'))
print(dic.get('a', '-1000'))
# if the key doesn't exist return a default value
print(dic.get('z', '-1000'))

for k in dic.keys():
    print(k)

for v in dic.values():
    print(v)

# int values need conversion
for k, v in dic.items():
    print(k + ' -> ' + v)

# --------------------
# fast arr reverse
a = [1, 2, 3]
print(a[::-1])

# fast swap
x, y = 1, 2
x, y = y, x
print(x, y) # 2 1






