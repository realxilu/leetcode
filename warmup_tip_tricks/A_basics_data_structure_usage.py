#------------------------------------------------------------------------
# QUEUE
from collections import deque
q = deque()  # supports multithreading

try:
    q.append(1)
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
except:
    print('exception thrown')

#------------------------------------------------------------------------
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

#------------------------------------------------------------------------
# HASHMAP |  DICTIONARY
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

# defaultdict with type 'list', it can be any class such as TreeNode
import collections
collections.defaultdict(list)

#------------------------------------------------------------------------
# LAMBDA EXPRESSION
l1 = list(map(lambda x: int(x), l1))

#------------------------------------------------------------------------
# MAP
vals = [1,2,3]
' '.join(map(str, vals))
# above will produce '1 2 3'



